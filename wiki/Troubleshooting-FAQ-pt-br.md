[English](Troubleshooting-FAQ) · [Italiano](Troubleshooting-FAQ-it) · [Deutsch](Troubleshooting-FAQ-de) · [Nederlands](Troubleshooting-FAQ-nl) · [Français](Troubleshooting-FAQ-fr) · [Español](Troubleshooting-FAQ-es) · [Português](Troubleshooting-FAQ-pt) · **Português (Brasil)** · [Dansk](Troubleshooting-FAQ-da) · [Norsk](Troubleshooting-FAQ-nb) · [Svenska](Troubleshooting-FAQ-sv) · [Íslenska](Troubleshooting-FAQ-is) · [Eesti](Troubleshooting-FAQ-et) · [Lietuvių](Troubleshooting-FAQ-lt) · [Latviešu](Troubleshooting-FAQ-lv) · [Polski](Troubleshooting-FAQ-pl) · [Čeština](Troubleshooting-FAQ-cs) · [Magyar](Troubleshooting-FAQ-hu) · [Română](Troubleshooting-FAQ-ro) · [Ελληνικά](Troubleshooting-FAQ-el) · [Русский](Troubleshooting-FAQ-ru) · [Українська](Troubleshooting-FAQ-uk) · [Türkçe](Troubleshooting-FAQ-tr) · [Afrikaans](Troubleshooting-FAQ-af) · [العربية](Troubleshooting-FAQ-ar) · [עברית](Troubleshooting-FAQ-he) · [اردو](Troubleshooting-FAQ-ur) · [हिन्दी](Troubleshooting-FAQ-hi) · [বাংলা](Troubleshooting-FAQ-bn) · [ไทย](Troubleshooting-FAQ-th) · [Bahasa Indonesia](Troubleshooting-FAQ-id) · [Tagalog](Troubleshooting-FAQ-tl) · [日本語](Troubleshooting-FAQ-ja) · [한국어](Troubleshooting-FAQ-ko) · [中文](Troubleshooting-FAQ-zh) · [中文 (繁體)](Troubleshooting-FAQ-zh-tw)

# Problemas e perguntas frequentes

## Instalação e inicialização

