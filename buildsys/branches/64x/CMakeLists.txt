# Platform detection
if(${CMAKE_SYSTEM_NAME} STREQUAL "Darwin")
  set(CLIPS_OS "DARWIN")
  set(WARNINGS
      "-Wall -Wundef -Wpointer-arith -Wshadow -Wstrict-aliasing \
                  -Winline -Wmissing-declarations -Wredundant-decls \
                  -Wmissing-prototypes -Wnested-externs -Wstrict-prototypes \
                  -Waggregate-return -Wno-implicit -Wno-write-strings")
elseif(${CMAKE_SYSTEM_NAME} STREQUAL "Linux")
  set(CLIPS_OS "LINUX")
  set(WARNINGS "-Wall -Wundef -Wpointer-arith -Wshadow -Wstrict-aliasing \
                -Winline -Wredundant-decls -Waggregate-return -fpermissive -Wno-write-strings")
endif()

# Compilation flags
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CLIPS_VERSION 6.4.2)
set(CLIPS_SOVERSION 6)

# set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fpermissive -x c++")
set(CMAKE_CXX_FLAGS "-O3 -g -fno-strict-aliasing -fPIC ${WARNINGS} -fpermissive" ${CMAKE_CXX_FLAGS})
set(CMAKE_C_FLAGS "-O3 -g -fno-strict-aliasing -fPIC ${WARNINGS} -fpermissive" ${CMAKE_C_FLAGS})
find_package(Python3 REQUIRED COMPONENTS Interpreter)
add_subdirectory(core)
if(BUILD_WITH_JAVA_EXAMPLES)
  add_subdirectory(clipsjni)
endif()
if(BUILD_WITH_CLIPS_EXAMPLES)
  install(DIRECTORY examples DESTINATION .)
endif()
