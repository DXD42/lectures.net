#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.

import os
import sys

sys.path.insert(0, os.path.abspath('../_lectures/docs/'))

from config_sphinx import *  # noqa isort:skip

project = u'Сетевое программирование'
html_title = project
epub_title = project

# Github
edit_on_github_project = 'ustu/lectures.net'
edit_on_github_branch = 'master'

latex_documents = [
    (
        'index',
        'lectures.tex',
        project,
        u'Свинцов Дмитрий',
        'manual'
    ),
]

exclude_patterns += [  # noqa
    'net/requests.rst',
]
