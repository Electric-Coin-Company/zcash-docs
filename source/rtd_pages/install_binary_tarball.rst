:orphan:

.. _install-binary-tarball-guide:

Binary Tarball Download & Setup
===============================

The Electric Coin Company provides a binary tarball for download.

As of v4.7.0, we are no longer supporting Debian 9(Stretch) packages in apt.

`Download Tarball for Debian Buster v4.7.0 <https://z.cash/downloads/zcash-4.7.0-linux64-debian-buster.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Buster:

.. code-block:: bash

   sha256sum zcash-4.7.0-linux64-debian-buster.tar.gz

Result: ``d27064e75ca21a807e4a47693f313c612ebfc9a03abc08f0e02f9d6105d15831``

`Download Tarball for Debian Bullseye v4.7.0 <https://z.cash/downloads/zcash-4.7.0-linux64-debian-bullseye.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Bullseye:

.. code-block:: bash

   sha256sum zcash-4.7.0-linux64-debian-bullseye.tar.gz

Result: ``95ab70cd6d7d3d6f89c834468dc7d8daf6549ef361aa506a14bc2d4e2275d0b0``

This checksum was generated from our gitian deterministic build process. `View all gitian signatures <https://github.com/zcash/gitian.sigs/tree/master>`_.

Once you've verified that it matches, extract the Buster or Bullseye files and move the binaries into your executables $PATH: 

.. code-block:: bash

    tar -xvf zcash-4.7.0-linux64-debian-buster.tar.gz

    mv -t /usr/local/bin/ zcash-4.7.0/bin/*

Now that Zcash is installed, run this command to download the parameters used to create and verify shielded transactions:

.. code-block:: bash 

    zcash-fetch-params

Finally, `set up a configuration file <https://zcash.readthedocs.io/en/latest/rtd_pages/zcash_conf_guide.html>`_ (`~/.zcash/zcash.conf`) before runnning zcashd. It can be completely empty; it will then run with the default parameters.
