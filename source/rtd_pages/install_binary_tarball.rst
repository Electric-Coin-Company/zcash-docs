:orphan:

.. _install-binary-tarball-guide:

Binary Tarball Download & Setup
===============================

The Electric Coin Company provides a binary tarball for download.

As of v6.12.0, We are no longer supporting Debian 10(Buster) packages in apt.

`Download Tarball for Debian Bullseye v6.12.0 <https://download.z.cash/downloads/zcash-6.12.0-linux64-debian-bullseye.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Bullseye:

.. code-block:: bash

   sha256sum zcash-6.12.0-linux64-debian-bullseye.tar.gz

Result: ``9ae25da27b185b6fa016f5005dca39203629b763e7ec1b5f389cd3f5acb3e9c4``

`Download Tarball for Debian Bookworm v6.12.0 <https://download.z.cash/downloads/zcash-6.12.0-linux64-debian-bookworm.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Bookworm:

.. code-block:: bash

   sha256sum zcash-6.12.0-linux64-debian-bookworm.tar.gz

Result: ``a4c98f051e5053c144df8e1a9b55a6775025d2dffb3b9684dad1f3aef68a4aa9``

This checksum was generated from our gitian deterministic build process. `View all gitian signatures <https://github.com/zcash/gitian.sigs/tree/master>`_.

Once you've verified that it matches, extract the Bullseye or Bookworm files and move the binaries into your executables $PATH: 

.. code-block:: bash

    tar -xvf zcash-6.12.0-linux64-debian-Bookworm.tar.gz

    mv -t /usr/local/bin/ zcash-6.12.0/bin/*

Now that Zcash is installed, run this command to download the parameters used to create and verify shielded transactions:

.. code-block:: bash 

    zcash-fetch-params

Finally, `set up a configuration file <https://zcash.readthedocs.io/en/latest/rtd_pages/zcash_conf_guide.html>`_ (`~/.zcash/zcash.conf`) before runnning zcashd. It can be completely empty; it will then run with the default parameters.
