# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Gompi(BundlePackage):
    """GNU Compiler Collection (GCC) based compiler toolchain,
    including OpenMPI for MPI support.
    """

    homepage = "https://hpcde.github.io/cluster-docs/"

    version('2020b')

    depends_on('autoconf', type=('build', 'run'))
    depends_on('automake', type=('build', 'run'))
    depends_on('cmake', type=('build', 'run'))
    depends_on('git', type=('build', 'run'))
    depends_on('gcc@10.2.0', type=('build', 'link', 'run'))
    depends_on('openmpi@4.0.5%gcc@10.2.0', type=('build', 'link', 'run'))

