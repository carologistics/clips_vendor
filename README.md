# clips_vendor
Wrapper around clips (https://clipsrules.net/) for usage with ROS 2.
Replaces the make-based original build system by cmake and builds dynamic
libraries for flexible usage.

Contains core implementation, clipsjni applications and demos as well as the 
given examples from the svn source repository 
(https://sourceforge.net/p/clipsrules/code/HEAD/tree/).

Note that clips can be both compiled with c and c++.
Here, the main application and library (libclips.so) is built using c++.
A c shared library is also provided (and used by the clipsjni applications).

# Usage

find_package(clips_vendor)
find_package(clips)

target_link_libraries(<target> PUBLIC Clips::libclips)
target_link_libraries(<target> PUBLIC ClipsC::libclips_c)
target_link_libraries(<target> PUBLIC ClipsNS::libclips_ns)


# A word of Caution

Inside of CLIPS headers there are a few #define macros that might mess with other libraries.

Known instances are: LHS and RHS which can interfere with template identifiers in boost/function_types/property_tags.hpp.
In these cases, undefine the macros after including the clips.h header.

Another issue is the mixing of typedef and enums when working with the namespaced version of cthe library.
e.g. clips::STRING_BIT is used to get the string bit, but ANY_TYPE_BITS is a typedef expanding to STRING_BIT | VOID_BIT ... which therefore breaks consistency.
In this scenario it is {using namespace clips ANY_TYPE_BITS
}
