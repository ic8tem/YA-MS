[English](Troubleshooting-FAQ) · [Italiano](Troubleshooting-FAQ-it) · [Deutsch](Troubleshooting-FAQ-de) · [Nederlands](Troubleshooting-FAQ-nl) · [Français](Troubleshooting-FAQ-fr) · [Español](Troubleshooting-FAQ-es) · **Português** · [Português (Brasil)](Troubleshooting-FAQ-pt-br) · [Dansk](Troubleshooting-FAQ-da) · [Norsk](Troubleshooting-FAQ-nb) · [Svenska](Troubleshooting-FAQ-sv) · [Íslenska](Troubleshooting-FAQ-is) · [Eesti](Troubleshooting-FAQ-et) · [Lietuvių](Troubleshooting-FAQ-lt) · [Latviešu](Troubleshooting-FAQ-lv) · [Polski](Troubleshooting-FAQ-pl) · [Čeština](Troubleshooting-FAQ-cs) · [Magyar](Troubleshooting-FAQ-hu) · [Română](Troubleshooting-FAQ-ro) · [Ελληνικά](Troubleshooting-FAQ-el) · [Русский](Troubleshooting-FAQ-ru) · [Українська](Troubleshooting-FAQ-uk) · [Türkçe](Troubleshooting-FAQ-tr) · [Afrikaans](Troubleshooting-FAQ-af) · [العربية](Troubleshooting-FAQ-ar) · [עברית](Troubleshooting-FAQ-he) · [اردو](Troubleshooting-FAQ-ur) · [हिन्दी](Troubleshooting-FAQ-hi) · [বাংলা](Troubleshooting-FAQ-bn) · [ไทย](Troubleshooting-FAQ-th) · [Bahasa Indonesia](Troubleshooting-FAQ-id) · [Tagalog](Troubleshooting-FAQ-tl) · [日本語](Troubleshooting-FAQ-ja) · [한국어](Troubleshooting-FAQ-ko) · [中文](Troubleshooting-FAQ-zh) · [中文 (繁體)](Troubleshooting-FAQ-zh-tw)

# Problemas e perguntas frequentes

## Instalação e arranque

