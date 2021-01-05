# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class BoutDev(AutotoolsPackage):
    """BOUT++ is a framework for writing fluid and plasma simulations in curvilinear geometry.
    It is intended to be quite modular, with a variety of numerical methods and time-integration
    solvers available. BOUT++ is primarily designed and tested with reduced plasma fluid models
    in mind, but it can evolve any number of equations, with equations appearing in a readable form.
    """

    homepage = "http://boutproject.github.io/"
    url      = "https://github.com/boutproject/BOUT-dev/releases/download/v4.3.2/BOUT++-v4.3.2.tar.gz"

    # notify when the package is updated.
    maintainers = ['alephpiece']

    version('4.3.2', sha256='ee10aa9ce90fdec4d3ac0cc11bfdedadcbda19b3d0a74851f94633ddc80c5751')
    version('4.3.1', sha256='7763fb4be96dd89551a0bb3a9b435dc09ebac4ef26d80b5edaa0f7c013d1b558')
    version('4.3.0', sha256='db50a66a62edf87f04b8cb6637838811bb9307726e748a9c1979fb1cbf250cd9')


    variant('shared', default=False, description='Enable building bout++ into an shared object')
    variant('checks', default='0', description='Set run-time checking level',
            values=('0', '1', '2', '3'), multi=False)
    variant('optimize', default='2', description='Enable optimization',
            values=('0', '1', '2', '3', '4'), multi=False)
    variant('track', default=False, description='Enable variable tracking')
    variant('debug', default=False, description='Enable all debugging flags')
    variant('nls', default=True, description='Enable Native Language support')
    variant('openmp', default=False, description='Enable building with OpenMP support')
    variant('pvode-openmp', default=False, description='Enable building PVODE with OpenMP support')
    variant(
        'openmp-schedule', default='static', description='Set OpenMP schedule',
        values=('static', 'dynamic', 'guided', 'auto'), multi=False
    )
    variant('sundials', default=False, description='Use SUNDIALS CVODE, IDA, and ARKODE solvers')
    variant('blaslapack', default=False, description='Use BLAS and LAPACK')
    variant('petsc', default=False, description='Use PETSc interface')
    variant('slepc', default=False, description='Use SLEPc interface')
    variant('mumps', default=False, description='Use MUMPS library for direct matrix inversions')
    variant('scorep', default=False, description='Enable support for scorep based instrumentation')

    # Mandatory dependencies
    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('mpi@3:', type=('build', 'link', 'run'))
    depends_on('fftw@3:')

    # Optional dependencies
    depends_on('hdf5 +mpi')
    depends_on('netcdf-c +mpi')
    depends_on('netcdf-cxx4')
    depends_on('sundials +CVODE+IDA+ARKODE', when='+sundials')
    depends_on('netlib-lapack~external-blas', when='+blaslapack')
    depends_on('petsc@3.4.0:', when='+petsc')
    depends_on('slepc@3.4.0:', when='+slepc')
    depends_on('mumps +metis+parmetis+ptscotch+scotch', when='+mumps')
    depends_on('scorep', when='+scorep')

    def configure_args(self):
        spec = self.spec
        args = []

        if spec.satisfies('+shared'):
            args.append('--enable-shared')

        args.append('--enable-checks={}'.format(spec.variants['checks'].value))
        args.append('--enable-optimize={}'.format(spec.variants['optimize'].value))

        # Profiling and debugging
        if spec.satisfies('+track'):
            args.append('--enable-track')

        if spec.satisfies('+debug'):
            args.append('--enable-debug')

        if spec.satisfies('+scorep'):
            args.append('--with-scorep={}'.format(spec['scorep'].prefix.bin))

        # Native Language support
        if spec.satisfies('~nls'):
            args.append('--disable-nls')

        # OpenMP support
        if spec.satisfies('+openmp'):
            args.append('--enable-openmp')
        else:
            args.append('--disable-openmp')

        if spec.satisfies('+pvode-openmp'):
            args.append('--enable-pvode-openmp')

        if 'openmp-schedule' in spec.variants:
            args.append('--with-openmp-schedule={}'.format(spec.variants['openmp-schedule'].value))

        # File format (only the parallel versions)
        #args.append('--with-hdf5={}/h5cc'.format(spec['hdf5'].prefix.bin))
        #args.append('--with-parallelhdf5={}/h5pcc'.format(spec['hdf5'].prefix.bin))
        args.append('--with-netcdf={}'.format(spec['netcdf-cxx4'].prefix))
        #args.append('--with-pnetcdf={}'.format(spec['netcdf-cxx4'].prefix))

        # Math libraries
        args.append('--with-fftw={}'.format(spec['fftw'].prefix))

        if spec.satisfies('+sundials'):
            args.append('--with-sundials={}'.format(spec['sundials'].prefix))

        if spec.satisfies('+blaslapack'):
            args.append('--with-lapack={}'.format(spec['netlib-lapack'].prefix))

        if spec.satisfies('+petsc'):
            args.append('--with-petsc={}'.format(spec['petsc'].prefix))

        if spec.satisfies('+slepc'):
            args.append('--with-slepc={}'.format(spec['slepc'].prefix))

        if spec.satisfies('+mumps'):
            args.append('--with-mumps={}'.format(spec['mumps'].prefix))

        return args

