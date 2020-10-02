# Zcashd & Zcash-cli on Windows

We do not currently support Zcashd & Zcash-cli on Windows.

We do not have documented instructions to build Zcashd & Zcash-cli on Windows, and do not recommend doing so. 

However, it is technically possible to run on them on Windows with a cross-compile from Debian. Follow the [install process for Debian/Ubuntu](Debian-Ubuntu-build.html), and then run the following command to cross-compile for Windows: ```HOST=x86_64-w64-mingw32 ./zcutil/build.sh -j$(nproc)```. 

Next, transfer the binary over to a Windows machine to run Zcashd & Zcash-cli on Windows. Updating Zcashd & Zcash-cli on Windows will require a cross-compile every time. For this reason, if you are able to run Zcashd & Zcash-cli on another operating system, we recommend doing that instead.