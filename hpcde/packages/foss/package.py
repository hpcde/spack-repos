# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Foss(BundlePackage):
    """GNU Compiler Collection (GCC) based compiler toolchain,
    including OpenMPI for MPI support, BLAS/LAPACK,
    ScaLAPACK, FFTW, ParMETIS, and PETSc.
    """

    homepage = "https://hpcde.github.io/cluster-docs/"

    version('2020b')

    depends_on('gompi@2020b', type=('build', 'link', 'run'))
    depends_on('blas%gcc@10.2.0')
    depends_on('lapack%gcc@10.2.0')
    depends_on('scalapack%gcc@10.2.0')
    depends_on('fftw%gcc@10.2.0')
    depends_on('parmetis%gcc@10.2.0')
    depends_on('petsc%gcc@10.2.0')

