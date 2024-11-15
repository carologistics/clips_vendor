# Source files
set(SOURCES
    agenda.c
    analysis.c
    argacces.c
    bload.c
    bmathfun.c
    bsave.c
    classcom.c
    classexm.c
    classfun.c
    classinf.c
    classini.c
    classpsr.c
    clsltpsr.c
    commline.c
    conscomp.c
    constrct.c
    constrnt.c
    crstrtgy.c
    cstrcbin.c
    cstrccom.c
    cstrcpsr.c
    cstrnbin.c
    cstrnchk.c
    cstrncmp.c
    cstrnops.c
    cstrnpsr.c
    cstrnutl.c
    default.c
    defins.c
    developr.c
    dffctbin.c
    dffctbsc.c
    dffctcmp.c
    dffctdef.c
    dffctpsr.c
    dffnxbin.c
    dffnxcmp.c
    dffnxexe.c
    dffnxfun.c
    dffnxpsr.c
    dfinsbin.c
    dfinscmp.c
    drive.c
    emathfun.c
    engine.c
    envrnmnt.c
    envrnbld.c
    evaluatn.c
    expressn.c
    exprnbin.c
    exprnops.c
    exprnpsr.c
    extnfunc.c
    factbin.c
    factbld.c
    factcmp.c
    factcom.c
    factfun.c
    factgen.c
    facthsh.c
    factfile.c
    factlhs.c
    factmch.c
    factmngr.c
    factprt.c
    factqpsr.c
    factqury.c
    factrete.c
    factrhs.c
    filecom.c
    filertr.c
    fileutil.c
    generate.c
    genrcbin.c
    genrccmp.c
    genrccom.c
    genrcexe.c
    genrcfun.c
    genrcpsr.c
    globlbin.c
    globlbsc.c
    globlcmp.c
    globlcom.c
    globldef.c
    globlpsr.c
    immthpsr.c
    incrrset.c
    inherpsr.c
    inscom.c
    insfile.c
    insfun.c
    insmngr.c
    insmoddp.c
    insmult.c
    inspsr.c
    insquery.c
    insqypsr.c
    iofun.c
    lgcldpnd.c
    memalloc.c
    miscfun.c
    modulbin.c
    modulbsc.c
    modulcmp.c
    moduldef.c
    modulpsr.c
    modulutl.c
    msgcom.c
    msgfun.c
    msgpass.c
    msgpsr.c
    multifld.c
    multifun.c
    objbin.c
    objcmp.c
    objrtbin.c
    objrtbld.c
    objrtcmp.c
    objrtfnx.c
    objrtgen.c
    objrtmch.c
    parsefun.c
    pattern.c
    pprint.c
    prccode.c
    prcdrfun.c
    prcdrpsr.c
    prdctfun.c
    prntutil.c
    proflfun.c
    reorder.c
    reteutil.c
    retract.c
    router.c
    rulebin.c
    rulebld.c
    rulebsc.c
    rulecmp.c
    rulecom.c
    rulecstr.c
    ruledef.c
    ruledlt.c
    rulelhs.c
    rulepsr.c
    scanner.c
    sortfun.c
    strngfun.c
    strngrtr.c
    symblbin.c
    symblcmp.c
    symbol.c
    sysdep.c
    textpro.c
    tmpltbin.c
    tmpltbsc.c
    tmpltcmp.c
    tmpltdef.c
    tmpltfun.c
    tmpltlhs.c
    tmpltpsr.c
    tmpltrhs.c
    tmpltutl.c
    userdata.c
    userfunctions.c
    utility.c
    watch.c)

