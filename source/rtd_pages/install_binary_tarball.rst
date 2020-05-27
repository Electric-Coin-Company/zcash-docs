:orphan:

.. _install-binary-tarball-guide:

Binary Tarball Download & Setup
===============================

The Electric Coin Company provides a binary tarball for download.

`Download Tarball for Debian Jessie v3.0.0 <https://z.cash/downloads/zcash-3.0.0-linux64-debian-jessie.tar.gz>`_

`Download Tarball for Debian Stretch v3.0.0 <https://z.cash/downloads/zcash-3.0.0-linux64-debian-stretch.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Jessie:

.. code-block:: bash

   sha256sum zcash-3.0.0-linux64-debian-jessie.tar.gz

Result: ``9810140c3395467a13154ce852c64b144b7450329031fbed018a730b6a65c930``

Debian Stretch:

.. code-block:: bash

   sha256sum zcash-3.0.0-linux64-debian-stretch.tar.gz

Result: ``d8adc5ca1f7dec5ffc8c012fa765aa54ea371e4895c45ec927eeb465e5581e28``

This checksum was generated from our gitian deterministic build process. `View all gitian signatures <https://github.com/zcash/gitian.sigs/tree/master>`_.

Once you've verified that it matches, extract the files and move the binaries into your executables $PATH: 

.. code-block:: bash

    tar -xvf zcash-3.0.0-linux64.tar.gz

    mv -t /usr/local/bin/ zcash-3.0.0/bin/* 

Now that Zcash is installed, run this command to download the parameters used to create and verify shielded transactions:

.. code-block:: bash 

    zcash-fetch-params

Finally, set up ``~/.zcash/zcash.conf`` before running Zcash as your local user, as documented in the :ref:`user_guide`. 
