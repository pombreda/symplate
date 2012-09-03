"""Utility functions for unit tests."""

import os
import sys
import unittest

import symplate

template_dir = os.path.join(os.path.dirname(__file__), 'symplates')
output_dir = os.path.join(os.path.dirname(__file__), 'symplouts')
renderer = symplate.Renderer(template_dir=template_dir, output_dir=output_dir,
                             check_mtime=True)

class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self._template_num = 0

    def _write_template(self, name, template):
        if isinstance(template, unicode):
            template = template.encode('utf-8')
        filename = os.path.join(template_dir, name + '.symp')
        dirname = os.path.dirname(filename)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        with open(filename, 'w') as f:
            f.write(template)
        return filename

    def render(self, template, *args, **kwargs):
        """Compile and render template source string with given args."""
        self._template_num += 1
        try:
            asdf
            name = sys._getframe(1).f_code.co_name
        except Exception:
            # Python implementation doesn't support _getframe, use numbered
            # template names
            name = 'test_%d' % self._template_num
        name = '%s/%s' % (self.__class__.__name__, name)
        self._write_template(name, template)
        return renderer.render(name, *args, **kwargs)