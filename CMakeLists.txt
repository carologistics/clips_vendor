cmake_minimum_required(VERSION 3.10)
project(clips_vendor)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_vendor_package REQUIRED)

set(CLIPS_REVISION r974)
set(CLIPS_SOURCE clipsrules-code-${CLIPS_REVISION})
set(CLIPS_SRC_DIR ${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}-prefix/src/${PROJECT_NAME})

# Patch file that applies the whole cmake-based buildsys
set(PATCH_FILE ${CMAKE_CURRENT_BINARY_DIR}/buildsys.patch)
# Clear the patch file if it exists (to avoid appending to old patches)
file(WRITE ${PATCH_FILE} "")
file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/empty)

# Generate entry point that is dependent on the actual CLIPS_SOURCE dir name
set(TOP_DIR_CMAKE_FILE ${CMAKE_CURRENT_BINARY_DIR}/CMakeLists.txt)
set(DEFFACTS_CALLBACK_PATCH_FILE ${CMAKE_CURRENT_BINARY_DIR}/deffacts_callback.patch)
set(DEFFUNCTION_CALLBACK_PATCH_FILE ${CMAKE_CURRENT_BINARY_DIR}/deffunction_callback.patch)
set(DEFGLOBAL_CALLBACK_PATCH_FILE ${CMAKE_CURRENT_BINARY_DIR}/defglobal_callback.patch)
set(DEFMODULE_CALLBACK_PATCH_FILE ${CMAKE_CURRENT_BINARY_DIR}/defmodule_callback.patch)
set(DEFTEMPLATE_CALLBACK_PATCH_FILE ${CMAKE_CURRENT_BINARY_DIR}/deftemplate_callback.patch)
set(REDEFINE_CALLBACK_PATCH_FILE ${CMAKE_CURRENT_BINARY_DIR}/redefine_callback.patch)
set(RULEDEF_CALLBACK_PATCH_FILE ${CMAKE_CURRENT_BINARY_DIR}/ruledef_callback.patch)
set(RUN_CALLBACK_PATCH_FILE ${CMAKE_CURRENT_BINARY_DIR}/run_callback.patch)
configure_file(
    ${CMAKE_SOURCE_DIR}/toplevel.buildsys.CMakeLists.txt.in
    ${TOP_DIR_CMAKE_FILE}
    @ONLY
)

set(BRANCH 64x)

configure_file(
    ${CMAKE_SOURCE_DIR}/deffacts_callback.patch.in
    ${DEFFACTS_CALLBACK_PATCH_FILE}
    @ONLY
)

configure_file(
    ${CMAKE_SOURCE_DIR}/deffunction_callback.patch.in
    ${DEFFUNCTION_CALLBACK_PATCH_FILE}
    @ONLY
)

configure_file(
    ${CMAKE_SOURCE_DIR}/defglobal_callback.patch.in
    ${DEFGLOBAL_CALLBACK_PATCH_FILE}
    @ONLY
)

configure_file(
    ${CMAKE_SOURCE_DIR}/defmodule_callback.patch.in
    ${DEFMODULE_CALLBACK_PATCH_FILE}
    @ONLY
)

configure_file(
    ${CMAKE_SOURCE_DIR}/deftemplate_callback.patch.in
    ${DEFTEMPLATE_CALLBACK_PATCH_FILE}
    @ONLY
)

configure_file(
    ${CMAKE_SOURCE_DIR}/redefine_callback.patch.in
    ${REDEFINE_CALLBACK_PATCH_FILE}
    @ONLY
)

configure_file(
    ${CMAKE_SOURCE_DIR}/ruledef_callback.patch.in
    ${RULEDEF_CALLBACK_PATCH_FILE}
    @ONLY
)

configure_file(
    ${CMAKE_SOURCE_DIR}/run_callback.patch.in
    ${RUN_CALLBACK_PATCH_FILE}
    @ONLY
)

file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/buildsys/${CLIPS_SOURCE})
file(COPY ${CMAKE_CURRENT_SOURCE_DIR}/buildsys/ DESTINATION ${CMAKE_CURRENT_BINARY_DIR}/buildsys/${CLIPS_SOURCE})

