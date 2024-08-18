cmake_minimum_required(VERSION 3.10)
project(clips_vendor)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_vendor_package REQUIRED)

set(EXTRA_CMAKE_FLAGS)
if(CMAKE_SYSTEM_PROCESSOR MATCHES "^(aarch64.*|AARCH64.*|arm64.*|ARM64.*|arm.*|ARM.*)")
  set(EXTRA_CMAKE_FLAGS -DOGRE_SIMD_NEON:BOOL=FALSE  -DOGRE_SIMD_SSE2:BOOL=FALSE)
endif()

ament_vendor(${PROJECT_NAME}
  SATISFIED FALSE
  VCS_TYPE svn
  VCS_URL https://svn.code.sf.net/p/clipsrules/code/
  PATCHES  patches/clips642.cmake.patch
  SOURCE_SUBDIR branches/64x/
  GLOBAL_HOOK
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()

