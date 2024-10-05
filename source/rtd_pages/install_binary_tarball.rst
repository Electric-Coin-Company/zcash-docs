:orphan:

.. _install-binary-tarball-guide:

Binary Tarball Download & Setup
===============================

The Electric Coin Company provides a binary tarball for download.

As of v6.0.0, We are no longer supporting Debian 10(Buster) packages in apt.

`Download Tarball for Debian Bullseye v6.0.0 <https://download.z.cash/downloads/zcash-6.0.0-linux64-debian-bullseye.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Bullseye:

.. code-block:: bash

   sha256sum zcash-6.0.0-linux64-debian-bullseye.tar.gz

Result: ``3cb82f490e9c8e88007a0216b5261b33ef0fda962b9258441b2def59cb272a4d``

`Download Tarball for Debian Bookworm v6.0.0 <https://download.z.cash/downloads/zcash-6.0.0-linux64-debian-bookworm.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Bookworm:

.. code-block:: bash

   sha256sum zcash-6.0.0-linux64-debian-bookworm.tar.gz

Result: ``467c79e2f1431dd797010f0e5c2e8c009845fdaca0c7e1bf0b790f93f6c88c9d``

This checksum was generated from our gitian deterministic build process. `View all gitian signatures <https://github.com/zcash/gitian.sigs/tree/master>`_.

Once you've verified that it matches, extract the Bullseye or Bookworm files and move the binaries into your executables $PATH: 

.. code-block:: bash

    tar -xvf zcash-6.0.0-linux64-debian-Bookworm.tar.gz

    mv -t /usr/local/bin/ zcash-6.0.0/bin/*

Now that Zcash is installed, run this command to download the parameters used to create and verify shielded transactions:

.. code-block:: bash 

    zcash-fetch-params

Finally, `set up a configuration file <https://zcash.readthedocs.io/en/latest/rtd_pages/zcash_conf_guide.html>`_ (`~/.zcash/zcash.conf`) before runnning zcashd. It can be completely empty; it will then run with the default parameters.
