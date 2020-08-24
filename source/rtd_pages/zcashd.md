# Zcash Full Node and CLI

Zcashd & Zcash-cli allow you to run a full node and interact with it via a command-line interface.  The zcashd full node downloads a copy of the Zcash blockchain,  enforces rules of the Zcash network, and can execute all functionalities. The zcash-cli allows interactions with the node (i.e. tell it to send a transaction).

![zcashdandzcashcli](./images/zcashd_and_zcashcli.png)

Zcashd & Zcash-cli are the maintained by Electric Coin Company (the founding team for Zcash).


## Install

* [Debian/Ubuntu](Debian-Ubuntu-build.md) ([officially](https://zcash.readthedocs.io/en/latest/rtd_pages/supported_platform_policy.html#supported-platform-policy) supported)

* [Other Linux Systems](Linux-misc-build.md) ("best-effort" supported)

* [OSx](OSx-build.md) ("best-effort" supported)

* [Windows](windows-build.md) (unsupported)


## Configuration

Zcashd requires a zcash.conf file to run. 

A blank zcash.conf file will run with all default settings. To generate one, run: 

```
mkdir -p ~/.zcash
touch ~./zcash/zcash.conf
```

Zcashd can be configured in various ways to suit different use cases; see the [Zcash.conf guide](zcash_conf_guide.html) for an extensive list of options. 

## Sync

Depending on the speed of the network connection and the size of the blockchain, syncing to current chain height for Zcash may take anywhere from hours to a couple days. Please be patient! 

You will not be able to run certain commands via Zcash-cli until Zcashd is synced to current height. 

## Use

Refer to this web-interface of [RPC commands](https://zcash-rpc.github.io/). This is one of our most-referenced resources. However, the same information is available in the terminal via the help command. 

Try generating some addresses, then sending and receiving transactions! Note that there are separate commands for transparent and shielded addresses/transactions. 

## Upgrading

<!--If you're on a Debian-based distribution, you can follow the :ref:`install-debian-bin-packages-guide` to install Zcash on your system. --> 

To upgrade Zcashd & Zcash-cli, fetch the latest updates:
  ```
   git fetch origin
  ```

Run Zcashd again and verify that the version number matches that of the [source repository](https://github.com/zcash/zcash).

Helpful tips: 
* Upgrading to v3.0.0 may require a re-fetch of the parametes and a build; try the following: 
  ```
  git checkout v3.0.0
   ./zcutil/fetch-params.sh
   ./zcutil/build.sh -j$(nproc)
  ```
* Running ``make clean`` before building the update can eliminate random known link errors. 
* If you run into issues upgrading, please see the [Network Upgrade Guide](nu_dev_guide.html).

## References

An extensive list of Zcashd & Zcash-cli pages, including ones linked inline in this page above. 
* [User Guide](user_guide.html)
* [Troubleshooting Guide](troubleshooting_guide.html)
* [Zcash Payment API](payment_api.html)
* [Wallet Backup Instructions](wallet_backup.html)
* [Sending Memos with Zcashd](memos.html)
* [Zcash.conf guide](zcash_conf_guide.html)
* [Zcash Mining guide](zcash_mining_guide.html)
* [Security Warnings](security_warnings.html)
* [Data Directory Files](files.html)
* [Tor Support in zcashd](tor.html)