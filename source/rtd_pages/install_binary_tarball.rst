:orphan:

.. _install-binary-tarball-guide:

Binary Tarball Download & Setup
===============================

The Electric Coin Company provides a binary tarball for download.

As of v5.0.0, We are no longer supporting Debian 9(Stretch) packages in apt.

`Download Tarball for Debian Buster v5.8.0 <https://download.z.cash/downloads/zcash-5.8.0-linux64-debian-buster.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Buster:

.. code-block:: bash

   sha256sum zcash-5.8.0-linux64-debian-buster.tar.gz

Result: ``7a63b8f8a2aefc7b634cc3e572103600f4af8c383bd90ca1d333870ddaa004ef``

`Download Tarball for Debian Bullseye v5.8.0 <https://download.z.cash/downloads/zcash-5.8.0-linux64-debian-bullseye.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Bullseye:

.. code-block:: bash

   sha256sum zcash-5.8.0-linux64-debian-bullseye.tar.gz

Result: ``d385b9fbeeb145f60b0b339d256cabb342713ed3014cd634cf2d68078365abd2``

This checksum was generated from our gitian deterministic build process. `View all gitian signatures <https://github.com/zcash/gitian.sigs/tree/master>`_.

Once you've verified that it matches, extract the Buster or Bullseye files and move the binaries into your executables $PATH: 

.. code-block:: bash

    tar -xvf zcash-5.8.0-linux64-debian-buster.tar.gz

    mv -t /usr/local/bin/ zcash-5.8.0/bin/*

Now that Zcash is installed, run this command to download the parameters used to create and verify shielded transactions:

.. code-block:: bash 

    zcash-fetch-params

Finally, `set up a configuration file <https://zcash.readthedocs.io/en/latest/rtd_pages/zcash_conf_guide.html>`_ (`~/.zcash/zcash.conf`) before runnning zcashd. It can be completely empty; it will then run with the default parameters.
