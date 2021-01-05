# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Oofem(CMakePackage):
    """OOFEM is free finite element code with object oriented architecture for
    solving mechanical, transport and fluid mechanics problems that operates on
    various platforms.

    The aim of this project is to develop efficient and robust tool for FEM
    computations as well as to provide modular and extensible environment for
    future development.
    """

    homepage = "http://www.oofem.org/en/oofem"
    url      = "https://www.oofem.org/cgi-bin/OOFEM/download.cgi?download=oofem-2.5.zip"

    maintainers = ['alephpiece']

    executables = ['oofem']

    version('2.5', sha256='0cc116ad5d526baacffd882dc7800b54e5be84816e2229014d07697ad7d1b363')
    version('2.4', sha256='27841a9c4e56e4d145285a16296d6c3de0a7ed1633d227a8d2e1ef9326eda9d9')

    variant('build_type', default='RelWithDebInfo',
            description='The build type to for CMake',
            values=('Debug', 'Release', 'RelWithDebInfo', 'MinSizeRel', 'Coverage')
    )

    variant('mpi', default=True, description='Enable MPI support')
    variant('parmetis', default=False, description='Enable ParMETIS support')
    variant('petsc', default=False, description='Enable PETSc support')
    variant('slepc', default=False, description='Enable SLEPC support')

    depends_on('cmake', type='build')

    depends_on('mpi', when='+mpi')
    depends_on('metis', when='+parmetis')
    depends_on('parmetis', when='+parmetis')
    depends_on('petsc', when='+petsc')
    depends_on('slepc', when='+slepc')

    conflicts('+parmetis', when='~mpi')
    conflicts('+petsc', when='~mpi')
    conflicts('+slepc', when='~petsc')

    def cmake_args(self):
        spec = self.spec
        cmake_args = []

        cmake_args.append('-DUSE_PARALLEL:BOOL={}'.format(
            'ON' if spec.satisfies('+mpi') else 'OFF'))

        if spec.satisfies('+parmetis'):
            cmake_args.extend([
                '-DUSE_PARMETIS:BOOL=ON',
                '-DPARMETIS_DIR={}'.format(spec['parmetis'].prefix),
                '-DUSE_METIS:BOOL=ON',
                '-DMETIS_DIR={}'.format(spec['metis'].prefix)
            ])

        if spec.satisfies('+petsc'):
            cmake_args.extend([
                '-DUSE_PETSC:BOOL=ON',
                '-DMY_PETSC_DIR={}'.format(spec['petsc'].prefix)
            ])

        if spec.satisfies('+slepc'):
            cmake_args.extend([
                '-DUSE_SLEPC:BOOL=ON',
                '-DSLEPC_DIR={}'.format(spec['slepc'].prefix)
            ])

        return cmake_args

