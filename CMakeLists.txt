cmake_minimum_required(VERSION 3.10)
project(clips_vendor)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_vendor_package REQUIRED)

set(CLIPS_REVISION r925)
set(CLIPS_SOURCE clipsrules-code-${CLIPS_REVISION})
set(CLIPS_SRC_DIR ${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}-prefix/src/${PROJECT_NAME})

# Patch file that applies the whole cmake-based buildsys
set(PATCH_FILE ${CMAKE_CURRENT_BINARY_DIR}/buildsys.patch)
# Clear the patch file if it exists (to avoid appending to old patches)
file(WRITE ${PATCH_FILE} "")
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/empty)

# Generate entry point that is dependent on the actual CLIPS_SOURCE dir name
set(TOP_DIR_CMAKE_FILE ${CMAKE_CURRENT_BINARY_DIR}/CMakeLists.txt)
set(CORE_CAST_C_PATCH_FILE ${CMAKE_CURRENT_BINARY_DIR}/core_cast_c.patch)
configure_file(
    ${CMAKE_SOURCE_DIR}/toplevel.buildsys.CMakeLists.txt.in
    ${TOP_DIR_CMAKE_FILE}
    @ONLY
)

set(BRANCH 64x)
configure_file(
    ${CMAKE_SOURCE_DIR}/core_cast_c.patch.in
    ${CORE_CAST_C_PATCH_FILE}
    @ONLY
)

# Generate the patch for the entire buildsys directory by diffing against the empty directory
execute_process(
  COMMAND git diff --no-index --dst-prefix=b/${CLIPS_SOURCE}/ ${CMAKE_CURRENT_BINARY_DIR}/empty ""
  WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/buildsys
  RESULT_VARIABLE diff_result
  OUTPUT_VARIABLE raw_patch_output
  ERROR_VARIABLE patch_error
)
if(diff_result EQUAL 1)
  file(APPEND ${PATCH_FILE} "${raw_patch_output}")
else()
  message(FATAL_ERROR "git diff failed: ${patch_error}")
endif()
# Generate the patch for top-level build file
execute_process(
  COMMAND git diff --no-index /dev/null CMakeLists.txt
  WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
  RESULT_VARIABLE diff_result
  OUTPUT_VARIABLE raw_patch_output
  ERROR_VARIABLE patch_error
)
if(diff_result EQUAL 1)
  file(APPEND ${PATCH_FILE} "${raw_patch_output}")
else()
  message(FATAL_ERROR "git diff failed: ${patch_error}")
endif()

# Apply the reverse patch silently in case it is still floating around
if(EXISTS ${CLIPS_SRC_DIR})
  message(STATUS "Directory exists: ${DIRECTORY_TO_CHECK}, reverse patch ...")

  execute_process(
    COMMAND git apply --no-index -R ${PATCH_FILE}
    WORKING_DIRECTORY ${CLIPS_SRC_DIR}
    RESULT_VARIABLE patch_result
    OUTPUT_QUIET
    ERROR_QUIET
  )
  execute_process(
    COMMAND git apply --no-index -R ${CORE_CAST_C_PATCH_FILE}
    WORKING_DIRECTORY ${CLIPS_SRC_DIR}
    RESULT_VARIABLE patch_result
    OUTPUT_QUIET
    ERROR_QUIET
  )
endif()

ament_vendor(${PROJECT_NAME}
  SATISFIED FALSE
  VCS_TYPE zip
  VCS_URL https://raw.githubusercontent.com/carologistics/clips_vendor/${CLIPS_REVISION}/${CLIPS_SOURCE}.zip
  PATCHES ${PATCH_FILE} ${CORE_CAST_C_PATCH_FILE}
  CMAKE_ARGS
    -DBUILD_WITH_JAVA_EXAMPLES=${BUILD_WITH_JAVA_EXAMPLES}
    -DBUILD_WITH_CLIPS_EXAMPLES=${BUILD_WITH_CLIPS_EXAMPLES}
  GLOBAL_HOOK
)

ament_package()

