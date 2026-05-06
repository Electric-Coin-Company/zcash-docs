:orphan:

.. _install-binary-tarball-guide:

Binary Tarball Download & Setup
===============================

The Zcash Open Development Lab (ZODL) provides a binary tarball for download.

As of v6.12.1, we are no longer supporting Debian 10 (Buster) packages in apt.

.. warning::

   **Signing key rotation (2026).** Starting with v6.12.2, release artifacts
   (tarballs and the APT ``Release.gpg``) are signed **only** with the ZODL
   key. The previous ECC key (``B1C9 095E AA18 48DB B54D 9DDA 1D05 FDC6 6B37
   2CFE``, ``sysadmin@z.cash``) is deprecated and its revocation is planned
   for 2026-06-23. If you verified earlier releases with the ECC key, make
   sure to also import the ZODL key before verifying v6.12.2+. See
   `Rotation of the signing keys announcement
   <https://forum.zcashcommunity.com/t/rotation-of-the-signing-keys-for-zcashd-zallet-and-standalone-android-binaries-for-zodl/55144>`_
   on the Zcash Community Forum.

Importing the ZODL signing key
------------------------------

The ZODL key (``sysadmin@zodl.com``) is:

``Key fingerprint = 0338 34DD 49DE CF9D BB99 34BC 6C93 CA8E 58E2 6AB1``

Import it with:

.. code-block:: bash

   wget -qO - https://apt.z.cash/zcash.asc | gpg --import

The combined keyring served at ``https://apt.z.cash/zcash.asc`` contains both
the legacy ECC key (for verifying older releases) and the ZODL key (required
for v6.12.2+).

Downloading and verifying the v6.12.2 tarball
---------------------------------------------

`Download Tarball for Debian Bullseye v6.12.2 <https://download.z.cash/downloads/zcash-6.12.2-linux64-debian-bullseye.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Bullseye:

.. code-block:: bash

   sha256sum zcash-6.12.2-linux64-debian-bullseye.tar.gz

Result: ``c355250cba203835c58400821df7b2786d660affdf6a7a6d9070695c05002df2``

`Download Tarball for Debian Bookworm v6.12.2 <https://download.z.cash/downloads/zcash-6.12.2-linux64-debian-bookworm.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Bookworm:

.. code-block:: bash

   sha256sum zcash-6.12.2-linux64-debian-bookworm.tar.gz

Result: ``75947c7df86fb3b4e3d7ff268077806272b5da5742959e13c3d6995e5c2059e0``

This checksum was generated from our gitian deterministic build process. `View all gitian signatures <https://github.com/zcash/gitian.sigs/tree/master>`_.

Optionally, you can also verify the detached GPG signature published alongside each tarball (signed with the ZODL key):

.. code-block:: bash

   wget https://download.z.cash/downloads/zcash-6.12.2-linux64-debian-bullseye.tar.gz.asc
   gpg --verify zcash-6.12.2-linux64-debian-bullseye.tar.gz.asc \
                zcash-6.12.2-linux64-debian-bullseye.tar.gz

You should see ``Good signature from "Zcash Open Development Lab (ZODL) …
<sysadmin@zodl.com>"``.

Once you've verified that it matches, extract the Bullseye or Bookworm files and move the binaries into your executables $PATH:

.. code-block:: bash

    tar -xvf zcash-6.12.2-linux64-debian-bookworm.tar.gz

    mv -t /usr/local/bin/ zcash-6.12.2/bin/*

Now that Zcash is installed, run this command to download the parameters used to create and verify shielded transactions:

.. code-block:: bash

    zcash-fetch-params

Finally, `set up a configuration file <https://zcash.readthedocs.io/en/latest/rtd_pages/zcash_conf_guide.html>`_ (`~/.zcash/zcash.conf`) before runnning zcashd. It can be completely empty; it will then run with the default parameters.
