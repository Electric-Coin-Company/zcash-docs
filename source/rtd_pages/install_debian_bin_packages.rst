:orphan:

.. _install-debian-bin-packages-guide:

Debian Binary Packages Setup
============================

Zcash Company operates a package repository for 64-bit Debian-based distributions. If you'd like to try out the binary packages, you can set it up on your system and install Zcash from there.

First install the following dependency so you can talk to our repository using HTTPS:

.. code-block:: bash

   sudo apt-get install apt-transport-https

Next add the Zcash master signing key to apt's trusted keyring:

.. code-block:: bash

   wget -qO - https://apt.z.cash/zcash.asc | sudo apt-key add -


``Key fingerprint = A2CB 84F2 48C7 DDC9 6C2C 55C8 AEFD 26F9 66E2 79CD``

Add the repository to your sources:

.. code-block:: bash

   echo "deb [arch=amd64] https://apt.z.cash/ jessie main" | sudo tee /etc/apt/sources.list.d/zcash.list

Finally, update the cache of sources and install Zcash:

.. code-block:: bash
   
   sudo apt-get update && sudo apt-get install zcash

Lastly you can run ``zcash-fetch-params`` to fetch the zero-knowledge parameters, and set up `~/.zcash/zcash.conf` before running Zcash as your local user, as documented in the :ref:`user_guide`. 

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

**Public Key Expiration error**

If you see the error when updating to a new version of zcashd:

``The following signatures were invalid: KEYEXPIRED 1539886450``

Follow the instructions at :ref:`updating_signing_keys`
   
Tor
---

The repository is also accessible via Tor, after installing the `apt-transport-tor` package, at the address zcaptnv5ljsxpnjt.onion. Use the following pattern in your sources.list file: ``deb [arch=amd64] tor+http://zcaptnv5ljsxpnjt.onion/ jessie main``

.. _updating_signing_keys:

Updating Signing Keys
---------------------

If your Debian binary package isn't updating due to an expired public key, you'll need to replace it with the updated key and apt information.

Remove the old signing key:

.. code-block:: bash

    sudo apt-key del 63C4A2169C1B2FA2

Remove the list item from local apt:

.. code-block:: bash

    sudo rm /etc/apt/sources.list.d/zcash.list

Update the repository list:

.. code-block:: bash

    apt-get update

Then retrieve new key:

.. code-block:: bash

    wget -qO - https://apt.z.cash/zcash.asc | sudo apt-key add -

Re-get the apt info:

.. code-block:: bash

    echo "deb [arch=amd64] https://apt.z.cash/ jessie main" | sudo tee /etc/apt/sources.list.d/zcash.list

Then update the list again:

.. code-block:: bash

    apt-get update

At this point you should be able to upgrade with the new public key.
