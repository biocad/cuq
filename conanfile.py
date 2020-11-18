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
        cmake.test()

    def package(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["cuq"]
        self.cpp_info.system_libs = ["nvidia-ml", "cudart", "stdc++"]

    def deploy(self):
        self.copy("*", dst="include", src="include")
        self.copy("*", dst="lib", src="lib")
