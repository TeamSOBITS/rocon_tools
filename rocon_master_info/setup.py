#!/usr/bin/env python3

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['rocon_master_info'],
    package_dir={'': 'src'},
    scripts=['scripts/rocon_master_info',
             ],
)

setup(**d)
