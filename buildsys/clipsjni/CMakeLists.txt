# Find Java
find_package(Java REQUIRED)
include(UseJava)
find_package(JNI REQUIRED)

set(SRC_DIR java-src)
set(NATIVE_SRC_DIR library-src)
# Main CLIPSJNI library
set(JNI_CP net/sf/clipsrules/jni)
set(JNI_FILES
    ${SRC_DIR}/${JNI_CP}/Activation.java
    ${SRC_DIR}/${JNI_CP}/Agenda.java
    ${SRC_DIR}/${JNI_CP}/BaseRouter.java
    ${SRC_DIR}/${JNI_CP}/CaptureRouter.java
    ${SRC_DIR}/${JNI_CP}/CLIPSException.java
    ${SRC_DIR}/${JNI_CP}/Focus.java
    ${SRC_DIR}/${JNI_CP}/CLIPSLineError.java
    ${SRC_DIR}/${JNI_CP}/CLIPSLoadException.java
    ${SRC_DIR}/${JNI_CP}/CLIPSType.java
    ${SRC_DIR}/${JNI_CP}/CommandExecutionEvent.java
    ${SRC_DIR}/${JNI_CP}/CommandExecutionListener.java
    ${SRC_DIR}/${JNI_CP}/CommandPromptTextArea.java
    ${SRC_DIR}/${JNI_CP}/Environment.java
    ${SRC_DIR}/${JNI_CP}/ExternalAddressValue.java
    ${SRC_DIR}/${JNI_CP}/FactInstance.java
    ${SRC_DIR}/${JNI_CP}/FactAddressValue.java
    ${SRC_DIR}/${JNI_CP}/FloatValue.java
    ${SRC_DIR}/${JNI_CP}/Focus.java
    ${SRC_DIR}/${JNI_CP}/FocusStack.java
    ${SRC_DIR}/${JNI_CP}/InstanceAddressValue.java
    ${SRC_DIR}/${JNI_CP}/InstanceNameValue.java
    ${SRC_DIR}/${JNI_CP}/IntegerValue.java
    ${SRC_DIR}/${JNI_CP}/LexemeValue.java
    ${SRC_DIR}/${JNI_CP}/Module.java
    ${SRC_DIR}/${JNI_CP}/MultifieldValue.java
    ${SRC_DIR}/${JNI_CP}/NumberValue.java
    ${SRC_DIR}/${JNI_CP}/PeriodicCallback.java
    ${SRC_DIR}/${JNI_CP}/PrimitiveValue.java
    ${SRC_DIR}/${JNI_CP}/Router.java
    ${SRC_DIR}/${JNI_CP}/RouterTextArea.java
    ${SRC_DIR}/${JNI_CP}/SlotValue.java
    ${SRC_DIR}/${JNI_CP}/StringValue.java
    ${SRC_DIR}/${JNI_CP}/SymbolValue.java
    ${SRC_DIR}/${JNI_CP}/UserFunction.java
    ${SRC_DIR}/${JNI_CP}/UserFunctionExamples.java
    ${SRC_DIR}/${JNI_CP}/VoidValue.java)
set(NATIVE_FILES
    ${NATIVE_SRC_DIR}/clipsjni_environment.c
    ${NATIVE_SRC_DIR}/clipsjni_environment_facts.c
    ${NATIVE_SRC_DIR}/clipsjni_environment_instances.c
    ${NATIVE_SRC_DIR}/clipsjni_environment_repl.c
    ${NATIVE_SRC_DIR}/clipsjni_environment_routers.c
    ${NATIVE_SRC_DIR}/clipsjni_environment_rules.c
    ${NATIVE_SRC_DIR}/clipsjni_glue.c
    ${NATIVE_SRC_DIR}/clipsjni_utilities.c)

set_source_files_properties(${NATIVE_FILES} PROPERTIES LANGUAGE C)

add_library(CLIPSJNI SHARED ${NATIVE_FILES})
target_link_libraries(CLIPSJNI PUBLIC libclips_c)
target_include_directories(CLIPSJNI PRIVATE ${JNI_INCLUDE_DIRS})
set_target_properties(CLIPSJNI PROPERTIES LINKER_LANGUAGE C)
set_target_properties(CLIPSJNI PROPERTIES
    COMPILE_FLAGS "-fPIC"
)
install(
  TARGETS CLIPSJNI
  LIBRARY DESTINATION lib
  ARCHIVE DESTINATION lib)

