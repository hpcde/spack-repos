# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyBoututils(PythonPackage):
    """pip-package of what was previously found in BOUT-dev/tools/pylib/boututils"""

    homepage = "https://pypi.org/project/boututils/#description"
    url      = "https://pypi.io/packages/source/b/boututils/boututils-0.1.4.tar.gz"

    maintainers = ['alephpiece']

    version('0.1.4', sha256='ed8e8778cea7f2335a22ddab8294f3983a82eca10c9d8357936a3102abef4563')

    depends_on('python@3.6:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')

    # use netlib-lapack as default blas/lapack for BOUT++
    depends_on('py-netcdf4', type=('build', 'run'))
    depends_on('py-h5py', type=('build', 'run'))

