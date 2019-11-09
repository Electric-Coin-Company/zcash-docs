:orphan:

.. _install-binary-tarball-guide:

Binary Tarball Download & Setup
===============================

The Electric Coin Company provides a binary tarball for download.

`Download Tarball for Debian Jessie v2.1.0-1 <https://z.cash/downloads/zcash-2.1.0-1-linux64-jessie.tar.gz>`_

`Download Tarball for Debian Stretch v2.1.0-1 <https://z.cash/downloads/zcash-2.1.0-1-linux64-stretch.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Jessie:

.. code-block:: bash

   sha256sum zcash-2.1.0-1-linux64-jessie.tar.gz

Result: ``ca79de0f6e37060e3abccebae6a4336f7a3017099078b05fd1eb12dc4ffd9b43``

Debian Stretch:

.. code-block:: bash

   sha256sum zcash-2.1.0-1-linux64-stretch.tar.gz

Result: ``aec6b3c4178c5ceb4e7b7ed3aaa96078b88b872640c7bb38208d5bce48e3f75c``

This checksum was generated from our gitian deterministic build process. `View all gitian signatures <https://github.com/zcash/gitian.sigs/tree/master>`_.

Once you've verified that it matches, extract the files and move the binaries into your executables $PATH: 

.. code-block:: bash

    tar -xvf zcash-2.1.0-1-linux64.tar.gz

    mv -t /usr/local/bin/ zcash-2.1.0-1/bin/* 

Now that Zcash is installed, run this command to download the parameters used to create and verify shielded transactions:

.. code-block:: bash 

    zcash-fetch-params

Finally, set up ``~/.zcash/zcash.conf`` before running Zcash as your local user, as documented in the :ref:`user_guide`. 