# Header files (to be installed)
set(HEADERS
    clips.h
    constant.h
    globlpsr.h
    match.h
    network.h
    object.h
    setup.h
    usrsetup.h
    agenda.h
    analysis.h
    argacces.h
    bload.h
    bmathfun.h
    bsave.h
    classcom.h
    classexm.h
    classfun.h
    classinf.h
    classini.h
    classpsr.h
    clsltpsr.h
    commline.h
    conscomp.h
    constrct.h
    constrnt.h
    crstrtgy.h
    cstrcbin.h
    cstrccmp.h
    cstrccom.h
    cstrcpsr.h
    cstrnbin.h
    cstrnchk.h
    cstrncmp.h
    cstrnops.h
    cstrnpsr.h
    cstrnutl.h
    default.h
    defins.h
    developr.h
    dffctbin.h
    dffctbsc.h
    dffctcmp.h
    dffctdef.h
    dffctpsr.h
    dffnxbin.h
    dffnxcmp.h
    dffnxexe.h
    dffnxfun.h
    dffnxpsr.h
    dfinsbin.h
    dfinscmp.h
    drive.h
    emathfun.h
    engine.h
    entities.h
    envrnbld.h
    envrnmnt.h
    evaluatn.h
    expressn.h
    exprnbin.h
    exprnops.h
    exprnpsr.h
    extnfunc.h
    factbin.h
    factbld.h
    factcmp.h
    factcom.h
    factfile.h
    factfun.h
    factgen.h
    facthsh.h
    factlhs.h
    factmch.h
    factmngr.h
    factprt.h
    factqpsr.h
    factqury.h
    factrete.h
    factrhs.h
    filecom.h
    filertr.h
    fileutil.h
    generate.h
    genrcbin.h
    genrccmp.h
    genrccom.h
    genrcexe.h
    genrcfun.h
    genrcpsr.h
    globlbin.h
    globlbsc.h
    globlcmp.h
    globlcom.h
    globldef.h
    immthpsr.h
    incrrset.h
    inherpsr.h
    inscom.h
    insfile.h
    insfun.h
    insmngr.h
    insmoddp.h
    insmult.h
    inspsr.h
    insquery.h
    insqypsr.h
    iofun.h
    lgcldpnd.h
    memalloc.h
    miscfun.h
    modulbin.h
    modulbsc.h
    modulcmp.h
    moduldef.h
    modulpsr.h
    modulutl.h
    msgcom.h
    msgfun.h
    msgpass.h
    msgpsr.h
    multifld.h
    multifun.h
    objbin.h
    objcmp.h
    objrtbin.h
    objrtbld.h
    objrtcmp.h
    objrtfnx.h
    objrtgen.h
    objrtmch.h
    parsefun.h
    pattern.h
    pprint.h
    prccode.h
    prcdrfun.h
    prcdrpsr.h
    prdctfun.h
    prntutil.h
    proflfun.h
    reorder.h
    reteutil.h
    retract.h
    router.h
    rulebin.h
    rulebld.h
    rulebsc.h
    rulecmp.h
    rulecom.h
    rulecstr.h
    ruledef.h
    ruledlt.h
    rulelhs.h
    rulepsr.h
    scanner.h
    sortfun.h
    strngfun.h
    strngrtr.h
    symblbin.h
    symblcmp.h
    symbol.h
    sysdep.h
    textpro.h
    tmpltbin.h
    tmpltbsc.h
    tmpltcmp.h
    tmpltdef.h
    tmpltfun.h
    tmpltlhs.h
    tmpltpsr.h
    tmpltrhs.h
    tmpltutl.h
    userdata.h
    utility.h
    watch.h)

file(GLOB ACTUAL_SOURCES "*.c")
file(GLOB ACTUAL_HEADERS "*.h")
# Sort the lists for comparison
list(SORT SOURCES)
list(SORT HEADERS)
list(SORT ACTUAL_SOURCES)
list(SORT ACTUAL_HEADERS)
# Strip paths from the actual files list
foreach(file_path ${ACTUAL_SOURCES})
  get_filename_component(file_name ${file_path} NAME)
  list(APPEND ACTUAL_SOURCES_STRIPPED ${file_name})
endforeach()

foreach(file_path ${ACTUAL_HEADERS})
  get_filename_component(file_name ${file_path} NAME)
  list(APPEND ACTUAL_HEADERS_STRIPPED ${file_name})
endforeach()
list(REMOVE_ITEM ACTUAL_SOURCES_STRIPPED main.c)

# Compare and warn if there is a mismatch
if(NOT SOURCES STREQUAL ACTUAL_SOURCES_STRIPPED)
  message(
    WARNING
      "The SOURCES list does not match the actual .c files in the directory.")
  list(APPEND S_NO_ACTUAL ${SOURCES})
  list(REMOVE_ITEM S_NO_ACTUAL ${ACTUAL_SOURCES_STRIPPED})
  message(WARNING "only in SOURCES list: ${S_NO_ACTUAL}")
  list(APPEND ACTUAL_NO_S ${ACTUAL_SOURCES_STRIPPED})
  list(REMOVE_ITEM ACTUAL_NO_S ${SOURCES})
  message(WARNING "only in real directory: ${ACTUAL_NO_S}")
endif()

if(NOT HEADERS STREQUAL ACTUAL_HEADERS_STRIPPED)
  message(
    WARNING
      "The HEADERS list does not match the actual .h files in the directory.")
  list(APPEND S_NO_ACTUAL ${HEADERS})
  list(REMOVE_ITEM S_NO_ACTUAL ${ACTUAL_HEADERS_STRIPPED})
  message(WARNING "only in HEADERS list: ${S_NO_ACTUAL}")
  list(APPEND ACTUAL_NO_S ${ACTUAL_HEADERS_STRIPPED})
  list(REMOVE_ITEM ACTUAL_NO_S ${HEADERS})
  message(WARNING "only in real directory: ${ACTUAL_NO_S}")
endif()

set(NAMESPACED_SOURCES_DIR ${CMAKE_BINARY_DIR}/ns_core)

set(NAMESPACED_HEADERS "")
foreach(header ${HEADERS})
	list(APPEND NAMESPACED_HEADERS "${NAMESPACED_SOURCES_DIR}/${header}")
endforeach()
set(NAMESPACED_SOURCES "")
foreach(source ${SOURCES})
	list(APPEND NAMESPACED_SOURCES "${NAMESPACED_SOURCES_DIR}/${source}")
