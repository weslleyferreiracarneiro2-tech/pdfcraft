; Instalador do Editor de PDF USINANDO (PdfCraft com "imprimir área selecionada").
; Compilado no GitHub pelo workflow usinando-windows.yml:
;   ISCC.exe /DAppVersion=0.7.1.N packaging\usinando\instalador.iss
; Os caminhos são relativos a esta pasta.

#define AppName "Editor de PDF USINANDO"
#define ExeName "EditorPDF-USINANDO.exe"
#define ProgId "USINANDO.EditorPDF"
#ifndef AppVersion
  #define AppVersion "0.0.0.0"
#endif

[Setup]
; Identificador fixo: uma versão nova instala por cima da anterior.
AppId={{03B090ED-3B78-4346-BA82-192658DCE46C}
AppName={#AppName}
AppVersion={#AppVersion}
AppVerName={#AppName} {#AppVersion}
AppPublisher=USINANDO Caldeiraria e Usinagem
AppComments=Leitor e editor de PDF baseado no PdfCraft (equipe ArtCraft), modificado pela USINANDO.
VersionInfoVersion={#AppVersion}
DefaultDirName={autopf}\{#AppName}
DisableProgramGroupPage=yes
DisableDirPage=auto
; Para todos os usuários do PC (pede senha de administrador); dá pra escolher "só pra mim".
PrivilegesRequired=admin
PrivilegesRequiredOverridesAllowed=dialog
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
OutputDir=..\..\dist
OutputBaseFilename=Instalar-Editor-PDF-USINANDO
SetupIconFile=..\..\assets\app-icon\pdfcraft.ico
UninstallDisplayIcon={app}\{#ExeName}
UninstallDisplayName={#AppName}
WizardStyle=modern
Compression=lzma2/max
SolidCompression=yes
CloseApplications=yes
ChangesAssociations=yes
InfoAfterFile=LEIA-ME.txt

[Languages]
Name: "ptbr"; MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"

[Tasks]
Name: "atalho"; Description: "Criar atalho na Área de Trabalho"

[Files]
Source: "..\..\target\release\pdfcraft.exe"; DestDir: "{app}"; DestName: "{#ExeName}"; Flags: ignoreversion
Source: "LEIA-ME.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\LICENSE-MIT"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\LICENSE-APACHE"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\NOTICE"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\ATTRIBUTION.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\assets\app-icon\LICENSE-document.txt"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{autoprograms}\{#AppName}"; Filename: "{app}\{#ExeName}"
Name: "{autodesktop}\{#AppName}"; Filename: "{app}\{#ExeName}"; Tasks: atalho

[Registry]
; Aparece em "Abrir com" para PDF e na lista de Aplicativos padrão do Windows.
Root: HKA; Subkey: "Software\Classes\{#ProgId}"; ValueType: string; ValueData: "Documento PDF"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\{#ProgId}\DefaultIcon"; ValueType: string; ValueData: "{app}\{#ExeName},-2"
Root: HKA; Subkey: "Software\Classes\{#ProgId}\shell\open\command"; ValueType: string; ValueData: """{app}\{#ExeName}"" ""%1"""
Root: HKA; Subkey: "Software\Classes\.pdf\OpenWithProgids"; ValueType: string; ValueName: "{#ProgId}"; ValueData: ""; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\Applications\{#ExeName}"; ValueType: string; ValueName: "FriendlyAppName"; ValueData: "{#AppName}"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\Applications\{#ExeName}\SupportedTypes"; ValueType: string; ValueName: ".pdf"; ValueData: ""
Root: HKA; Subkey: "Software\USINANDO\EditorPDF\Capabilities"; ValueType: string; ValueName: "ApplicationName"; ValueData: "{#AppName}"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\USINANDO\EditorPDF\Capabilities"; ValueType: string; ValueName: "ApplicationDescription"; ValueData: "Leitor e editor de PDF da USINANDO"
Root: HKA; Subkey: "Software\USINANDO\EditorPDF\Capabilities\FileAssociations"; ValueType: string; ValueName: ".pdf"; ValueData: "{#ProgId}"
Root: HKA; Subkey: "Software\RegisteredApplications"; ValueType: string; ValueName: "{#AppName}"; ValueData: "Software\USINANDO\EditorPDF\Capabilities"; Flags: uninsdeletevalue

[Run]
Filename: "{app}\{#ExeName}"; Description: "Abrir o {#AppName} agora"; Flags: nowait postinstall skipifsilent
Filename: "ms-settings:defaultapps"; Description: "Escolher o {#AppName} como programa padrão de PDF (abre as Configurações do Windows)"; Flags: shellexec nowait postinstall skipifsilent unchecked
