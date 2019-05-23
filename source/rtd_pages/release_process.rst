.. _release_process:

Release Process 
===============

Roles 
-----

- Product Manager: Responsible for defining the priority of features and bugfixes for upcoming releases. Works with 
  the Release Manager to make tradeoffs if needed and keeps Scrum of Scrums up to date on the current release content 
  and future roadmap.

- Release Manager: Responsible for ensuring target features and bugfixes are in the release and all quality and 
  security guidelines are met. Responsible for writing the draft of release notes and delivering it to the Comms Lead
  and delivering a git revision to the Binary Shepherd.

- Binary Shepherd: Does all technical processes to produce a signed source release and signed installable packages. 
  Does not write any copy or make decisions about release scope/schedule. Notifies the Release Manager and 
  Release Comms that the release is published.

- Release Comms: Reviews release notes and prepares and publishes the blog post when notified by the Binary Shepherd 
  that the release is live; follows up with community outreach about the release. Ensures the new binary is on the website.

- Documentation Shepherd: Ensures there exists documentation explaining new features for the given release and these 
  are ready to deploy to RTD once the release is finalized.

Process
-------

1. 6 weeks before release: Product Manager and Release Manager agree to target date and targeted features and bugfixes 
   for the next release. Ensure that this is synchronized with any light client or Insight updates if needed.
2. 6 weeks before release: Release Manager makes a copy of the Regular Release Smoke Tests Template, renames it 
   for the upcoming release and ensures engineers know it's there so they can add the PRs included in the release 
   to it, with associated testing plans if needed.

   - A majority of existing smoke tests are automated, see https://github.com/zcash/zcash/pull/3913 
     (NOTE: As of 5/21/2019, these are not apart of CI. They need to be run independently from CI tests)
   - New features likely need to have manual tests added(section 8 of Regular Release Smoke Tests Template), 
     to ensure they operate as expected. Ideally, these need to become automated, if possible, to ensure 
     regression tests continue to test these same scenarios in future releases.
3. Release Manager and Product Manager frequently communicate about expected timelines and in scope targeted features and bugfixes.

4. 1.5 weeks before release (the last day of the last full sprint before the release, which is a Thursday): Release Manager does a final check that:

  - All tickets with security and documentation requirement labels have fulfilled their requirements (Cross verify with Documentation Shepherd )
  - Ticket gardening for current milestone
    - Ensure all goals for the Github milestone are met. If not, remove tickets or PRs with a comment as to why it is not included.
  - Check depends are properly hosted by looking at the check-depends builder:
    - https://ci.z.cash/#/builders/
  - Check that there are no surprising performance regressions
    - https://speed.z.cash
  - Update src/chainparams.cpp nMinimumChainWork with information from the getblockchaininfo rpc.
  - Update the fields for EOL (add a note to the upcoming release notes with this field)
  - Protocol Safety Checks:

    - If this release changes the behavior of the protocol or fixes a serious bug, verify that a 
      pre-release PR merge updated PROTOCOL_VERSION in version.h correctly.
    - If this release breaks backwards compatibility or needs to prevent interaction with software 
      forked projects, change the network magic numbers. Set the four pchMessageStart in CTestNetParams in chainparams.cpp to random values.
    - Both of these should be done in standard PRs ahead of the release process. If these 
      were not anticipated correctly, this could block the release, so if you suspect this 
      is necessary, double check with the whole engineering team.

  - All GitHub release notes are completed - Release Manager may need to condense these for Release Comms
  - Block Explorer updates have been completed (if needed)
  - Light Client updates have been completed (if needed)

5. 1 week before release:

  - Release Manager ensures all PRs have been merged with appropriate documentation/notes/etc.
  - Release Manager creates and tags a Release Candidate (RC) using make-release.py 
    (NOTE: The RC does NOT require the Binary Shepherd. People are expected to simply pull on tags(https://github.com/zcash/zcash/tags) from Github, not use apt-get)
  - Release Manager completes release announcement/blog post draft and notifies Release Comms 
    of upcoming RC. (NOTE: RCs do NOT need formal Github release notes, see https://github.com/zcash/zcash/releases)
  - Release Comms reviews blog post for release.
  - Team performs RC testing, see Regular Release Smoke Tests Template for the given release version.
    - Automated smoke test can take quite some time (~8 hours)
    - Manual smoke tests can vary (e.g. hours or days depending on difficulty of test)
    - If the testing fails, go back to step 3, else, proceed to the next step

6. Day of release:

   - Binary Shepherd does the following:
     https://github.com/Electric-Coin-Company/infrastructure/wiki/How-to-do-a-release
   - Ensure this page is up to date with the latest release info https://z.cash/support/schedule/
     - Git repo: https://github.com/Electric-Coin-Company/zcash-release-scheduling

   - Update testnet.z.cash and mainnet.z.cash hosts
     - These hosts are managed from this project: https://github.com/Electric-Coin-Company/infrastructure
     - sudo apt-get update && sudo apt-get install zcash
     - then restart zcash systemctl restart zcashd
   - Update detector hosts
     - These hosts are managed from the infrastructure project
     - More info about the detectors here: https://github.com/Electric-Coin-Company/infrastructure/wiki/Zcash-Monitoring#detectors
     - Detectors 7, 6, 5 run latest version
     - Detectors 4, 3 run previous version
     - Detectors 1, 2 run version that's 2 releases behind.
   - Documentation Shepard update Zcash Read the Docs
     - Increment versions in RST source

       - This will also update the download link https://z.cash/downloads/zcash-2.0.5-2-linux64.tar.gz

     - Update SHA for apt-get Debain page (https://zcash.readthedocs.io/en/latest/rtd_pages/install_debian_bin_packages.html)
     - Tag this version to be consistent with the zcash release version
     - Verify website has up to date docs to announce release/deploy
   - Release Manager
     - Publish drafted Github release notes, see Release Manager Release Process to ensure all items are complete
   - Release Comms 
     - Publish the release announcement (blog, zcash-dev, rocket chat, slack)

Note: releases are not done on Friday, only on Monday-Thursday.