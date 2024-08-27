:orphan:

.. _install-binary-tarball-guide:

Binary Tarball Download & Setup
===============================

The Electric Coin Company provides a binary tarball for download.

As of v5.10.0, We are no longer supporting Debian 10(Buster) packages in apt.

`Download Tarball for Debian Bullseye v5.10.0 <https://download.z.cash/downloads/zcash-5.10.0-linux64-debian-bullseye.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Bullseye:

.. code-block:: bash

   sha256sum zcash-5.10.0-linux64-debian-bullseye.tar.gz

Result: ``72d06e97bab29b2a21fc52637485840335fd7fff3f5f06ad9f66c326d3f7ca1f``

`Download Tarball for Debian Bookworm v5.10.0 <https://download.z.cash/downloads/zcash-5.10.0-linux64-debian-bookworm.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Bookworm:

.. code-block:: bash

   sha256sum zcash-5.10.0-linux64-debian-bookworm.tar.gz

Result: ``911e0fdc5c7eee412dda2f7557df9c0827bc5a4b6e369cd0177a47e566b5fdb4``

This checksum was generated from our gitian deterministic build process. `View all gitian signatures <https://github.com/zcash/gitian.sigs/tree/master>`_.

Once you've verified that it matches, extract the Bullseye or Bookworm files and move the binaries into your executables $PATH: 

.. code-block:: bash

    tar -xvf zcash-5.10.0-linux64-debian-Bookworm.tar.gz

    mv -t /usr/local/bin/ zcash-5.10.0/bin/*

Now that Zcash is installed, run this command to download the parameters used to create and verify shielded transactions:

.. code-block:: bash 

    zcash-fetch-params

Finally, `set up a configuration file <https://zcash.readthedocs.io/en/latest/rtd_pages/zcash_conf_guide.html>`_ (`~/.zcash/zcash.conf`) before runnning zcashd. It can be completely empty; it will then run with the default parameters.
