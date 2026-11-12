; YA-MS - installatore per Windows (Inno Setup 6)
; Installa nella cartella personale C:\YA-MS (programma e cartella data insieme), senza permessi di amministratore.
#ifndef AppVersion
  #define AppVersion "1.0.0"
#endif
#ifndef Arch
  #define Arch "x64"
#endif
#ifndef SourceDir
  #define SourceDir "..\publish\win-x64"
#endif

[Setup]
AppId={{7B1C2E55-9A3F-4C2B-9E4D-6A1F0C3B8D21}
AppName=YA-MS
AppVersion={#AppVersion}
AppVerName=YA-MS {#AppVersion}
AppPublisher=Costantino Cerrotta IC8TEM
AppComments=Previsione e calcolo in diretta dell'efficienza degli sciami meteorici per il meteor scatter
DefaultDirName={sd}\YA-MS
DisableProgramGroupPage=yes
PrivilegesRequired=lowest
#if Arch == "x64"
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
#endif
#if Arch == "arm64"
ArchitecturesAllowed=arm64
ArchitecturesInstallIn64BitMode=arm64
#endif
OutputDir=..\dist
OutputBaseFilename=YA-MS-{#AppVersion}-windows-{#Arch}-setup
SetupIconFile=..\src\Assets\ya-ms.ico
UninstallDisplayIcon={app}\YA-MS.exe
Compression=lzma2
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "italian"; MessagesFile: "compiler:Languages\Italian.isl"

[Tasks]
Name: "desktopicon"; Description: "Crea un'icona sul desktop"; GroupDescription: "Icone:"

[Files]
; programma
Source: "{#SourceDir}\*"; DestDir: "{app}"; Excludes: "data\*,doc\*"; Flags: ignoreversion recursesubdirs createallsubdirs
; dati di riferimento (catalogo, massimi IMO, fonti, documenti): aggiornati a ogni installazione
Source: "{#SourceDir}\data\*"; DestDir: "{app}\data"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "{#SourceDir}\doc\*"; DestDir: "{app}\doc"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{userprograms}\YA-MS"; Filename: "{app}\YA-MS.exe"
Name: "{userdesktop}\YA-MS"; Filename: "{app}\YA-MS.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\YA-MS.exe"; Description: "Avvia YA-MS"; Flags: nowait postinstall skipifsilent
