cmake_minimum_required(VERSION 3.10)
project(clips_vendor)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_vendor_package REQUIRED)

ament_vendor(${PROJECT_NAME}
  SATISFIED FALSE
  VCS_TYPE svn
  VCS_VERSION 914
  VCS_URL https://svn.code.sf.net/p/clipsrules/code/branches/64x
  PATCHES  patches/clips642.cmake.patch
  GLOBAL_HOOK
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()

