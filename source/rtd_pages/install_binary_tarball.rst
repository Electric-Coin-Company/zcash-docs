:orphan:

.. _install-binary-tarball-guide:

Binary Tarball Download & Setup
===============================

The Electric Coin Company provides a binary tarball for download.

`Download Tarball for Debian Jessie v2.1.1 <https://z.cash/downloads/zcash-2.1.1-linux64-debian-jessie.tar.gz>`_

`Download Tarball for Debian Stretch v2.1.1 <https://z.cash/downloads/zcash-2.1.1-linux64-debian-stretch.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Jessie:

.. code-block:: bash

   sha256sum zcash-2.1.1-linux64-debian-jessie.tar.gz

Result: ``ced046653b21820f490fa51cef280dec86e77ac9c005b8f52eda87439415f52e``

Debian Stretch:

.. code-block:: bash

   sha256sum zcash-2.1.1-linux64-debian-stretch.tar.gz

Result: ``d18e60d9762847a6038d3d2259d84a24cbf83793a08372beaaae1479ef244f03``

This checksum was generated from our gitian deterministic build process. `View all gitian signatures <https://github.com/zcash/gitian.sigs/tree/master>`_.

Once you've verified that it matches, extract the files and move the binaries into your executables $PATH: 

.. code-block:: bash

    tar -xvf zcash-2.1.1-linux64.tar.gz

    mv -t /usr/local/bin/ zcash-2.1.1/bin/* 

Now that Zcash is installed, run this command to download the parameters used to create and verify shielded transactions:

.. code-block:: bash 

    zcash-fetch-params

Finally, set up ``~/.zcash/zcash.conf`` before running Zcash as your local user, as documented in the :ref:`user_guide`. 
