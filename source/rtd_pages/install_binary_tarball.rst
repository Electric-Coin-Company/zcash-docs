:orphan:

.. _install-binary-tarball-guide:

Binary Tarball Download & Setup
===============================

The Electric Coin Company provides a binary tarball for download.

As of v5.0.0, We are no longer supporting Debian 9(Stretch) packages in apt.

`Download Tarball for Debian Buster v5.6.1 <https://z.cash/downloads/zcash-5.6.1-linux64-debian-buster.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Buster:

.. code-block:: bash

   sha256sum zcash-5.6.1-linux64-debian-buster.tar.gz

Result: ``ae4b8fbb49fa7b6a8a5f498103b267ba9fdd9e694b26a40a100596265ca1329b``

`Download Tarball for Debian Bullseye v5.6.1 <https://z.cash/downloads/zcash-5.6.1-linux64-debian-bullseye.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Bullseye:

.. code-block:: bash

   sha256sum zcash-5.6.1-linux64-debian-bullseye.tar.gz

Result: ``0144cc75f00460b136103eeb7c629d5af8101d52b9a77524f44305d44cfbc795``

This checksum was generated from our gitian deterministic build process. `View all gitian signatures <https://github.com/zcash/gitian.sigs/tree/master>`_.

Once you've verified that it matches, extract the Buster or Bullseye files and move the binaries into your executables $PATH: 

.. code-block:: bash

    tar -xvf zcash-5.6.1-linux64-debian-buster.tar.gz

    mv -t /usr/local/bin/ zcash-5.6.1/bin/*

Now that Zcash is installed, run this command to download the parameters used to create and verify shielded transactions:

.. code-block:: bash 

    zcash-fetch-params

Finally, `set up a configuration file <https://zcash.readthedocs.io/en/latest/rtd_pages/zcash_conf_guide.html>`_ (`~/.zcash/zcash.conf`) before runnning zcashd. It can be completely empty; it will then run with the default parameters.
