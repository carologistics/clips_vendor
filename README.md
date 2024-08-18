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
