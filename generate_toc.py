#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from glob import glob
from os.path import relpath


def generate_toc(f_out: str):
    files_py = glob('./Python/**/*.py', recursive=True)
    match_str = r'^# (.+)\n^# (http.+)$'

    toc = []

    # TODO: write kyu levels
    for soln in files_py:
        with open(soln, 'r') as f:
            matched = re.search(match_str, f.read(), re.MULTILINE)

        if matched:
            entry = f'[{matched[1]}]({matched[2]})'
        else:
            fname = re.match(r'[^\\]+\/(.+)\.py$', soln)[1]
            entry = fname.replace('_', ' ').capitalize()

        toc.append('- ' + entry + '\n\t- [Solution](./' + relpath(soln) + ')\n')

    with open(f_out, 'w') as out:
        out.writelines(toc)
        print('Done.')


generate_toc('./toc.md')
