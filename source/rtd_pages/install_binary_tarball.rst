:orphan:

.. _install-binary-tarball-guide:

Binary Tarball Download & Setup
===============================

The Electric Coin Company provides a binary tarball for download.

`Download Tarball for Debian Jessie v2.1.1-1 <https://z.cash/downloads/zcash-2.1.1-1-linux64-debian-jessie.tar.gz>`_

`Download Tarball for Debian Stretch v2.1.1-1 <https://z.cash/downloads/zcash-2.1.1-1-linux64-debian-stretch.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Jessie:

.. code-block:: bash

   sha256sum zcash-2.1.1-1-linux64-debian-jessie.tar.gz

Result: ``d2694b312521cb3c22d2ef46dcbf72fb6d2102e2b5609cf37d23543228d976d1``

Debian Stretch:

.. code-block:: bash

   sha256sum zcash-2.1.1-1-linux64-debian-stretch.tar.gz

Result: ``15780d5b34cc0f9536d85d7c424b9788327e0881d0c503ef9f8dc277b2e2a4ff``

This checksum was generated from our gitian deterministic build process. `View all gitian signatures <https://github.com/zcash/gitian.sigs/tree/master>`_.

Once you've verified that it matches, extract the files and move the binaries into your executables $PATH: 

.. code-block:: bash

    tar -xvf zcash-2.1.1-1-linux64.tar.gz

    mv -t /usr/local/bin/ zcash-2.1.1-1/bin/* 

Now that Zcash is installed, run this command to download the parameters used to create and verify shielded transactions:

.. code-block:: bash 

    zcash-fetch-params

Finally, set up ``~/.zcash/zcash.conf`` before running Zcash as your local user, as documented in the :ref:`user_guide`. 
