project(eigen-pybind)
cmake_minimum_required(VERSION 3.15...3.27)
find_package(Python 3.8 COMPONENTS Interpreter Development.Module REQUIRED)

if (NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
  set(CMAKE_BUILD_TYPE Release CACHE STRING "Choose the type of build." FORCE)
  set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS "Debug" "Release" "MinSizeRel" "RelWithDebInfo")
endif()

# Detect the installed nanobind package and import it into CMake
execute_process(
  COMMAND "${Python_EXECUTABLE}" -m pybind11 --cmakedir
  OUTPUT_STRIP_TRAILING_WHITESPACE OUTPUT_VARIABLE NB_DIR)
list(APPEND CMAKE_PREFIX_PATH "${NB_DIR}")
find_package(pybind11 CONFIG REQUIRED)

# Add Eigen
find_package(Eigen3 3.4 REQUIRED NO_MODULE)

pybind11_add_module(example src/interface/example.cpp)
target_include_directories(example PRIVATE src/cpp)
target_link_libraries (example PRIVATE Eigen3::Eigen)
