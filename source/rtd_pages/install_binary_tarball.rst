:orphan:

.. _install-binary-tarball-guide:

Binary Tarball Download & Setup
===============================

The Electric Coin Company provides a binary tarball for download.

`Download Tarball for Debian Jessie v2.1.0 <https://z.cash/downloads/zcash-2.1.0-linux64-jessie.tar.gz>`_

`Download Tarball for Debian Stretch v2.1.0 <https://z.cash/downloads/zcash-2.1.0-linux64-stretch.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Jessie:

.. code-block:: bash

   sha256sum zcash-2.1.0-linux64-jessie.tar.gz

Result: ``385720e8b9d430a54d497021491bbe65d0da5cb3e6819769a6f7481e59489f15``

Debian Stretch:

.. code-block:: bash

   sha256sum zcash-2.1.0-linux64-stretch.tar.gz

Result: ``9bb4db21fee0dbce45ef2e4e7c0752c3827dc7c7117b8e4cec673c201dbce3cf``

This checksum was generated from our gitian deterministic build process. `View all gitian signatures <https://github.com/zcash/gitian.sigs/tree/master>`_.

Once you've verified that it matches, extract the files and move the binaries into your executables $PATH: 

.. code-block:: bash

    tar -xvf zcash-2.1.0-linux64.tar.gz

    mv -t /usr/local/bin/ zcash-2.1.0/bin/* 

Now that Zcash is installed, run this command to download the parameters used to create and verify shielded transactions:

.. code-block:: bash 

    zcash-fetch-params

Finally, set up ``~/.zcash/zcash.conf`` before running Zcash as your local user, as documented in the :ref:`user_guide`. 
