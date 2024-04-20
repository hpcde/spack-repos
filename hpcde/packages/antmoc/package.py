from spack.package import *


class Antmoc(CMakePackage):
    """ANT-MOC: Advanced Neutron Transport - Methods of Characteristics."""

    homepage = "https://gitlab.com/HPCer/neutronics/ant-moc"
    url = "https://gitlab.com/HPCer/neutronics/ant-moc/-/archive/0.1.15/ant-moc-0.1.15.tar.gz"
    git = "git@gitlab.com:HPCer/neutronics/ant-moc.git"

    maintainers = ["alephpiece"]

    executables = [r"^antmoc$"]

    license("MIT")

    version("0.1.15", sha256='2a40fdd7803f72eaad1b5fd10c7c701f1e89763a215d1cf1df3fbd76093ac66a')

    variant('cmfd', default=False, description='Enable CMFD acceleration')
    variant('cyclic', default=True,
            description='Enable cyclic tracking (will disable domain decomposition)')
    variant("mpi", default=False, description="Enable MPI support")
    variant('shared', default=True, description='Build shared libraries')

    conflicts('+cmfd', when='+cyclic',
              msg='CMFD is not available for cyclic tracking')

    depends_on("cmake@3.16:", type="build")
    depends_on("mpi@3", when="+mpi", type=("build", "link", "run"))
    depends_on("cxxopts@3")
    depends_on("fmt@6:8 +shared", when="@:0.1.14")
    depends_on("fmt@8:10 +shared", when="@0.1.15:")
    depends_on("tinyxml2@7:10 +shared")
    depends_on("toml11@3.6:3.7")
    depends_on("hdf5@1.10:1.14 ~mpi+shared", when="~mpi")
    depends_on("hdf5@1.10:1.14 +mpi+shared", when="+mpi")
    depends_on("googletest@1.10.0: +gmock+pthreads+shared")

    def url_for_version(self, version):
        if version < Version("0.1.15"):
            return f"https://gitlab.com/HPCer/neutronics/ant-moc/-/archive/v{version}/ant-moc-v{version}.tar.gz"
        return f"https://gitlab.com/HPCer/neutronics/ant-moc/-/archive/{version}/ant-moc-{version}.tar.gz"

    def cmake_args(self):
        spec = self.spec
        args = [
            self.define('USE_INTERNAL_ALL', False),
            self.define('ENABLE_DEBUG', False),
            self.define('ENABLE_TESTS', False),
            self.define('ENABLE_COVERAGE', False),
            self.define('ENABLE_DOUBLE_PRECISION', True),
            self.define_from_variant('BUILD_SHARED_LIBS', 'shared'),
            self.define_from_variant('ENABLE_CYCLIC', 'cyclic'),
            self.define_from_variant('ENABLE_CMFD', 'cmfd'),
            self.define_from_variant('ENABLE_MPI', 'mpi'),
        ]

        return args