### O SmartScreen do Windows diz "O Windows protegeu o seu PC"
O programa não está assinado com um certificado comercial. Clique em *Mais informações* → *Executar mesmo assim*. Baixe-o apenas da página [Releases](https://github.com/ic8tem/YA-MS/releases).

### macOS: não é possível abrir porque é de um desenvolvedor não identificado
O YA-MS não está assinado pela Apple, por isso o **Gatekeeper** o bloqueia na primeira vez. No `.dmg`, **clique direito em "Installa YA-MS.command" → Abrir** e confirme. O script remove de `~/YA-MS/YA-MS.app` a marca de quarentena "baixado da internet" e o abre. Se o macOS continuar recusando, abra *Configurações do Sistema → Privacidade e segurança* e clique em *Abrir mesmo assim*.

### macOS: qual .dmg?
`-mac-apple-silicon.dmg` para processadores M1/M2/M3/M4, `-mac-intel.dmg` para Macs Intel (menu Apple → *Sobre este Mac* indica qual você tem).

### Linux: o YA-MS não aparece no menu de aplicações
Execute `./installa.sh` a partir da pasta extraída (não a partir de `~/YA-MS`). Alguns ambientes de desktop exigem encerrar e reiniciar a sessão para mostrar as entradas novas. Você sempre pode iniciá-lo com `~/YA-MS/YA-MS`.

### Falta o mapa da Europa
*Mapa da Europa não disponível (é necessária a rede na primeira inicialização).* O mapa do Natural Earth é baixado para `data/mappa` na primeira inicialização. Conecte-se à internet e reinicie o YA-MS.

## Visualização

### Linux: o texto japonês aparece como quadradinhos
Faltam fontes CJK (chinês, japonês, coreano) no sistema. Instale as fontes **Noto CJK** e reinicie o YA-MS. O mesmo acontece com o árabe, o hebraico, o urdu, o hindi e o bengali: no Debian, Ubuntu e Raspberry Pi OS instale também `fonts-noto-core`.

| Distribuição | Comando |
|---|---|
| Debian, Ubuntu, Mint | `sudo apt install fonts-noto-cjk` |
| Fedora | `sudo dnf install google-noto-sans-cjk-fonts` |
| Arch | `sudo pacman -S noto-fonts-cjk` |
| openSUSE | `sudo zypper install noto-sans-cjk-fonts` |

### O texto é pequeno demais, ou os gráficos não têm espaço
Use o controle **Fonte** (100–300 %) e oculte as linhas com **Comandos**. Veja [Configurações](Settings-and-Data-Folder-pt-br#fonte-e-comandos).

### A tela é clara demais à noite
Escolha **Noite** ou **Preto** na lista **Tema**.

## Internet e dados de radar

### Mensagem "Sem conexão com a Internet"
O YA-MS a mostra **uma única vez** quando nenhuma fonte é alcançável; a barra de status fica vermelha. O programa continua funcionando com os **últimos dados salvos** e tenta novamente sozinho a cada 5 minutos; quando a rede volta aparece *Conexão restabelecida.* Não é preciso fazer nada.

### Aviso laranja em Fluxo radar: "Não consigo ler a escala vertical do fluxo …"
O radar de Collm muda a escala vertical todos os dias e o YA-MS a lê nas etiquetas do gráfico. Se uma etiqueta não puder ser lida, o programa usa a escala calibrada de 0–1200 meteoros/hora e avisa que há **valores a verificar**. Normalmente o gráfico horário seguinte é lido corretamente. Se durante muitas horas você vir *Formato do gráfico alterado* ou *Eixos do fluxo não encontrados na posição esperada*, o radar mudou o formato do gráfico: por favor, [informe](Contributing-and-Contacts-pt-br).

### "A escala do gráfico das altitudes mudou"
As estatísticas das altitudes (moda, média, mediana) continuam válidas; só as contagens absolutas do histograma das altitudes deixam de ser.

### "Fluxo radar: sem dados"
Clique em **Baixar agora** em [Fluxo radar](Radar-Flux-pt-br) e verifique se `data/fonti_radar.csv` tem `attivo=1` para Collm.

### RMOB: por que o download automático está desativado?
O RMOB pede que **os programas automáticos não baixem os seus arquivos**. Ative a *obtenção automática a cada 5 minutos* só depois que o RMOB lhe der autorização. Enquanto isso, use **Baixar RMOB agora** ou **Carregar arquivo RMOB do disco...**. Veja [Previsões experimentais](Experimental-Forecasts-pt-br#rmob-e-os-programas-automáticos).

### RMOB: "Formato do arquivo não reconhecido" ou poucas horas lidas
Use o arquivo de texto mensal do observador (`NAME_MMYYYYrmob.TXT`) ou uma tabela de boletim com um único observador. O ajuste do expoente precisa de pelo menos 3 horas em comum com os dados de Collm (ontem e hoje).

## Cálculos

### "Locator da estação inválido" / "Locator do correspondente inválido"
Os locators devem ter 4, 6 ou 8 caracteres (p. ex. `JN70`, `JN70CN`, `JN70CN12`).

### "Nenhuma zona comum da camada E"
O percurso é mais longo do que o dobro do alcance à altitude dos rastros (cerca de 2 × 1062 km com o lóbulo a 0° e rastros a 89,5 km): um único salto de meteor scatter não consegue cobri-lo. Aumentar a **Elevação do lóbulo** encurta ainda mais o alcance.

### Hot A / Hot B aparecem em cinza
Já estão **dentro do lóbulo da sua antena** quando ela aponta para o DX: não é preciso girá-la. Veja [Abóbada celeste](Sky-View-pt-br#avisos).

### A eficiência é diferente da do MCG_MS ou do MS-Soft
O YA-MS usa o percurso real e o seu próprio modelo; a escala de OH5IY e do MCG_MS não está documentada em detalhes. Compare horas e tendências em vez de porcentagens absolutas, e veja o [modelo](Efficiency-Calculation-pt-br#o-modelo).

### A passagem do feixe do GRAVES parece defasada
A sequência do feixe é calculada a partir do relógio do PC: sincronize-o com um servidor NTP. Além disso, a estação de comando do GRAVES às vezes desloca a sequência alguns passos; o detalhe é uma previsão a ser confirmada na escuta.

## Outras perguntas

**O YA-MS é gratuito?** Sim, é um programa gratuito para radioamadores.

**Ele controla o meu rotor ou o meu rádio?** Não. O YA-MS é uma ferramenta de previsão e planejamento; para o QSO use o seu programa de modos digitais (p. ex. MSHV, WSJT-X).

**Funciona acima dos 432 MHz?** A lista de bandas termina nos 432 MHz (28, 50, 70, 144, 222, 432). A previsão experimental aceita qualquer frequência de 28 a 1300 MHz, mas as regras de SM6FHZ que usa vêm da experiência nos 144 e 432 MHz.

**Algo deu errado.** Escreva ao autor indicando o seu sistema operacional, a versão do YA-MS e o que você fez: veja [Contribuir e contatos](Contributing-and-Contacts-pt-br).