add_jar(
  JavaCLIPSJNI
  SOURCES ${JNI_FILES}
  OUTPUT_NAME CLIPSJNI
  VERSION ${CLIPS_VERSION}
  ENTRY_POINT net.sf.clipsrules.jni.Environment)
install_jar(JavaCLIPSJNI DESTINATION share/clips/java)

# custom manifest to add class path of main jar
file(WRITE ${CMAKE_BINARY_DIR}/META-INF/MANIFEST.MF
     "Manifest-Version: ${CLIPS_VERSION}\n" "Class-Path: CLIPSJNI.jar\n")

# AnimalDemo
set(ANIMAL_CP net/sf/clipsrules/jni/examples/animal)
file(
  GLOB ANIMAL_RSRC_FILES
  RELATIVE ${CMAKE_CURRENT_SOURCE_DIR}
  ${SRC_DIR}/${ANIMAL_CP}/resources/*)
add_jar(
  AnimalDemo
  SOURCES ${SRC_DIR}/${ANIMAL_CP}/AnimalDemo.java
  ENTRY_POINT net.sf.clipsrules.jni.examples.animal.AnimalDemo
  INCLUDE_JARS JavaCLIPSJNI
  OUTPUT_NAME AnimalDemo
  VERSION ${CLIPS_VERSION} RESOURCES NAMESPACE ${ANIMAL_CP}/resources
                           ${ANIMAL_RSRC_FILES}
  MANIFEST ${CMAKE_BINARY_DIR}/META-INF/MANIFEST.MF)
install_jar(AnimalDemo DESTINATION share/clips/java)
file(
  GENERATE
  OUTPUT clips-animal-demo
  CONTENT
    "#!/bin/sh\n \
    java -jar $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}>$<INSTALL_INTERFACE:${CMAKE_CURRENT_INSTALL_DIR}/bin>/AnimalDemo.jar \"\$@\"\n"
)
install(
  PROGRAMS ${CMAKE_CURRENT_BINARY_DIR}/clips-animal-demo
  DESTINATION bin
  PERMISSIONS
    OWNER_EXECUTE
    OWNER_WRITE
    OWNER_READ
    GROUP_EXECUTE
    GROUP_READ
    WORLD_EXECUTE
    WORLD_READ)

# AutoDemo
set(AUTO_CP net/sf/clipsrules/jni/examples/auto)
file(
  GLOB AUTO_RSRC_FILES
  RELATIVE ${CMAKE_CURRENT_SOURCE_DIR}
  ${SRC_DIR}/${AUTO_CP}/resources/*)
add_jar(
  AutoDemo
  SOURCES ${SRC_DIR}/${AUTO_CP}/AutoDemo.java
  ENTRY_POINT net.sf.clipsrules.jni.examples.auto.AutoDemo
  INCLUDE_JARS JavaCLIPSJNI
  OUTPUT_NAME AutoDemo
  VERSION ${CLIPS_VERSION} RESOURCES NAMESPACE ${AUTO_CP}/resources
                           ${AUTO_RSRC_FILES}
  MANIFEST ${CMAKE_BINARY_DIR}/META-INF/MANIFEST.MF)
install_jar(AutoDemo DESTINATION share/clips/java)
file(
  GENERATE
  OUTPUT clips-auto-demo
  CONTENT
    "#!/bin/sh\n \
    java -jar $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}>$<INSTALL_INTERFACE:${CMAKE_CURRENT_INSTALL_DIR}/bin>/AutoDemo.jar \"\$@\"\n"
)
install(
  PROGRAMS ${CMAKE_CURRENT_BINARY_DIR}/clips-auto-demo
  DESTINATION bin
  PERMISSIONS
    OWNER_EXECUTE
    OWNER_WRITE
    OWNER_READ
    GROUP_EXECUTE
    GROUP_READ
    WORLD_EXECUTE
    WORLD_READ)

# SudokuDemo
set(SUDOKU_CP net/sf/clipsrules/jni/examples/sudoku)
file(
  GLOB SUDOKU_RSRC_FILES
  RELATIVE ${CMAKE_CURRENT_SOURCE_DIR}
  ${SRC_DIR}/${SUDOKU_CP}/resources/*)
add_jar(
  SudokuDemo
  SOURCES ${SRC_DIR}/${SUDOKU_CP}/SudokuDemo.java
  ENTRY_POINT net.sf.clipsrules.jni.examples.sudoku.SudokuDemo
  INCLUDE_JARS JavaCLIPSJNI
  OUTPUT_NAME SudokuDemo
  VERSION ${CLIPS_VERSION} RESOURCES NAMESPACE ${SUDOKU_CP}/resources
                           ${SUDOKU_RSRC_FILES}
  MANIFEST ${CMAKE_BINARY_DIR}/META-INF/MANIFEST.MF)
install_jar(SudokuDemo DESTINATION share/clips/java)
file(
  GENERATE
  OUTPUT clips-sudoku-demo
  CONTENT
    "#!/bin/sh\n \
    java -jar $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}>$<INSTALL_INTERFACE:${CMAKE_CURRENT_INSTALL_DIR}/bin>/SudokuDemo.jar \"\$@\"\n"
)
install(
  PROGRAMS ${CMAKE_CURRENT_BINARY_DIR}/clips-sudoku-demo
  DESTINATION bin
  PERMISSIONS
    OWNER_EXECUTE
    OWNER_WRITE
    OWNER_READ
    GROUP_EXECUTE
    GROUP_READ
    WORLD_EXECUTE
    WORLD_READ)

# WineDemo
set(WINE_CP net/sf/clipsrules/jni/examples/wine)
file(
  GLOB WINE_RSRC_FILES
  RELATIVE ${CMAKE_CURRENT_SOURCE_DIR}
  ${SRC_DIR}/${WINE_CP}/resources/*)
add_jar(
  WineDemo
  SOURCES ${SRC_DIR}/${WINE_CP}/WineDemo.java
  ENTRY_POINT net.sf.clipsrules.jni.examples.wine.WineDemo
  INCLUDE_JARS JavaCLIPSJNI
  OUTPUT_NAME WineDemo
  VERSION ${CLIPS_VERSION} RESOURCES NAMESPACE ${WINE_CP}/resources
                           ${WINE_RSRC_FILES}
  MANIFEST ${CMAKE_BINARY_DIR}/META-INF/MANIFEST.MF)
install_jar(WineDemo DESTINATION share/clips/java)
file(
  GENERATE
  OUTPUT clips-wine-demo
  CONTENT
    "#!/bin/sh\n \
    java -jar $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}>$<INSTALL_INTERFACE:${CMAKE_CURRENT_INSTALL_DIR}/bin>/WineDemo.jar \"\$@\"\n"
)
install(
  PROGRAMS ${CMAKE_CURRENT_BINARY_DIR}/clips-wine-demo
  DESTINATION bin
  PERMISSIONS
    OWNER_EXECUTE
    OWNER_WRITE
    OWNER_READ
    GROUP_EXECUTE
    GROUP_READ
    WORLD_EXECUTE
    WORLD_READ)

# RouterDemo
set(ROUTER_CP net/sf/clipsrules/jni/examples/router)
file(
  GLOB ROUTER_RSRC_FILES
  RELATIVE ${CMAKE_CURRENT_SOURCE_DIR}
  ${SRC_DIR}/${ROUTER_CP}/resources/*)
add_jar(
  RouterDemo
  SOURCES ${SRC_DIR}/${ROUTER_CP}/RouterDemo.java
  ENTRY_POINT net.sf.clipsrules.jni.examples.router.RouterDemo
  INCLUDE_JARS JavaCLIPSJNI
  OUTPUT_NAME RouterDemo
  VERSION ${CLIPS_VERSION} RESOURCES NAMESPACE ${ROUTER_CP}/resources
                           ${ROUTER_RSRC_FILES}
  MANIFEST ${CMAKE_BINARY_DIR}/META-INF/MANIFEST.MF)
install_jar(RouterDemo DESTINATION share/clips/java)
file(
  GENERATE
  OUTPUT clips-router-demo
  CONTENT
    "#!/bin/sh\n \
java -jar $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}>$<INSTALL_INTERFACE:${CMAKE_CURRENT_INSTALL_DIR}/bin>/RouterDemo.jar \"\$@\"\n"
)
install(
  PROGRAMS ${CMAKE_CURRENT_BINARY_DIR}/clips-router-demo
  DESTINATION bin
  PERMISSIONS
    OWNER_EXECUTE
    OWNER_WRITE
    OWNER_READ
    GROUP_EXECUTE
    GROUP_READ
    WORLD_EXECUTE
    WORLD_READ)

# CLIPS IDE
set(IDE_CP net/sf/clipsrules/jni/examples/ide)
set(IDE_FILES
    ${SRC_DIR}/${IDE_CP}/CLIPSIDE.java
    ${SRC_DIR}/${IDE_CP}/ActivationTableModel.java
    ${SRC_DIR}/${IDE_CP}/AgendaBrowserFrame.java
    ${SRC_DIR}/${IDE_CP}/AgendaBrowserManager.java
    ${SRC_DIR}/${IDE_CP}/BoundsDesktopManager.java
    ${SRC_DIR}/${IDE_CP}/ConstructInspectorFrame.java
    ${SRC_DIR}/${IDE_CP}/DialogFrame.java
    ${SRC_DIR}/${IDE_CP}/EditMenu.java
    ${SRC_DIR}/${IDE_CP}/EntityBrowserFrame.java
    ${SRC_DIR}/${IDE_CP}/EnvironmentMenu.java
    ${SRC_DIR}/${IDE_CP}/FactBrowserManager.java
    ${SRC_DIR}/${IDE_CP}/FactInstanceTableModel.java
    ${SRC_DIR}/${IDE_CP}/FileMenu.java
    ${SRC_DIR}/${IDE_CP}/FocusStackTableModel.java
    ${SRC_DIR}/${IDE_CP}/FontDialog.java
    ${SRC_DIR}/${IDE_CP}/FontPreferencesDialog.java
    ${SRC_DIR}/${IDE_CP}/FontProperties.java
    ${SRC_DIR}/${IDE_CP}/FontSample.java
    ${SRC_DIR}/${IDE_CP}/FramePlacer.java
    ${SRC_DIR}/${IDE_CP}/HelpMenu.java
    ${SRC_DIR}/${IDE_CP}/IDEPreferences.java
    ${SRC_DIR}/${IDE_CP}/InstanceBrowserManager.java
    ${SRC_DIR}/${IDE_CP}/ModuleTableModel.java
    ${SRC_DIR}/${IDE_CP}/SlotValueTableModel.java
    ${SRC_DIR}/${IDE_CP}/TextFrame.java
    ${SRC_DIR}/${IDE_CP}/TextMenu.java
    ${SRC_DIR}/${IDE_CP}/WatchMenu.java)

file(
  GLOB IDE_RSRC_FILES
  RELATIVE ${CMAKE_CURRENT_SOURCE_DIR}
  ${SRC_DIR}/${IDE_CP}/resources/*)
add_jar(
  CLIPSIDE
  SOURCES ${IDE_FILES}
  ENTRY_POINT net.sf.clipsrules.jni.examples.ide.CLIPSIDE
  INCLUDE_JARS JavaCLIPSJNI
  OUTPUT_NAME CLIPSIDE
  VERSION ${CLIPS_VERSION} RESOURCES NAMESPACE ${IDE_CP}/resources
                           ${IDE_RSRC_FILES}
  MANIFEST ${CMAKE_BINARY_DIR}/META-INF/MANIFEST.MF)
install_jar(CLIPSIDE DESTINATION share/clips/java)
file(
  GENERATE
  OUTPUT clips-ide
  CONTENT
    "#!/bin/sh\n \
java -jar $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}>$<INSTALL_INTERFACE:${CMAKE_CURRENT_INSTALL_DIR}/bin>/CLIPSIDE.jar \"\$@\"\n"
)
install(
  PROGRAMS ${CMAKE_CURRENT_BINARY_DIR}/clips-ide
  DESTINATION bin
  PERMISSIONS
    OWNER_EXECUTE
    OWNER_WRITE
    OWNER_READ
    GROUP_EXECUTE
    GROUP_READ
    WORLD_EXECUTE
    WORLD_READ)
