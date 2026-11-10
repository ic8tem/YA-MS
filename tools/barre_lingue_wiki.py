# Wiki YA-MS: rigenera la barra delle lingue in cima a ogni pagina (e nella _Sidebar) con tutte le lingue presenti.
# Uso: python3 tools/barre_lingue_wiki.py
import glob, io, os, re
W = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'wiki')
LANGS = [('', 'English'), ('it', 'Italiano'), ('de', 'Deutsch'), ('nl', 'Nederlands'), ('fr', 'Français'), ('es', 'Español'),
         ('pt', 'Português'), ('pt-BR', 'Português (Brasil)'), ('da', 'Dansk'), ('nb', 'Norsk'), ('sv', 'Svenska'), ('is', 'Íslenska'),
         ('et', 'Eesti'), ('lt', 'Lietuvių'), ('lv', 'Latviešu'), ('pl', 'Polski'), ('cs', 'Čeština'), ('hu', 'Magyar'), ('ro', 'Română'),
         ('el', 'Ελληνικά'), ('ru', 'Русский'), ('uk', 'Українська'), ('tr', 'Türkçe'), ('af', 'Afrikaans'), ('ar', 'العربية'),
         ('he', 'עברית'), ('ur', 'اردو'), ('hi', 'हिन्दी'), ('bn', 'বাংলা'), ('th', 'ไทย'), ('id', 'Bahasa Indonesia'), ('tl', 'Tagalog'),
         ('ja', '日本語'), ('ko', '한국어'), ('zh', '中文'), ('zh-TW', '中文 (繁體)')]
codes = [c for c, _ in LANGS if c]
pages = sorted(os.path.basename(f)[:-3] for f in glob.glob(os.path.join(W, '*.md'))
               if not os.path.basename(f).startswith('_') and not re.search(r'-(%s)\.md$' % '|'.join(map(re.escape, codes)), f))
present = lambda page, c: os.path.exists(os.path.join(W, page + ('-' + c if c else '') + '.md'))
def bar(page, cur):
    out = []
    for c, n in LANGS:
        if not present(page, c): continue
        out.append('**%s**' % n if c == cur else '[%s](%s)' % (n, page + ('-' + c if c else '')))
    return ' · '.join(out)
n = 0
for page in pages:
    for c, _ in LANGS:
        f = os.path.join(W, page + ('-' + c if c else '') + '.md')
        if not os.path.exists(f): continue
        lines = io.open(f, encoding='utf-8').read().split('\n')
        b = bar(page, c)
        if lines and ('](' + page in lines[0] or lines[0].startswith('**')) and ' · ' in lines[0]:
            if page == 'Home' and c == '' and lines[0].startswith('**English**'): lines[0] = b
            else: lines[0] = b
        else:
            lines = [b, ''] + lines
        io.open(f, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines)); n += 1
sb = os.path.join(W, '_Sidebar.md')
s = io.open(sb, encoding='utf-8').read()
s = re.sub(r'\*\*Languages:\*\* .*', '**Languages:** ' + ' · '.join('[%s](Home%s)' % (nm, '-' + c if c else '') for c, nm in LANGS if present('Home', c)), s)
io.open(sb, 'w', encoding='utf-8', newline='\n').write(s)
print('pagine', len(pages), 'file aggiornati', n)
