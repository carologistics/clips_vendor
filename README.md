# clips_vendor
Wrapper around clips (https://clipsrules.net/) for usage with ROS 2.
Replaces the make-based original build system by cmake and builds dynamic
libraries for flexible usage.

Contains core implementation, cli and optionally also the clipsjni applications and demos as well as the given examples from the svn source repository (https://svn.code.sf.net/p/clipsrules/code).

Note that clips can be both compiled with c and c++.
Here, the main application and library *libclips.so* is built using c++.
A c shared library *libclips_c.so* is also provided (and used by the clipsjni applications).
Furthermore, a namespaced version *libclips_ns.so* is supplied, which wraps the original files with `namespace clips {}` to minimize conflicts with other libraries and projects.

As clips is written as as a C project there are no namespaces and a lot of preprocessor macros involved, which require some careful considerations.
Make sure to read the [Known Issues](#Known-Issues) to avoid some of the related pitfalls.

# Build Instructions

The optional features are controlled via CMake variables:
 - BUILD_WITH_JAVA_EXAMPLES
 - BUILD_WITH_CLIPS_EXAMPLES

Per default these examples will not be added, to build them from source, simply pass the corresponding cmake args as shown below:
```bash
colcon build --cmake-args -DBUILD_WITH_JAVA_EXAMPLES=true -DBUILD_WITH_CLIPS_EXAMPLES=true
```

# Usage

## CLI
Simply run `clips`:
```bash
clips
```

## Shared Libraries

in CMake:

```cmake
find_package(clips_vendor)
find_package(clips)

...

target_link_libraries(<target> PUBLIC Clips::libclips)      # when using c++ compiled library
target_link_libraries(<target> PUBLIC ClipsC::libclips_c)   # when using c compiled library
target_link_libraries(<target> PUBLIC ClipsNS::libclips_ns) # wen using namespaced c++ library
```

in C++:
```c++
#include<clips/clips.h>    // when using libclips

extern C {
  #include<clips/clips.h>    // when using libclips_c
}

#include<clips_ns/clips.h> // when using libclips_ns
```

## Optional java Examples
The following commands should be available in your path after sourcing:
```bash
 clips-animal-deme
 clips-auto-demo
 clips-ide
 clips-router-demo
 clips-sudoku-demo
 clips-wine-demo
```

## Optional CLIPS Examples
The example files will be located at the installation destination under `opt/clips_vendor/examples`.

# Known Issues
### Clashes with other Libraries
As *libclips* and *libclips_c* contain unnamespaced definitions of structs and functions, it is recommended to use `libclips_ns` instead, to prevent accidental clashes with other libraries.

Regardless of the chosen clips library, inside of CLIPS headers there are a `#define` macros that might interfere with other libraries.
For example, `LHS` and `RHS` macros interfere with template identifiers in `boost/function_types/property_tags.hpp`.

In these cases, undefine the macros after including the `clips.h` header.

### Mixing of Macros and Enums in libclips_ns
Another issue is the mixing of typedef and enums when working with the namespaced version of the library.
Looking at this snippet from `constant.h`:
```c++
typedef enum
  {
   FLOAT_BIT = (1 << 0),
   INTEGER_BIT = (1 << 1),
   // ...
  } CLIPSType;

#define NUMBER_BITS (INTEGER_BIT | FLOAT_BIT)
```
With namespace wrapping, the "unscoped" enum requires the usage of a namespace to reference the values, e.g., `clips::FLOAT_BIT`.
However, the macro `NUMBER_BITS` expands to just `(INTEGER_BIT | FLOAT_BIT)` which is only valid when the expansion is wrapped in the namespace

In this scenario it is necessary to use `using namespace clips;` before using the `NUMBER_BITS`. In particular, `clips::NUMBER_BITS` is **not** valid, neither is just using `NUMBER_BITS` without having declared the usage of namespace clips.