endforeach()

set(PREPROCESS_SCRIPT "${CMAKE_CURRENT_SOURCE_DIR}/../add_namespace.py")

# Step 1: Create preprocessed directory
file(MAKE_DIRECTORY ${NAMESPACED_SOURCES_DIR})
add_custom_command(
	OUTPUT ${NAMESPACED_SOURCES} ${NAMESPACED_HEADERS}
	COMMAND ${Python3_EXECUTABLE} ${PREPROCESS_SCRIPT} ${CMAKE_CURRENT_SOURCE_DIR} ${NAMESPACED_SOURCES_DIR} --namespace clips
    DEPENDS ${PREPROCESS_SCRIPT}
    COMMENT "Preprocessing core lib with namespace"
    DEPENDS ${SOURCES} ${HEADERS}
)

# Create shared library with namespaces
add_library(libclips_ns SHARED ${NAMESPACED_SOURCES})
target_compile_options(libclips_ns PRIVATE -x c++)
target_compile_options(libclips_ns PRIVATE -std=gnu++11)
set_target_properties(libclips_ns PROPERTIES PREFIX ""
                                          VERSION ${CLIPS_VERSION}
                                          SOVERSION ${CLIPS_SOVERSION})
target_include_directories(
  libclips_ns PUBLIC $<BUILD_INTERFACE:${NAMESPACED_SOURCES_DIR}>
                  $<INSTALL_INTERFACE:include>)
set_target_properties(libclips_ns PROPERTIES LINKER_LANGUAGE CXX)

# Install the shared library
install(
  TARGETS libclips_ns
  EXPORT export_libclips_ns
  LIBRARY DESTINATION lib
  ARCHIVE DESTINATION lib
  INCLUDES DESTINATION include)
install(FILES ${NAMESPACED_HEADERS} DESTINATION include/clips_ns)
install(EXPORT export_libclips_ns
		FILE ClipsNSTargets.cmake
		NAMESPACE ClipsNS::
        DESTINATION lib/cmake/clips)

# Create shared library
add_library(libclips SHARED ${SOURCES})
target_compile_options(libclips PRIVATE -x c++)
target_compile_options(libclips PRIVATE -std=gnu++11)
set_target_properties(libclips PROPERTIES PREFIX ""
                                          VERSION ${CLIPS_VERSION}
                                          SOVERSION ${CLIPS_SOVERSION})
target_include_directories(
  libclips PUBLIC $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
                  $<INSTALL_INTERFACE:include>)
set_target_properties(libclips PROPERTIES LINKER_LANGUAGE CXX)

# Install the shared library
install(
  TARGETS libclips
  EXPORT export_libclips
  LIBRARY DESTINATION lib
  ARCHIVE DESTINATION lib
  INCLUDES DESTINATION include)
install(FILES ${HEADERS} DESTINATION include/clips)


# Main executable
set_source_files_properties(main.c PROPERTIES LANGUAGE CXX)
add_executable(clips main.c)
target_link_libraries(clips PRIVATE libclips m)
set_target_properties(clips PROPERTIES LINKER_LANGUAGE CXX)

# Install the main executable
install(TARGETS clips RUNTIME DESTINATION bin)

# create shared c library for jni
add_library(libclips_c SHARED ${SOURCES})
target_compile_options(libclips_c PRIVATE -x c)
target_compile_options(libclips_c PRIVATE -std=c99)
#target_compile_options(libclips_c PRIVATE -x c)
set_target_properties(libclips_c PROPERTIES PREFIX ""
                                          VERSION ${CLIPS_VERSION}
                                          SOVERSION ${CLIPS_SOVERSION})
target_include_directories(
  libclips_c PUBLIC $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
                  $<INSTALL_INTERFACE:include>)
set_target_properties(libclips_c PROPERTIES LINKER_LANGUAGE C)
install(
  TARGETS libclips_c
  EXPORT export_libclips_c
  LIBRARY DESTINATION lib
  ARCHIVE DESTINATION lib
  INCLUDES DESTINATION include)

install(EXPORT export_libclips
		FILE ClipsTargets.cmake
		NAMESPACE Clips::
        DESTINATION lib/cmake/clips)
install(EXPORT export_libclips_c
		FILE ClipsCTargets.cmake
		NAMESPACE ClipsC::
        DESTINATION lib/cmake/clips)


include(CMakePackageConfigHelpers)
write_basic_package_version_file(
    "${CMAKE_CURRENT_BINARY_DIR}/clipsConfigVersion.cmake"
	VERSION ${CLIPS_VERSION}
    COMPATIBILITY AnyNewerVersion
)

configure_file(clipsConfig.cmake.in
               "${CMAKE_CURRENT_BINARY_DIR}/clipsConfig.cmake"
               @ONLY)

install(FILES
  "${CMAKE_CURRENT_BINARY_DIR}/clipsConfig.cmake"
  "${CMAKE_CURRENT_BINARY_DIR}/clipsConfigVersion.cmake"
  DESTINATION lib/cmake/clips
)
