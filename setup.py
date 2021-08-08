# DO NOT EDIT!!! built with `python _building/build_setup.py`
import setuptools
setuptools.setup(
    name="k3net",
    packages=["k3net"],
    version="0.1.0",
    license='MIT',
    description='Utility functions for network related operation.',
    long_description='# k3net\n\n[![Action-CI](https://github.com/pykit3/k3net/actions/workflows/python-package.yml/badge.svg)](https://github.com/pykit3/k3net/actions/workflows/python-package.yml)\n[![Build Status](https://travis-ci.com/pykit3/k3net.svg?branch=master)](https://travis-ci.com/pykit3/k3net)\n[![Documentation Status](https://readthedocs.org/projects/k3net/badge/?version=stable)](https://k3net.readthedocs.io/en/stable/?badge=stable)\n[![Package](https://img.shields.io/pypi/pyversions/k3net)](https://pypi.org/project/k3net)\n\nUtility functions for network related operation.\n\nk3net is a component of [pykit3] project: a python3 toolkit set.\n\n\nUtility functions for network related operation.\n\n\n\n# Install\n\n```\npip install k3net\n```\n\n#   Author\n\nZhang Yanpo (张炎泼) <drdr.xp@gmail.com>\n\n#   Copyright and License\n\nThe MIT License (MIT)\n\nCopyright (c) 2015 Zhang Yanpo (张炎泼) <drdr.xp@gmail.com>\n\n\n[pykit3]: https://github.com/pykit3',
    long_description_content_type="text/markdown",
    author='Zhang Yanpo',
    author_email='drdr.xp@gmail.com',
    url='https://github.com/pykit3/k3net',
    keywords=['python', 'net'],
    python_requires='>=3.0',

    install_requires=['k3ut<0.2,>=0.1.15', 'netifaces~=0.11.0', 'PyYAML>=5.0.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
    ] + ['Programming Language :: Python :: 3.6', 'Programming Language :: Python :: 3.7', 'Programming Language :: Python :: 3.8', 'Programming Language :: Python :: Implementation :: PyPy'],
)
