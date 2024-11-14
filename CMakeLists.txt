cmake_minimum_required(VERSION 3.10)
project(clips_vendor)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_vendor_package REQUIRED)

# Output patch file location
set(PATCH_FILE ${CMAKE_CURRENT_BINARY_DIR}/buildsys.patch)

# Clear the patch file if it exists (to avoid appending to old patches)
file(WRITE ${PATCH_FILE} "")

file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/empty)

# Generate the patch for the entire buildsys directory by diffing against the empty directory
execute_process(
  COMMAND git diff --no-index --dst-prefix= ${CMAKE_CURRENT_BINARY_DIR}/empty buildsys/
  WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
  RESULT_VARIABLE diff_result
  OUTPUT_VARIABLE raw_patch_output
  ERROR_VARIABLE patch_error
)
if(diff_result EQUAL 1)
  file(APPEND ${PATCH_FILE} "${raw_patch_output}")
else()
  message(FATAL_ERROR "git diff failed: ${patch_error}")
endif()

set(CLIPS_SRC_DIR ${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}-prefix/src/${PROJECT_NAME})

if(EXISTS ${CLIPS_SRC_DIR})
  message(STATUS "Directory exists: ${DIRECTORY_TO_CHECK}, reverse patch ...")

  # Apply the reverse patch silently in case it is still floating around
  execute_process(
    COMMAND git apply --no-index -R ${PATCH_FILE}
    WORKING_DIRECTORY ${CLIPS_SRC_DIR}
    RESULT_VARIABLE patch_result
    OUTPUT_QUIET
    ERROR_QUIET
  )
endif()

ament_vendor(${PROJECT_NAME}
  SATISFIED FALSE
  VCS_TYPE svn
  VCS_VERSION 925
  VCS_URL https://svn.code.sf.net/p/clipsrules/code/branches/64x
  PATCHES ${PATCH_FILE}
  CMAKE_ARGS
    -DBUILD_WITH_JAVA_EXAMPLES=${BUILD_WITH_JAVA_EXAMPLES}
    -DBUILD_WITH_CLIPS_EXAMPLES=${BUILD_WITH_CLIPS_EXAMPLES}
  GLOBAL_HOOK
)

ament_package()

