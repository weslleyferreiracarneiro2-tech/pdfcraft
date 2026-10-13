"""Gera a página de download do Editor de PDF USINANDO (www.usinando.com.br/leitorpdf/).

Uso: python gerar.py INSTALADOR.exe VERSAO PASTA_SAIDA
Escreve na PASTA_SAIDA: index.html, logo-usinando.png, .htaccess e uma cópia do instalador.
A página não tem script (a CSP do site só aceita script do próprio domínio) e usa só CSS inline.
"""
import hashlib
import html
import pathlib
import shutil
import sys

instalador, versao, saida = pathlib.Path(sys.argv[1]), sys.argv[2], pathlib.Path(sys.argv[3])
aqui = pathlib.Path(__file__).resolve().parent
saida.mkdir(parents=True, exist_ok=True)

dados = instalador.read_bytes()
sha = hashlib.sha256(dados).hexdigest()
mb = f"{len(dados) / 1024 / 1024:.0f}".replace(".", ",")
nome_exe = "Instalar-Editor-PDF-USINANDO.exe"

pagina = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Editor de PDF USINANDO — download</title>
<style>
  :root {{ --azul: #1565c0; --azul-escuro: #0d47a1; --texto: #1d2733; --suave: #5b6b7d; --fundo: #f3f6fa; --cartao: #fff; --borda: #d9e2ec; }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; background: var(--fundo); color: var(--texto); font: 16px/1.55 "Segoe UI", system-ui, -apple-system, Roboto, Arial, sans-serif; }}
  main {{ max-width: 760px; margin: 0 auto; padding: 32px 16px 48px; }}
  .logo {{ display: block; height: 52px; width: auto; margin-bottom: 22px; }}
  h1 {{ font-size: 30px; line-height: 1.2; margin: 0 0 8px; }}
  .sub {{ color: var(--suave); margin: 0 0 26px; font-size: 17px; }}
  .cartao {{ background: var(--cartao); border: 1px solid var(--borda); border-radius: 14px; padding: 22px; margin-bottom: 18px; }}
  .baixar {{ display: inline-block; background: var(--azul); color: #fff; text-decoration: none; font-weight: 600; font-size: 19px; padding: 16px 28px; border-radius: 10px; }}
  .baixar:hover, .baixar:focus {{ background: var(--azul-escuro); }}
  .info {{ color: var(--suave); font-size: 14px; margin: 12px 0 0; }}
  h2 {{ font-size: 19px; margin: 0 0 12px; }}
  ol {{ margin: 0; padding-left: 22px; }}
  li {{ margin: 6px 0; }}
  b {{ font-weight: 600; }}
  .aviso {{ border-left: 4px solid var(--azul); background: #eaf2fc; padding: 12px 14px; border-radius: 6px; margin-top: 14px; font-size: 15px; }}
  .sha {{ font-family: Consolas, "Courier New", monospace; font-size: 12px; word-break: break-all; color: var(--suave); }}
  footer {{ color: var(--suave); font-size: 13px; margin-top: 26px; }}
  .autor {{ margin-top: 18px; padding-top: 14px; border-top: 1px solid var(--borda); text-align: center; font-size: 14px; color: var(--texto); }}
</style>
</head>
<body>
<main>
  <img class="logo" src="logo-usinando.png" alt="USINANDO" width="235" height="52">
  <h1>Editor de PDF USINANDO</h1>
  <p class="sub">Leitor e editor de PDF da empresa, com a função de <b>imprimir só um pedaço da página</b>.</p>

  <section class="cartao">
    <a class="baixar" href="{nome_exe}" download>Baixar o instalador</a>
    <p class="info">Versão {html.escape(versao)} · {mb} MB · Windows 10 e 11 (64 bits)</p>
  </section>

  <section class="cartao">
    <h2>Como instalar</h2>
    <ol>
      <li>Clique em <b>Baixar o instalador</b> e abra o arquivo baixado.</li>
      <li>Se aparecer o aviso azul <b>"O Windows protegeu o computador"</b>, clique em <b>Mais informações</b> e depois em <b>Executar assim mesmo</b>. Ele aparece porque o programa não tem assinatura digital.</li>
      <li>Confirme a senha de administrador, se o Windows pedir, e vá clicando em <b>Avançar</b> até <b>Concluir</b>.</li>
      <li>Pronto: o atalho <b>Editor de PDF USINANDO</b> fica na Área de Trabalho e no Iniciar.</li>
    </ol>
    <p class="aviso">Pra atualizar, é só baixar e rodar o instalador de novo, por cima. Não use "Verificar atualizações" dentro do programa: a versão oficial do PdfCraft não tem a função de imprimir o pedaço.</p>
  </section>

  <section class="cartao">
    <h2>Como imprimir só um pedaço da página</h2>
    <ol>
      <li>Abra o PDF e vá em <b>Editar &gt; Capturar instantâneo</b>.</li>
      <li>Arraste o mouse em volta do pedaço. Ele fica marcado em azul.</li>
      <li>Clique com o <b>botão direito</b> em cima do pedaço marcado e escolha <b>Imprimir área selecionada…</b></li>
      <li>Escolha a impressora e clique em <b>Imprimir</b>. "Ajustar" aumenta o pedaço pra folha; "Tamanho real" imprime na escala do desenho.</li>
    </ol>
  </section>

  <footer>
    <p>Baseado no PdfCraft, da equipe ArtCraft (software livre, licenças MIT ou Apache-2.0). Versão modificada pela USINANDO; não é um produto oficial da ArtCraft.</p>
    <p class="sha">SHA-256 do instalador: {sha}</p>
    <p class="autor">Designed by Weslley Ferreira</p>
  </footer>
</main>
</body>
</html>
"""
(saida / "index.html").write_bytes(pagina.encode("utf-8"))
shutil.copyfile(aqui.parent / "logo-usinando.png", saida / "logo-usinando.png")
shutil.copyfile(instalador, saida / nome_exe)
(saida / ".htaccess").write_bytes(
    b"# Download do Editor de PDF USINANDO: fora dos buscadores, pagina sem cache, .exe baixa direto.\n"
    b"Options -Indexes\n"
    b"DirectoryIndex index.html\n"
    b"<IfModule mod_headers.c>\n"
    b"    Header always set X-Robots-Tag \"noindex, nofollow\"\n"
    b"    <Files \"index.html\">\n"
    b"        Header set Cache-Control \"no-cache\"\n"
    b"    </Files>\n"
    b"    <FilesMatch \"\\.exe$\">\n"
    b"        Header set Content-Disposition \"attachment\"\n"
    b"        Header set Cache-Control \"no-cache\"\n"
    b"    </FilesMatch>\n"
    b"</IfModule>\n"
    b"<FilesMatch \"\\.exe$\">\n"
    b"    ForceType application/octet-stream\n"
    b"</FilesMatch>\n"
)
print(f"ok: {saida} (sha256 {sha}, {mb} MB)")
