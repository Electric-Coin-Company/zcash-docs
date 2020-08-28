Lightwalletd Instance Setup Guide
=================================

There are several reasons you may want to set up your own lightwalletd instance rather than using one of the public instances.

- while developing your light client (wallet) code, you can see lightwalletd's logging output
- for production use with your own light clients, to minimize trust by controlling this important part of the infrastructure
- to contribute to the development of lightwalletd itself.

There are two ways to deploy a lightwalletd instance:

- Clone the lightwalletd source code from its [GitHub repo](https://github.com/zcash/lightwalletd/)
- Run a binary instance using Docker.

This rest of this guide helps with the second option, which is the easier of the two.
You will need root (`sudo`) permissions. Install these if you haven't already:

- [Zcashd](file:///home/larry/gitlab/zcash-docs/build/html/rtd_pages/zcashd.html#install)
- [Docker](https://docs.docker.com/get-docker/)

Start zcashd on either testnet or mainnet and wait for it to finish syncing with the network.

The lightwalletd maintains some on-disk state (database) that must persist across restarts.
Create a directory to contain this state; you can choose any name (adjust below) but it needs
this particular user ID, 2002, as its owner:

```
mkdir ./lightwalletd_db_volume
sudo chown 2002 ./lightwalletd_db_volume
```
Last step! Launch lightwalletd,
port 8232 is mainnet; 18232 is testnet; also substitute your zcashd's rpcuser and rpcpassword:

```
docker run --rm \
  --volume $PWD/lightwalletd_db_volume:/srv/lightwalletd/db_volume \
  --network host \
  electriccoinco/lightwalletd:v0.4.2 \
  --grpc-bind-addr 0.0.0.0:9067 \
  --no-tls-very-insecure \
  --rpchost localhost \
  --rpcport 8232 \
  --rpcuser lightwd \
  --rpcpassword lightpassword \
  --data-dir /srv/lightwalletd/db_volume \
  --log-file /dev/stdout
```

The first time you run this, you'll see logging that shows lightwalletd downloading blocks
from zcashd The lightwalletd is usable immediately; the blocks downloading improves
performance (once it completes). You'll see two files populating within the database
directory. After it has download the blocks, then when you start lightwalletd it will
have high performance immediately.

If you remove the database directory (do that only while lightwalletd isn't running), it
will re-download blocks the next time it runs. This database is simply a cache and
never contains critical data.

If you restart zcashd to the other network (testnet to mainnet or the reverse), you
must restart lightwalletd. But you can restart zcashd to the same network without
restarting lightwalletd; it will attempt to reconnect for a few minutes and then give up.

You can test that it's running correctly using the [grpcurl](https://github.com/fullstorydev/grpcurl) tool,
for example:

```
$ grpcurl -plaintext localhost:9067 cash.z.wallet.sdk.rpc.CompactTxStreamer/GetLightdInfo
  "version": "v0.4.2",
  "vendor": "ECC LightWalletD",
  "taddrSupport": true,
  "chainName": "main",
  "saplingActivationHeight": "419200",
  "consensusBranchId": "f5b9230b",
  "blockHeight": "948288"
}
$ 
```
