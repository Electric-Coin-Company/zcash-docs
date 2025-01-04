:orphan:

.. _install-binary-tarball-guide:

Binary Tarball Download & Setup
===============================

The Electric Coin Company provides a binary tarball for download.

As of v6.1.0, We are no longer supporting Debian 10(Buster) packages in apt.

`Download Tarball for Debian Bullseye v6.1.0 <https://download.z.cash/downloads/zcash-6.1.0-linux64-debian-bullseye.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Bullseye:

.. code-block:: bash

   sha256sum zcash-6.1.0-linux64-debian-bullseye.tar.gz

Result: ``1d17ceacb265599bb4ee690baaf2b335cfe9825df5198359c771ee1834fd4358``

`Download Tarball for Debian Bookworm v6.1.0 <https://download.z.cash/downloads/zcash-6.1.0-linux64-debian-bookworm.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Bookworm:

.. code-block:: bash

   sha256sum zcash-6.1.0-linux64-debian-bookworm.tar.gz

Result: ``3612f351e39be6a94bbf298f238e2b98c3050e72b8641b61615d6019479b7595``

This checksum was generated from our gitian deterministic build process. `View all gitian signatures <https://github.com/zcash/gitian.sigs/tree/master>`_.

Once you've verified that it matches, extract the Bullseye or Bookworm files and move the binaries into your executables $PATH: 

.. code-block:: bash

    tar -xvf zcash-6.1.0-linux64-debian-Bookworm.tar.gz

    mv -t /usr/local/bin/ zcash-6.1.0/bin/*

Now that Zcash is installed, run this command to download the parameters used to create and verify shielded transactions:

.. code-block:: bash 

    zcash-fetch-params

Finally, `set up a configuration file <https://zcash.readthedocs.io/en/latest/rtd_pages/zcash_conf_guide.html>`_ (`~/.zcash/zcash.conf`) before runnning zcashd. It can be completely empty; it will then run with the default parameters.
