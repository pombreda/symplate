"""Symplate example to render a simple blog homepage."""

import collections
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import symplate

BlogEntry = collections.namedtuple('BlogEntry', 'title url html_body')

renderer = symplate.Renderer(
        os.path.join(os.path.dirname(__file__), 'symplates'),
        output_dir=os.path.join(os.path.dirname(__file__), 'symplouts'),
        check_mtimes=True)

def main():
    entries = [
        BlogEntry('Sorry', '/sorry/', '<p>Sorry for the lack of updates.</p>'),
        BlogEntry('My life story', '/my-life-story/', '<p>Once upon a time...</p>'),
        BlogEntry(u'First \u201cpost\u201d', '/first-post/', '<p>This is the first post.</p>'),
    ]
    output = renderer.render('blog', entries, title="Ben's Blog")
    sys.stdout.write(output.encode('utf-8'))

if __name__ == '__main__':
    main()
