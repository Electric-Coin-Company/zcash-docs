:orphan:

.. _install-debian-bin-packages-guide:

Debian Binary Packages Setup
============================

The Electric Coin Company operates a package repository for 64-bit Debian-based distributions. If you'd like to try out the binary packages, you can set it up on your system and install Zcash from there.

First install the following dependency so you can talk to our repository using HTTPS:

.. code-block:: bash

   sudo apt-get install apt-transport-https wget gnupg2

Next add the Zcash master signing key to apt's trusted keyring:

.. code-block:: bash

   wget -qO - https://apt.z.cash/zcash.asc | sudo apt-key add -


``Key fingerprint = 3FE6 3B67 F85E A808 DE9B  880E 6DEF 3BAF 2727 66C0``

Add the repository to your sources:

.. code-block:: bash

   echo "deb [arch=amd64] https://apt.z.cash/ jessie main" | sudo tee /etc/apt/sources.list.d/zcash.list

Finally, update the cache of sources and install Zcash:

.. code-block:: bash
   
   sudo apt-get update && sudo apt-get install zcash

Lastly you can run ``zcash-fetch-params`` to fetch the zero-knowledge parameters, and set up `~/.zcash/zcash.conf` before running Zcash as your local user, as documented in the :ref:`user_guide`. 

**Missing Public Key Error**

If you see:

``The following signatures couldn't be verified because the public key is not available: NO_PUBKEY C2A798EF998940FA``

Get the new key either directly from the `z.cash site <https://apt.z.cash/zcash.asc>`_:

``wget -qO - https://apt.z.cash/zcash.asc | sudo apt-key add -``

or download from a public keyserver:

``sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 6DEF3BAF272766C0``

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

The repository is also accessible via Tor, after installing the `apt-transport-tor` package, at the address zcaptnv5ljsxpnjt.onion. Use the following pattern in your sources.list file: ``deb [arch=amd64] tor+http://zcaptnv5ljsxpnjt.onion/ jessie main``

.. _updating_signing_keys:

Updating Signing Keys
---------------------

If your Debian binary package isn't updating due to an error with the public key, you can resolve the problem by updating to the new key. 

**Revoked Key error**

If you see:

``The following signatures were invalid: REVKEYSIG AEFD26F966E279CD``

Remove the key marked as revoked:

.. code-block:: bash

    sudo apt-key del AEFD26F966E279CD

Then retrieve the updated key:

.. code-block:: bash

    wget -qO - https://apt.z.cash/zcash.asc | sudo apt-key add -

Then update the list again:

.. code-block:: bash

    sudo apt-get update


**Expired Key error**

If you see:

``The following signatures were invalid: KEYEXPIRED 1539886450``

Remove the old signing key:

.. code-block:: bash

    sudo apt-key del 63C4A2169C1B2FA2

Remove the list item from local apt:

.. code-block:: bash

    sudo rm /etc/apt/sources.list.d/zcash.list

Update the repository list:

.. code-block:: bash

    sudo apt-get update

Then retrieve new key:

.. code-block:: bash

    wget -qO - https://apt.z.cash/zcash.asc | sudo apt-key add -

Re-get the apt info:

.. code-block:: bash

    echo "deb [arch=amd64] https://apt.z.cash/ jessie main" | sudo tee /etc/apt/sources.list.d/zcash.list

Then update the list again:

.. code-block:: bash

    sudo apt-get update

At this point you should be able to upgrade with the new public key.

Upgrading Debian 8 Jessie to Debian 9 Stretch
----------------------------------------------

Before you begin upgrading from Debian 8 to Debian 9, we strongly encourage you to follow :ref:`wallet_backup` .

At the very minimum, it is best to move these backup wallet files to an external USB.

Once you have ensured all your keys, wallet, and conf files are backup properly it is worth reading through https://www.debian.org/releases/stable/amd64/release-notes/ch-upgrading.html

Specifically, you will want to pay attention to items described in https://www.debian.org/releases/stretch/amd64/release-notes/ch-upgrading.en.html#trouble

If you are comfortable with your Debian and Zcash backups, please follow the below instructions for a minimal system upgrade:

1. It is recommended to have your Debian 8 Jessie system up to date before beginning. 

   .. code-block:: bash

       sudo apt-get update
       sudo apt-get upgrade

2. Edit your `/etc/apt/sources.list` file to replace all jessie fields with stretch.

   .. code-block:: bash

       sed -i 's/jessie/stretch/g' /etc/apt/sources.list

   You should now notice the mirrors in `/etc/apt/sources.list` contain stretch fields, not jessie

   Note: If you decide to use `stable` instead of `stretch`, you may run the risk of accidentally 
   updating when Debian 10 becomes the stable version.

3. Update and upgrade the list of available packages for Debain 9 Stretch.

   .. code-block:: bash

       sudo apt-get update
       sudo apt-get upgrade

4. Ensure you have proper disk space before completing system upgrade with latest available version

   .. code-block:: bash

       sudo apt-get dist-upgrade

5. Once upgrade is complete, remove the packages that are no longer needed

   .. code-block:: bash

       sudo apt-get autoremove

6. Reboot your system and sanity check the kernel version on boot

    .. code-block:: bash

       reboot
    
    System restarts

    .. code-block:: bash

       uname -a

    OR 

    .. code-block:: bash

       cat /etc/debian_version

You should see a Debain 9 field and the upgrade is complete!


