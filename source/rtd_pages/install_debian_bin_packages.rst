:orphan:

.. _install-debian-bin-packages-guide:

Debian Binary Packages Setup
============================

The Electric Coin Company operates a package repository for 64-bit Debian-based distributions. If you'd like to try out the binary packages, you can set it up on your system and install Zcash from there.

First install the following dependency so you can talk to our repository using HTTPS:

.. code-block:: bash

   sudo apt-get update && sudo apt-get install apt-transport-https wget gnupg2

Next add the Zcash master signing key to apt's trusted keyring:

.. code-block:: bash

   wget -qO - https://apt.z.cash/zcash.asc | gpg --import
   gpg --export B1C9095EAA1848DBB54D9DDA1D05FDC66B372CFE | sudo apt-key add -

``Key fingerprint = B1C9 095E AA18 48DB B54D 9DDA 1D05 FDC6 6B37 2CFE``

Add the repository to your Bullseye sources:

.. code-block:: bash

   echo "deb [arch=amd64] https://apt.z.cash/ bullseye main" | sudo tee /etc/apt/sources.list.d/zcash.list

Or add the repository to your Bookworm sources:

.. code-block:: bash

   echo "deb [arch=amd64] https://apt.z.cash/ bookworm main" | sudo tee /etc/apt/sources.list.d/zcash.list

Update the cache of sources and install Zcash:

.. code-block:: bash
   
   sudo apt-get update && sudo apt-get install zcash

Fetch the zero-knowledge parameters: 

.. code-block:: bash
   
   zcash-fetch-params

Lastly, `set up a configuration file <https://zcash.readthedocs.io/en/latest/rtd_pages/zcash_conf_guide.html>`_ (`~/.zcash/zcash.conf`) before runnning zcashd. It can be completely empty; it will then run with the default parameters.

**Missing Public Key Error**

If you see:

``The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 70C830C67EB9DCB4``

Get the new key directly from the `z.cash site <https://apt.z.cash/zcash.asc>`_:

.. code-block:: bash

   wget -qO - https://apt.z.cash/zcash.asc | gpg --import
   gpg --export B1C9095EAA1848DBB54D9DDA1D05FDC66B372CFE | sudo apt-key add -

to retrieve the new key and resolve this error.

For any other signing key issues see :ref:`updating_signing_keys`

Troubleshooting
---------------

.. note:: Only x86-64 processors are supported.


If you're starting from a new virtual machine, sudo may not come installed. See this issue for instructions to get up and running: https://github.com/zcash/zcash/issues/1844

**libgomp1 or libstdc++6 version problems**

These libraries are provided with gcc/g++. If you see errors related to updating them, you may need to upgrade your gcc/g++ packages to version 4.9 or later. First check which version you have using ``g++ --version``; if it is before 4.9 then you will need to upgrade.

On Ubuntu Trusty, you can install gcc/g++ 4.9 as follows:

.. code-block:: bash

   sudo add-apt-repository ppa:ubuntu-toolchain-r/test
   sudo apt-get update
   sudo apt-get install g++-4.9
   
Tor
---

The repository is also accessible via Tor, after installing the `apt-transport-tor` package, at the address zcaptnv5ljsxpnjt.onion. Use the following pattern in your sources.list file: ``deb [arch=amd64] tor+http://zcaptnv5ljsxpnjt.onion/ stretch main``

.. _updating_signing_keys:

Updating Signing Keys
---------------------

If your Debian binary package isn't updating due to an error with the public key, you can resolve the problem by updating to the new key. 

**Revoked Key error**

If you see something similar to:

``The following signatures were invalid: REVKEYSIG AEFD26F966E279CD``

Remove the key marked as revoked:

.. code-block:: bash

    sudo apt-key del AEFD26F966E279CD

Then retrieve the updated key:

.. code-block:: bash

   wget -qO - https://apt.z.cash/zcash.asc | gpg --import
   gpg --export B1C9095EAA1848DBB54D9DDA1D05FDC66B372CFE | sudo apt-key add -

Then update the list again:

.. code-block:: bash

    sudo apt-get update


**Expired Key error**

If you see something similar to:

``The following signatures were invalid: KEYEXPIRED 1539886450``

Remove the old signing key:

.. code-block:: bash

    sudo apt-key del 1539886450

Remove the list item from local apt:

.. code-block:: bash

    sudo rm /etc/apt/sources.list.d/zcash.list

Update the repository list:

.. code-block:: bash

    sudo apt-get update

Then retrieve new key:

.. code-block:: bash

   wget -qO - https://apt.z.cash/zcash.asc | gpg --import
   gpg --export B1C9095EAA1848DBB54D9DDA1D05FDC66B372CFE | sudo apt-key add -

Re-get the apt info:

.. code-block:: bash

    echo "deb [arch=amd64] https://apt.z.cash/ bullseye main" | sudo tee /etc/apt/sources.list.d/zcash.list

Then update the list again:

.. code-block:: bash

    sudo apt-get update

At this point you should be able to upgrade with the new public key.