### O SmartScreen do Windows diz "O Windows protegeu o seu PC"
O programa não está assinado com um certificado comercial. Clique em *Mais informações* → *Executar mesmo assim*. Descarregue-o apenas da página [Releases](https://github.com/ic8tem/YA-MS/releases).

### macOS: não é possível abrir porque é de um programador não identificado
O YA-MS não está assinado pela Apple, por isso o **Gatekeeper** bloqueia-o na primeira vez. No `.dmg`, **clique direito em "Installa YA-MS.command" → Abrir** e confirme. O script retira de `~/YA-MS/YA-MS.app` a marca de quarentena "descarregado da internet" e abre-o. Se o macOS continuar a recusar, abra *Definições do Sistema → Privacidade e segurança* e prima *Abrir mesmo assim*.

### macOS: qual .dmg?
`-mac-apple-silicon.dmg` para processadores M1/M2/M3/M4, `-mac-intel.dmg` para Macs Intel (menu Apple → *Acerca deste Mac* indica qual tem).

### Linux: o YA-MS não aparece no menu de aplicações
Execute `./installa.sh` a partir da pasta extraída (não a partir de `~/YA-MS`). Alguns ambientes de trabalho precisam de terminar e reiniciar a sessão para mostrar as entradas novas. Pode sempre iniciá-lo com `~/YA-MS/YA-MS`.

### Falta o mapa da Europa
*Mapa da Europa não disponível (é necessária a rede no primeiro arranque).* O mapa do Natural Earth é descarregado para `data/mappa` no primeiro arranque. Ligue-se à internet e reinicie o YA-MS.

## Visualização

### Linux: o texto japonês aparece como quadradinhos
Faltam fontes CJK (chinês, japonês, coreano) no sistema. Instale as fontes **Noto CJK** e reinicie o YA-MS. O mesmo acontece com o árabe, o hebraico, o urdu, o hindi e o bengali: no Debian, Ubuntu e Raspberry Pi OS instale também `fonts-noto-core`.

| Distribuição | Comando |
|---|---|
| Debian, Ubuntu, Mint | `sudo apt install fonts-noto-cjk` |
| Fedora | `sudo dnf install google-noto-sans-cjk-fonts` |
| Arch | `sudo pacman -S noto-fonts-cjk` |
| openSUSE | `sudo zypper install noto-sans-cjk-fonts` |

### O texto é demasiado pequeno, ou os gráficos não têm espaço
Use o controlo **Tipo de letra** (85–140 %) e recolha as filas com **Comandos**. Ver [Definições](Settings-and-Data-Folder-pt#tipo-de-letra-e-comandos).

### O ecrã é demasiado luminoso à noite
Escolha **Noite** ou **Preto** na lista **Tema**.

## Internet e dados de radar

### Mensagem "Sem ligação à Internet"
O YA-MS mostra-a **uma única vez** quando nenhuma fonte é alcançável; a barra de estado fica vermelha. O programa continua a funcionar com os **últimos dados guardados** e volta a tentar sozinho a cada 5 minutos; quando a rede volta aparece *Ligação restabelecida.* Não é preciso fazer nada.

### Aviso laranja em Fluxo radar: "Não consigo ler a escala vertical do fluxo …"
O radar de Collm muda a escala vertical todos os dias e o YA-MS lê-a nas etiquetas do gráfico. Se uma etiqueta não puder ser lida, o programa usa a escala calibrada de 0–1200 meteoros/hora e avisa que há **valores a verificar**. Normalmente o gráfico horário seguinte é lido corretamente. Se durante muitas horas vir *Formato do gráfico alterado* ou *Eixos do fluxo não encontrados na posição esperada*, o radar mudou o formato do gráfico: por favor, [comunique-o](Contributing-and-Contacts-pt).

### "A escala do gráfico das altitudes mudou"
As estatísticas das altitudes (moda, média, mediana) continuam válidas; só as contagens absolutas do histograma das altitudes deixam de o ser.

### "Fluxo radar: sem dados"
Prima **Descarregar agora** em [Fluxo radar](Radar-Flux-pt) e verifique que `data/fonti_radar.csv` tem `attivo=1` para Collm.

### RMOB: porque está desativada a descarga automática?
O RMOB pede que **os programas automáticos não descarreguem os seus ficheiros**. Ative a *obtenção automática a cada 5 minutos* só depois de o RMOB lhe ter dado autorização. Entretanto use **Descarregar RMOB agora** ou **Carregar ficheiro RMOB do disco...**. Ver [Previsões experimentais](Experimental-Forecasts-pt#rmob-e-os-programas-automáticos).

### RMOB: "Formato do ficheiro não reconhecido" ou poucas horas lidas
Use o ficheiro de texto mensal do observador (`NAME_MMYYYYrmob.TXT`) ou uma tabela de boletim com um único observador. O ajuste do expoente precisa de pelo menos 3 horas em comum com os dados de Collm (ontem e hoje).

## Cálculos

### "Locator da estação inválido" / "Locator do correspondente inválido"
Os locators devem ter 4, 6 ou 8 caracteres (p. ex. `JN70`, `JN70CN`, `JN70CN12`).

### "Nenhuma zona comum da camada E"
O percurso é mais longo do que o dobro do alcance à altitude dos rastos (cerca de 2 × 1062 km com o lóbulo a 0° e rastos a 89,5 km): um único salto de meteor scatter não o consegue cobrir. Aumentar a **Elevação do lóbulo** encurta ainda mais o alcance.

### Hot A / Hot B aparecem a cinzento
Já estão **dentro do lóbulo da sua antena** quando aponta para o DX: não é preciso rodá-la. Ver [Abóbada celeste](Sky-View-pt#avisos).

### A eficiência é diferente da do MCG_MS ou do MS-Soft
O YA-MS usa o percurso real e o seu próprio modelo; a escala de OH5IY e do MCG_MS não está documentada em pormenor. Compare horas e tendências em vez de percentagens absolutas, e veja o [modelo](Efficiency-Calculation-pt#o-modelo).

### A passagem do feixe do GRAVES parece desfasada
A sequência do feixe é calculada a partir do relógio do PC: sincronize-o com um servidor NTP. Além disso, a estação de comando do GRAVES desloca por vezes a sequência alguns passos; o pormenor é uma previsão a confirmar à escuta.

## Outras perguntas

**O YA-MS é gratuito?** Sim, é um programa gratuito para radioamadores.

**Controla o meu rotor ou o meu rádio?** Não. O YA-MS é uma ferramenta de previsão e planeamento; para o QSO use o seu programa de modos digitais (p. ex. MSHV, WSJT-X).

**Funciona acima dos 432 MHz?** A lista de bandas termina nos 432 MHz (28, 50, 70, 144, 222, 432). A previsão experimental aceita qualquer frequência de 28 a 1300 MHz, mas as regras de SM6FHZ que usa vêm da experiência nos 144 e 432 MHz.

**Algo correu mal.** Escreva ao autor indicando o seu sistema operativo, a versão do YA-MS e o que fez: ver [Contribuir e contactos](Contributing-and-Contacts-pt).
