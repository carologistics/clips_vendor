^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package clips_vendor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

6.4.3 (2024-11-21)
------------------
* CMakeLists: fetch zip from github
  Soruceforge snapshots are created on-demand and downloading through
  CMake will fail if the snapshot is not existing already.
  these snapshots are also not persistent and are deleted regularly.
  Hence downloading directly from sourceforge is not working reliably.
  To prevent the issue just store the snapshot on github.
  We could instead pull the changes from the latest available download,
  but this has no clear revision attached to it and is also not kept
  up-to-date.
* buildsys: patch missing char *cast
* project: switch from svn to source zip
* package.xml: add Tim as second maintainer to prepare release
* license: clear up distinction between source and vendor package license
  As per the discussion of https://github.com/ros/rosdistro/pull/43450.
  Also, update the version to reflect the added license.txt, see:
  https://sourceforge.net/p/clipsrules/discussion/776945/thread/f3176d3efe/#e913
* patches: compile libclips with c++ and offer separate libclips_c for c
* project: add initial commit for a clips vendor package using cmake
  The idea is to use the svn source and patch it to a cmake buildsys which
  then can be seamlessly used with ament_vendor().
  The original buildsys is just plain make with in-source builds and
  without proper shared libraries.
  Hence quite a bit of work is required to modernize the clips buildsys.
  Currently this build uses the svn directly, but does not fix any commit
  version, which should be fixed to specific releases in the future.
* Contributors: Tarik Viehmann, Tim Wendt
