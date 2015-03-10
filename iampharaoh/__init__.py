# Copyright (c) 2014 Idival, Mario <marioidival@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os
import binascii
from textwrap import dedent

from pyramid.compat import native_
from pyramid.scaffolds.template import Template


class PharaohTemplate(Template):

    def pre(self, command, output_dir, vars):
        """ Overrides `pre` method to verify if package name is not equals of
        anything package.
        """
        package_name = os.path.abspath('.').split('/')[-1]
        blacklist_names = ('site', package_name)

        if vars['package'] in blacklist_names:
            msg = """
            Sorry, you may not name your "{0}". This name "{0}" has been
            defined. Please name it anything except "{0}".
            """.format(vars['package'])
            raise ValueError(msg)

        vars['random_string'] = native_(binascii.hexlify(os.urandom(20)))
        vars['root_project'] = package_name
        package_logger = vars['package']
        if package_logger == 'root':
            # Rename the app logger in the rare case a project is named 'root'
            package_logger = 'app'
        vars['package_logger'] = package_logger
        return Template.pre(self, command, output_dir, vars)

    def post(self, command, output_dir, vars): # pragma: no cover
        """ Overrides :meth:`pyramid.scaffolds.template.Template.post`, to
        print "Welcome to Pyramid.  Sorry for the convenience." after a
        successful scaffolding rendering."""

        separator = "X" * 79
        msg = dedent("""
        %(separator)s
        Tutorials: http://docs.pylonsproject.org/projects/pyramid_tutorials
        Documentation: http://docs.pylonsproject.org/projects/pyramid
        Twitter (tips & updates): http://twitter.com/pylons
        Mailing List: http://groups.google.com/group/pylons-discuss

        Creator of this scaffold: Mario Idival
        Twitter/Github: @marioidival

        Welcome to Pyramid.  Sorry for the convenience.
        %(separator)s
        """ % {'separator': separator})

        self.out(msg)
        return Template.post(self, command, output_dir, vars)

    def out(self, msg): # pragma: no cover (replaceable testing hook)
        print(msg)


class AppsTemplate(PharaohTemplate):
    _template_dir = 'app'
    summary = "Create an 'app' in project. - Like startapp Django"


class ProjectTemplate(PharaohTemplate):
    _template_dir = 'project'
    summary = "Scaffold created for Django users initiate with Pyramid more\
        comfortably"
