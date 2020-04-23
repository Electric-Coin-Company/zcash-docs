:orphan:

.. _install-binary-tarball-guide:

Binary Tarball Download & Setup
===============================

The Electric Coin Company provides a binary tarball for download.

`Download Tarball for Debian Jessie v2.1.2 <https://z.cash/downloads/zcash-2.1.2-linux64-debian-jessie.tar.gz>`_

`Download Tarball for Debian Stretch v2.1.2 <https://z.cash/downloads/zcash-2.1.2-linux64-debian-stretch.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Jessie:

.. code-block:: bash

   sha256sum zcash-2.1.2-linux64-debian-jessie.tar.gz

Result: ``f4333515b7c01102e66a3bee6d00661cf9af8e0304250a6845a753464ffca137``

Debian Stretch:

.. code-block:: bash

   sha256sum zcash-2.1.2-linux64-debian-stretch.tar.gz

Result: ``e9cea9fc252d12444b30fa9a66aeb8375845ec11764ecc52b56f31e5c61b775c``

This checksum was generated from our gitian deterministic build process. `View all gitian signatures <https://github.com/zcash/gitian.sigs/tree/master>`_.

Once you've verified that it matches, extract the files and move the binaries into your executables $PATH: 

.. code-block:: bash

    tar -xvf zcash-2.1.2-linux64.tar.gz

    mv -t /usr/local/bin/ zcash-2.1.2/bin/* 

Now that Zcash is installed, run this command to download the parameters used to create and verify shielded transactions:

.. code-block:: bash 

    zcash-fetch-params

Finally, set up ``~/.zcash/zcash.conf`` before running Zcash as your local user, as documented in the :ref:`user_guide`. 
