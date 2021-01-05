# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyBoutdata(PythonPackage):
    """pip-package of what is found in BOUT-dev/tools/pylib/boutdata.
    Note that BOUT-dev/tools/pylib/boutdata will likely be replaced by this repo in BOUT++ v4.3.0.

    This package will likely be superseded by xBOUT in the near future
    """

    homepage = "https://pypi.org/project/boutdata/"
    url      = "https://pypi.io/packages/source/b/boutdata/boutdata-0.1.2.tar.gz"

    maintainers = ['alephpiece']

    version('0.1.2', sha256='8f0148f00c66c75f7bac6392af73e35676b65395e19496c2c10cd6f586097ac5')

    depends_on('python@3.6:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-boututils', type=('build', 'run'))

