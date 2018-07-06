.. _supported_platform_policy:

Supported Platform Policy
=========================

Our supported platforms policy is as follows, largely inspired by the `Tahoe-LAFS buildbot policy <https://tahoe-lafs.org/trac/tahoe-lafs/wiki/BuildbotPolicy>`_

- A supported platform must have a buildbot builder which builds and runs all tests.
- A buildbot builder uses the 'default' or 'standard' configuration for its platform, 
  and if we need something substantially different, we call that something different. 
  Examples include default file systems, default compilers, default kernels, etc…
- If build/testing for a supported platform fails, this blocks progress on all platforms.
  #. If the merge-acceptance test suite fails only on osx, but not other platforms, a merge should fail.
  #. If the pre-release test suite fails only on debian, the release is blocked on all platforms.
- Furthermore, for pre-release testing, we should run tests of candidate packages on default 
  systems which don't even have developer tools, unless those tools come by default on that platform.
- For platforms which have frequent updates, such as *debian testing*, we should upgrade all installed 
  packages on the builders during each `CI deployment`.

By contrast `unsupported platforms` do not block progress. These may still have buildbot builders, 
partial test suites. Unsupported platforms should still use default configurations, or be appropriately named to distinguish their uniqueness.
