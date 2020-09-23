# Building Zcashd & Zcash-cli on Debian/Ubuntu

Zcashd & Zcash-cli are [officially supported](https://zcash.readthedocs.io/en/latest/rtd_pages/supported_platform_policy.html) for Debian/Ubuntu. Since Debian/Ubuntu is the best supported platform, we recommend running Zcashd & Zcash-cli on Debian/Ubuntu if possible. 

## Instructions

First install the development toolchain with `apt`:

```
sudo apt-get install \
    build-essential pkg-config libc6-dev m4 g++-multilib \
    autoconf libtool ncurses-dev unzip git python3 python3-zmq \
    zlib1g-dev curl bsdmainutils automake
```

Now fetch the source code:

```
git clone https://github.com/zcash/zcash.git
cd zcash/
git checkout v4.0.0
```

In order to run `zcashd` and some tests you will need the zkSNARK parameters:

```
./zcutil/fetch-params.sh
```

Now you can build:

```
./zcutil/build.sh -j$(nproc)
```

To clean the source, there is a utility. This is useful when switching branches, altering dependencies, or if you encounter a build caching issue (in which case, please [let us know](https://github.com/zcash/zcash/issues)).

```
./zcutil/clean.sh
```

## Next steps
Now that you've built Zcashd & Zcash-cli, we can move on to the next steps of: configuration, sync, and use. Refer back to the [Zcashd & Zcash-cli page](https://zcash.readthedocs.io/en/latest/rtd_pages/zcashd.html) for further instructions. 
