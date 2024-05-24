:orphan:

.. _install-binary-tarball-guide:

Binary Tarball Download & Setup
===============================

The Electric Coin Company provides a binary tarball for download.

As of v5.0.0, We are no longer supporting Debian 9(Stretch) packages in apt.

`Download Tarball for Debian Buster v5.9.1 <https://github.com/zcash/artifacts/raw/master/v5.9.1/buster/zcash-5.9.1-linux64-debian-buster.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Buster:

.. code-block:: bash

   sha256sum zcash-5.9.1-linux64-debian-buster.tar.gz

Result: ``df14aebdd9dcc8c9fd3b36e74adb8e4ce896a8349eb030eed3ca64132b678b94``

`Download Tarball for Debian Bullseye v5.9.1 <https://github.com/zcash/artifacts/raw/master/v5.9.1/bullseye/zcash-5.9.1-linux64-debian-bullseye.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Bullseye:

.. code-block:: bash

   sha256sum zcash-5.9.1-linux64-debian-bullseye.tar.gz

Result: ``1911d4da83781dfe9d50fb4e0e5bab14fddca6e648f861563a629583182f478e``

`Download Tarball for Debian Bookworm v5.9.1 <https://github.com/zcash/artifacts/raw/master/v5.9.1/bookworm/zcash-5.9.1-linux64-debian-bookworm.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Bookworm:

.. code-block:: bash

   sha256sum zcash-5.9.1-linux64-debian-bookworm.tar.gz

Result: ``3229e5a2c54a90f93530f93f9c59b0e134c9b95d9ed3754a4635f749586f7fd0``

This checksum was generated from our gitian deterministic build process. `View all gitian signatures <https://github.com/zcash/gitian.sigs/tree/master>`_.

Once you've verified that it matches, extract the Buster, Bullseye or Bookworm files and move the binaries into your executables $PATH: 

.. code-block:: bash

    tar -xvf zcash-5.9.1-linux64-debian-buster.tar.gz

    mv -t /usr/local/bin/ zcash-5.9.1/bin/*

Now that Zcash is installed, run this command to download the parameters used to create and verify shielded transactions:

.. code-block:: bash 

    zcash-fetch-params

Finally, `set up a configuration file <https://zcash.readthedocs.io/en/latest/rtd_pages/zcash_conf_guide.html>`_ (`~/.zcash/zcash.conf`) before runnning zcashd. It can be completely empty; it will then run with the default parameters.