# Generate the patch for the entire buildsys directory by diffing against the empty directory
execute_process(
  COMMAND git diff --no-index --dst-prefix= empty buildsys
  WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
  RESULT_VARIABLE diff_result
  OUTPUT_VARIABLE raw_patch_output
  ERROR_VARIABLE patch_error
  ERROR_STRIP_TRAILING_WHITESPACE
)
if (NOT patch_error STREQUAL "")
  message(FATAL_ERROR "Error occurred: ${patch_error}")
endif()
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
      COMMAND git apply --no-index -R ${DEFFACTS_CALLBACK_PATCH_FILE}
      WORKING_DIRECTORY ${CLIPS_SRC_DIR}
      RESULT_VARIABLE deffacts_callback_patch_result
      OUTPUT_QUIET
      ERROR_QUIET
  )
  
  execute_process(
      COMMAND git apply --no-index -R ${DEFFUNCTION_CALLBACK_PATCH_FILE}
      WORKING_DIRECTORY ${CLIPS_SRC_DIR}
      RESULT_VARIABLE deffunction_callback_patch_result
      OUTPUT_QUIET
      ERROR_QUIET
  )
  
  execute_process(
      COMMAND git apply --no-index -R ${DEFGLOBAL_CALLBACK_PATCH_FILE}
      WORKING_DIRECTORY ${CLIPS_SRC_DIR}
      RESULT_VARIABLE defglobal_callback_patch_result
      OUTPUT_QUIET
      ERROR_QUIET
  )

  execute_process(
      COMMAND git apply --no-index -R ${DEFMODULE_CALLBACK_PATCH_FILE}
      WORKING_DIRECTORY ${CLIPS_SRC_DIR}
      RESULT_VARIABLE defmodule_callback_patch_result
      OUTPUT_QUIET
      ERROR_QUIET
  )
  
  execute_process(
      COMMAND git apply --no-index -R ${DEFTEMPLATE_CALLBACK_PATCH_FILE}
      WORKING_DIRECTORY ${CLIPS_SRC_DIR}
      RESULT_VARIABLE deftemplate_callback_patch_result
      OUTPUT_QUIET
      ERROR_QUIET
  )
  
  execute_process(
      COMMAND git apply --no-index -R ${REDEFINE_CALLBACK_PATCH_FILE}
      WORKING_DIRECTORY ${CLIPS_SRC_DIR}
      RESULT_VARIABLE redefine_callback_patch_result
      OUTPUT_QUIET
      ERROR_QUIET
  )
  
  execute_process(
      COMMAND git apply --no-index -R ${RULEDEF_CALLBACK_PATCH_FILE}
      WORKING_DIRECTORY ${CLIPS_SRC_DIR}
      RESULT_VARIABLE ruledef_callback_patch_result
      OUTPUT_QUIET
      ERROR_QUIET
  )
  
  execute_process(
      COMMAND git apply --no-index -R ${RUN_CALLBACK_PATCH_FILE}
      WORKING_DIRECTORY ${CLIPS_SRC_DIR}
      RESULT_VARIABLE run_callback_patch_result
      OUTPUT_QUIET
      ERROR_QUIET
  )
endif()

ament_vendor(${PROJECT_NAME}
  SATISFIED FALSE
  VCS_TYPE zip
  VCS_URL https://raw.githubusercontent.com/carologistics/clips_vendor/${CLIPS_REVISION}/${CLIPS_SOURCE}.zip
  PATCHES ${PATCH_FILE} ${CORE_CAST_C_PATCH_FILE} ${DEFFACTS_CALLBACK_PATCH_FILE} ${DEFFUNCTION_CALLBACK_PATCH_FILE} ${DEFGLOBAL_CALLBACK_PATCH_FILE} ${DEFMODULE_CALLBACK_PATCH_FILE} ${DEFTEMPLATE_CALLBACK_PATCH_FILE} ${REDEFINE_CALLBACK_PATCH_FILE} ${RULEDEF_CALLBACK_PATCH_FILE} ${RUN_CALLBACK_PATCH_FILE}
  CMAKE_ARGS
    -DBUILD_WITH_JAVA_EXAMPLES=${BUILD_WITH_JAVA_EXAMPLES}
    -DBUILD_WITH_CLIPS_EXAMPLES=${BUILD_WITH_CLIPS_EXAMPLES}
  GLOBAL_HOOK
)

ament_package()

