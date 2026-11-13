#!/usr/bin/env python3
"""Turn the static .dc.html pages into plain HTML you can open in a browser.

  python3 tools/build_static.py

Reads project/*.dc.html, writes site/<Name>.html.
- /_blob/<id> image URLs -> ../assets/<id>.<ext>
- <x-dc> / support.js wrapper removed, <helmet> moved into <head>
- links X.dc.html -> X.html
Pages with simple <sc-if> toggles are built in their default state (clicks do nothing).
Pages with other dynamic bindings ({{ }}, <sc-for>, <dc-import>) need the Design
runtime (reference/dc-runtime.js) and are skipped; they are listed at the end.
"""
import glob, os, re, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
assets = {os.path.splitext(f)[0]: f for f in os.listdir(os.path.join(root, 'assets'))}
out_dir = os.path.join(root, 'site'); os.makedirs(out_dir, exist_ok=True)
built, skipped = [], []
for path in sorted(glob.glob(os.path.join(root, 'project', '*.dc.html'))):
    name = os.path.basename(path)[:-len('.dc.html')]
    s = open(path, encoding='utf-8').read()
    # default-state snapshot: <sc-if> keeps its content only when its hint value is true; event holes dropped
    s = re.sub(r'<sc-if value="\{\{[^}]*\}\}"[^>]*hint-placeholder-val="\{\{\s*(true|false)\s*\}\}"[^>]*>(.*?)</sc-if>',
               lambda m: m.group(2) if m.group(1) == 'true' else '', s, flags=re.S)
    s = re.sub(r'\s(?:onClick|onChange|onInput|onKeyDown|onSubmit)="\{\{[^}]*\}\}"', '', s)
    if re.search(r'\{\{|<sc-|<dc-import', s):
        skipped.append(name); continue
    h0, h1 = s.index('<helmet>'), s.index('</helmet>')
    helmet = s[h0 + 8:h1]
    body = s[h1 + 9:]; body = body[:body.index('</x-dc>')]
    title = re.search(r'<title>.*?</title>', s, re.S)
    title = title.group(0) if title else '<title>%s</title>' % name
    html = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n%s\n%s\n</head>\n<body>\n%s\n</body>\n</html>\n'
            % (title, helmet, body))
    html = re.sub(r'/_blob/([0-9a-f]{32})', lambda m: '../assets/' + assets.get(m.group(1), m.group(1)), html)
    html = re.sub(r'href="([A-Za-z0-9_-]+)\.dc\.html', r'href="\1.html', html)
    open(os.path.join(out_dir, name + '.html'), 'w', encoding='utf-8').write(html)
    built.append(name)
print('built %d pages into site/' % len(built))
print('skipped (dynamic, need the runtime): ' + ', '.join(skipped))
