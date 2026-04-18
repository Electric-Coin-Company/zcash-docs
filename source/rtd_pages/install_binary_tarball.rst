:orphan:

.. _install-binary-tarball-guide:

Binary Tarball Download & Setup
===============================

The Electric Coin Company provides a binary tarball for download.

As of v6.12.1, We are no longer supporting Debian 10(Buster) packages in apt.

`Download Tarball for Debian Bullseye v6.12.1 <https://download.z.cash/downloads/zcash-6.12.1-linux64-debian-bullseye.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Bullseye:

.. code-block:: bash

   sha256sum zcash-6.12.1-linux64-debian-bullseye.tar.gz

Result: ``62c4b44cfee86db341d55d7c0b553c3fe84f43a47170a5b5728b7314115c52fc``

`Download Tarball for Debian Bookworm v6.12.1 <https://download.z.cash/downloads/zcash-6.12.1-linux64-debian-bookworm.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Bookworm:

.. code-block:: bash

   sha256sum zcash-6.12.1-linux64-debian-bookworm.tar.gz

Result: ``15110f45ce64ba2eaf1635080158c24ff8d8903e813c51da6655fd56f44a1a4f``

This checksum was generated from our gitian deterministic build process. `View all gitian signatures <https://github.com/zcash/gitian.sigs/tree/master>`_.

Once you've verified that it matches, extract the Bullseye or Bookworm files and move the binaries into your executables $PATH: 

.. code-block:: bash

    tar -xvf zcash-6.12.1-linux64-debian-Bookworm.tar.gz

    mv -t /usr/local/bin/ zcash-6.12.1/bin/*

Now that Zcash is installed, run this command to download the parameters used to create and verify shielded transactions:

.. code-block:: bash 

    zcash-fetch-params

Finally, `set up a configuration file <https://zcash.readthedocs.io/en/latest/rtd_pages/zcash_conf_guide.html>`_ (`~/.zcash/zcash.conf`) before runnning zcashd. It can be completely empty; it will then run with the default parameters.
