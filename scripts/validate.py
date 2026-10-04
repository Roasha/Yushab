"""Check static website references without third-party packages."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1] / 'docs'

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.ids = [], set()
    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if values.get('id'):
            self.ids.add(values['id'])
        for name in ('href', 'src', 'action'):
            if values.get(name):
                self.links.append(values[name])

pages = {}
for path in ROOT.rglob('*.html'):
    page = Page()
    page.feed(path.read_text(encoding='utf-8'))
    pages[path.resolve()] = page
errors = []
for path, page in pages.items():
    for link in page.links:
        url = urlsplit(link)
        if url.scheme or url.netloc:
            continue
        if url.path.startswith('/'):
            errors.append(f'{path.name}: root-relative path breaks project hosting: {link}')
            continue
        target = (path.parent / unquote(url.path)).resolve() if url.path else path
        if not target.exists():
            errors.append(f'{path.name}: missing target {link}')
        elif url.fragment and target in pages and url.fragment not in pages[target].ids:
            errors.append(f'{path.name}: missing anchor {link}')
if errors:
    raise SystemExit('\n'.join(errors))
assert (ROOT / 'index.html').is_file()
assert len(list((ROOT / 'product').glob('*.html'))) == 152
print(f'PASS: {len(pages)} HTML pages and all local links, images and form targets.')
