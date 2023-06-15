:orphan:

.. _install-binary-tarball-guide:

Binary Tarball Download & Setup
===============================

The Electric Coin Company provides a binary tarball for download.

As of v5.0.0, We are no longer supporting Debian 9(Stretch) packages in apt.

`Download Tarball for Debian Buster v5.5.1 <https://z.cash/downloads/zcash-5.5.1-linux64-debian-buster.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Buster:

.. code-block:: bash

   sha256sum zcash-5.5.1-linux64-debian-buster.tar.gz

Result: ``a43d00c8400da3b4aafb1a1de6b62db6ba8780a7d20c5173b8e180929b3026fa``

`Download Tarball for Debian Bullseye v5.5.1 <https://z.cash/downloads/zcash-5.5.1-linux64-debian-bullseye.tar.gz>`_

After downloading but before extracting, verify that the checksum of the tarball matches the hash below for the version of the binary you downloaded:

Debian Bullseye:

.. code-block:: bash

   sha256sum zcash-5.5.1-linux64-debian-bullseye.tar.gz

Result: ``98d3816f460b60a5cbb6d513492129f434cfa0a48badbd626dd82ed374a0e2a7``

This checksum was generated from our gitian deterministic build process. `View all gitian signatures <https://github.com/zcash/gitian.sigs/tree/master>`_.

Once you've verified that it matches, extract the Buster or Bullseye files and move the binaries into your executables $PATH: 

.. code-block:: bash

    tar -xvf zcash-5.5.1-linux64-debian-buster.tar.gz

    mv -t /usr/local/bin/ zcash-5.5.1/bin/*

Now that Zcash is installed, run this command to download the parameters used to create and verify shielded transactions:

.. code-block:: bash 

    zcash-fetch-params

Finally, `set up a configuration file <https://zcash.readthedocs.io/en/latest/rtd_pages/zcash_conf_guide.html>`_ (`~/.zcash/zcash.conf`) before runnning zcashd. It can be completely empty; it will then run with the default parameters.
