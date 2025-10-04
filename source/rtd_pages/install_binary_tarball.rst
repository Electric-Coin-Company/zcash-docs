:orphan:

.. _install-binary-tarball-guide:

Binary Tarball Download & Setup
===============================

The Electric Coin Company provides a binary tarball for download.

As of v6.10.0, We are no longer supporting Debian 10(Buster) packages in apt.

`Download Tarball for Debian Bullseye v6.10.0 <https://download.z.cash/downloads/zcash-6.10.0-linux64-debian-bullseye.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Bullseye:

.. code-block:: bash

   sha256sum zcash-6.10.0-linux64-debian-bullseye.tar.gz

Result: ``4c59f3a83f61c01f753b653c2780b3dfb9f65af93a7815ff6bd784c326f773e8``

`Download Tarball for Debian Bookworm v6.10.0 <https://download.z.cash/downloads/zcash-6.10.0-linux64-debian-bookworm.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Bookworm:

.. code-block:: bash

   sha256sum zcash-6.10.0-linux64-debian-bookworm.tar.gz

Result: ``1ffae22571924ed4e7129c9e85b28a2e62f47cbaa26a9f9dfe096b510a6c8f37``

This checksum was generated from our gitian deterministic build process. `View all gitian signatures <https://github.com/zcash/gitian.sigs/tree/master>`_.

Once you've verified that it matches, extract the Bullseye or Bookworm files and move the binaries into your executables $PATH: 

.. code-block:: bash

    tar -xvf zcash-6.10.0-linux64-debian-Bookworm.tar.gz

    mv -t /usr/local/bin/ zcash-6.10.0/bin/*

Now that Zcash is installed, run this command to download the parameters used to create and verify shielded transactions:

.. code-block:: bash 

    zcash-fetch-params

Finally, `set up a configuration file <https://zcash.readthedocs.io/en/latest/rtd_pages/zcash_conf_guide.html>`_ (`~/.zcash/zcash.conf`) before runnning zcashd. It can be completely empty; it will then run with the default parameters.
