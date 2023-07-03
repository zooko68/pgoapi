#!/usr/bin/env python

import os
from setuptools import setup, find_packages

try:  # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements

setup_dir = os.path.dirname(os.path.realpath(__file__))
path_req = os.path.join(setup_dir, 'requirements.txt')
install_reqs = parse_requirements(path_req, session=False)

reqs = [str(ir.req) for ir in install_reqs]

setup(name='pgoapi',
      author = 'tjado',
      description = 'Pokemon Go API lib',
      version = '1.2.0',
      url = 'https://github.com/pogodevorg/pgoapi',
      download_url = "https://github.com/pogodevorg/pgoapi/releases",
      packages = find_packages(),
      install_requires = reqs
      )
