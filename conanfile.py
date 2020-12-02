from conans import ConanFile, CMake


class Conan(ConanFile):
    url = "https://github.com/biocad/cuq"
    description = "CUDA multi-GPU concurrent tasks queue"
    settings = "os", "build_type", "arch", "compiler", "CUDA"
    generators = "cmake"
    exports_sources = "*"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.parallel = False
        cmake.test(args=["--", 'ARGS=--output-on-failure'])

    def package(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["cuq"]
        # users will be able to link statically with our library
        # but this requires the following system libraries
        self.cpp_info.system_libs = ["cudart", "nvidia-ml", "stdc++"]
        self.cpp_info.libdirs.append("/usr/local/cuda/lib64")

    def deploy(self):
        self.copy("*", dst="include", src="include")
        self.copy("*", dst="lib", src="lib")
