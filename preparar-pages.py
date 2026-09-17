from pathlib import Path
from urllib.parse import urlparse
import os, re, shutil, sys
if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(encoding="utf-8")

# A URL vem do GitHub Pages; também aceita URL e pasta de saída como argumentos.
url = (sys.argv[1] if len(sys.argv) > 1 else os.environ.get('PAGES_URL', '')).rstrip('/')
parsed = urlparse(url)
if parsed.scheme not in ('http', 'https') or not parsed.netloc:
    raise SystemExit('Informe uma URL completa: python preparar-pages.py https://usuario.github.io/repositorio')
base = parsed.path.rstrip('/')
source = Path(__file__).resolve().parent
out = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else source / '_site'
if out == source or source in out.parents and out.name != '_site':
    raise SystemExit('Use uma pasta de saída separada, ou _site.')
out.mkdir(parents=True, exist_ok=False)
origins = ['https://jaguaruna-321-modular.espa-o-de-tr-3944.chatgpt.site', 'https://jaguaruna.321modular.com.br']
allowed = {'assets', 'videos', 'chales', 'catalogo', 'politica-de-privacidade', 'chunks', 'index.html', '404.html', 'app.js', 'app.js.LEGAL.txt', 'styles.css', 'sitemap.xml', 'robots.txt', 'llms.txt', '.nojekyll', 'CNAME'}
for entry in source.iterdir():
    if entry.name not in allowed and not re.fullmatch(r'google[a-zA-Z0-9]+\.html', entry.name):
        continue
    if entry.is_dir(): shutil.copytree(entry, out / entry.name)
    else: shutil.copy2(entry, out / entry.name)
for p in out.rglob('*'):
    if not p.is_file() or p.suffix not in ('.html', '.css', '.xml', '.txt'):
        continue
    text = p.read_text(encoding='utf-8')
    if p.suffix == '.html':
        # Links, imagens, vídeos, miniaturas, srcset e JSON das galerias.
        text = re.sub(r'((?:href|src|poster|data-image|data-src)=")(/(?!/)[^"]*)', lambda m: m[1] + base + m[2], text)
        text = re.sub(r'(srcset=")([^"]+)', lambda m: m[1] + re.sub(r'(^|,\s*)(/)', lambda n: n[1] + base + n[2], m[2]), text)
        text = text.replace('&quot;/assets/', '&quot;' + base + '/assets/')
    if p.suffix == '.css':
        text = re.sub(r"(url\(['\"]?)(/(?!/))", lambda m: m[1] + base + m[2], text)
    for origin in origins:
        text = text.replace(origin, url)
    p.write_text(text, encoding='utf-8')
print('Site preparado em', out, 'para', url)
