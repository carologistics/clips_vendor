cmake_minimum_required(VERSION 3.10)
project(clips_vendor)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_vendor_package REQUIRED)

ament_vendor(${PROJECT_NAME}
  SATISFIED FALSE
  VCS_TYPE svn
  VCS_VERSION 914
  VCS_URL https://svn.code.sf.net/p/clipsrules/code/branches/64x
  CMAKE_ARGS
    -DBUILD_WITH_JAVA_EXAMPLES=${BUILD_WITH_JAVA_EXAMPLES}
    -DBUILD_WITH_CLIPS_EXAMPLES=${BUILD_WITH_CLIPS_EXAMPLES}
  GLOBAL_HOOK
)

ExternalProject_Get_property(${PROJECT_NAME} SOURCE_DIR)
execute_process(
  COMMAND ${CMAKE_COMMAND} -E copy_if_different
  ${CMAKE_CURRENT_SOURCE_DIR}/buildsys/CMakeLists.txt
  ${SOURCE_DIR}/CMakeLists.txt
  COMMAND ${CMAKE_COMMAND} -E copy_if_different
  ${CMAKE_CURRENT_SOURCE_DIR}/buildsys/add_namespace.py
  ${SOURCE_DIR}/add_namespace.py
  COMMAND ${CMAKE_COMMAND} -E copy_if_different
  ${CMAKE_CURRENT_SOURCE_DIR}/buildsys/core/CMakeLists.txt
  ${SOURCE_DIR}/core/CMakeLists.txt
  COMMAND ${CMAKE_COMMAND} -E copy_if_different
  ${CMAKE_CURRENT_SOURCE_DIR}/buildsys/core/clipsConfig.cmake.in
  ${SOURCE_DIR}/core/clipsConfig.cmake.in
  COMMAND ${CMAKE_COMMAND} -E copy_if_different
  ${CMAKE_CURRENT_SOURCE_DIR}/buildsys/clipsjni/CMakeLists.txt
  ${SOURCE_DIR}/clipsjni/CMakeLists.txt
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()

