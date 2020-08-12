# Zcash Basics

Zcash is a cryptocurrency that uses advanced applied cryptography to provide enhanced privacy via shielded addresses. Zcash is the first practical application of zk-SNARKs, a specific type of zero-knowledge proof.

## Overview

Get a quick dive on Zcash in 8 minutes:

1. Introducing blockchains, Zcash vs Bitcoin, and Zcash's main feature (2 min)

	<iframe width="560" height="315" src="https://www.youtube.com/embed/VHkZnuM-VLE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1. How we define financial privacy, and why financial privacy is important (3 min)

	<iframe width="560" height="315" src="https://www.youtube.com/embed/SAbbEJzsJB0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

3. How Zcash uses zero-knowledge proofs for financial privacy (2 min)

	<iframe width="560" height="315" src="https://www.youtube.com/embed/4k5nI-ajDxk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Zcash Features

This is a quick summary; the [Zcash technology page](https://z.cash/technology/) has additional information and examples. 

Primary features: 
* **Addresses**: Zcash has two types of addresses: private (z-addresses) and transparent (t-addresses). Z-addresses start with a “z,” and t-addresses start with a "t."  The two Zcash address types are interoperable. Funds can be transferred between z-addresses and t-addresses. There are privacy implications of shielding or deshielding information through these transactions. Today, most wallets and exchanges exclusively support t-addresses, although support for shielded addresses is available for mobile and desktop wallets. 
* **Transactions**: Transactions between two transparent addresses (t-addresses) work just like Bitcoin: the sender, receiver and transaction value are publicly visible. Transactions involving shielded addresses include shielded (z-to-z), shielding (t-to-z), and deshielding (z-to-t), with the z-address getting privacy protections. The most secure transaction is a shielded (z-to-z) one, which encrypts the sender and receiver addresses and transaction amount. However, all transactions appear on the public blockchain, so a transaction is known to have occured and what fees were paid. 
* **Viewing keys**: The owner of a z-address can share its transaction details with trusted third parties via a view key--a key that grants read access but not spend authority over the address. This allows for "selective disclosure", where transactions are auditable but disclosure is under the participant's control. This allows compliance with payment for auditing, tax regulations, or anti-money laundering rules.


Supporting features: 
* Like Bitcoin, Zcash has a fixed total supply of 21 million units.
* Low-fee transactions of .0001 ZEC; default for all transactions, but configurable.
* Encrypted memos to pass along messages or other useful data.
* Transaction expiration to reduce mempool bloat; default expiry is 20 blocks (50 min).
* Multisignature transactions; currently only available for public transactions.


## Zcash Protocol 

* **Units and divisibility**: The unit of account of the Zcash system is a ZEC. The ticker symbol used to represent Zcash is also “ZEC”. As a nod to Bitcoin’s creator, a zatoshi is the smallest amount within Zcash representing 0.00000001 ZEC, one hundred millionth of a ZEC.
* **Funding Structure**: Zcash pays out a portion of each block reward to fund protocol development and (for the first year) to pay back investors. During the first four years of Zcash, 10% of the block reward was transferred to the Founders Reward fund and distributed to the Electric Coin Co., Zcash Foundation and initial investors. After network upgrade 4, 8% of the block reward will be transferred to the Dev Fund and managed by a Major Grants Review Committee.
* **Mining**: Originally Zcash could be mined at home, using CPU or GPU machines. As mining hardware evolved, ASIC machines became the preferred mining machine for professional cryptocurrency miners and mining pools. ASICs can be customized for a particular use (such as mining Zcash) and therefore outperformed previous mining hardware such as CPUs and GPUs. Zcash community members voted against ASIC-resistant protocol updates in mid-2018 citing security concerns. The top mining pools for Zcash include Flypool, Nanopool and Slushpool. 
The next network upgrade, Heartwood includes ZIP 213, which would allow miners to mine directly to a shielded coinbase.
* **Scalability**: Scalability work is in progress. There are several approaches to making blockchains scalable, both at the protocol layer (layer 1) and at the application layer (layer 2). In September 2019, Sean Bowe, researcher at Electric Coin Co., proposed Halo, a novel technique for practical recursive zero-knowledge proofs. ECC researcher Daira Hopwood presented a research proposal for sharding architecture. This proposal calls for the use of sharding, a technique that partitions a database into sections or “shards” to improve the throughput limit, in order to scale to high transaction volumes. 

## Project History 

* **Pre-launch**: Zcash grew out of “Zerocash/Zerocoin,” an experimental proposal from seven scientists to improve privacy protections in Bitcoin. The Zerocoin company, known today as the Electric Coin Co., raised $3M in funding to develop the initial protocol.
* **Creation**:  Zcash launched on October 28, 2016 by Electric Coin Co., a private company founded by [Zooko Wilcox](https://en.wikipedia.org/wiki/Zooko_Wilcox-O%27Hearn). Zcash relies on a novel mathematical proof called a zk-SNARK. “SNARKs are the engine that can quickly and efficiently verify a transaction and add it to the blockchain without revealing any details to the public.” SNARKs require a set of public parameters which allow users to construct and verify private transactions. These parameters are set up in an elaborate [secure multi-party computation](https://en.wikipedia.org/wiki/Secure_multi-party_computation); for Zcash, this is known as the [Trusted Setup](https://z.cash/technology/paramgen/).
* **2016 - 2018**: After the Zcash launch, the Zcash engineering team released a series of upgrades known as the “Sprout series.” The team also put forward plans for two core protocol upgrades known as Overwinter and Sapling. The Sapling upgrade made efficiency improvements and enabled new kinds of core protocol features. The Zcash Foundation was formed in March 2017 with an initial endowment of 273,000 ZEC, taken from the Founder’s Reward. The Zcash Foundation organized the [Powers of Tau ceremony](https://www.zfnd.org/blog/powers-of-tau/), which was at the time the largest multi-party computation ceremony ever performed.  In 2017, enterprise partnerships like the [Zcash collaboration with JP Morgan](https://electriccoin.co/blog/jpm-quorum-integration/) further fueled a wider interest in blockchains and zk-SNARKs. The Sapling upgrade activated October 29, 2018, almost two years to the date from the initial Zcash launch.
* **2019-2020**: In early 2019, the Zcash Company rebranded to the Electric Coin Co. to differentiate from Zcash the protocol and the Zcash Foundation. The Zcash community began a several-month-long governance discussion regarding the continuation of the Founder’s Reward and the [Zcash trademark](https://electriccoin.co/blog/electric-coin-co-donates-zcash-trademark-to-zcash-foundation/). In February 2019 it was revealed that a serious cryptographic flaw had affected the zk-SNARK proving system, called [BCTV14](https://eprint.iacr.org/2013/879), that was used by Zcash before the Sapling upgrade. This flaw could have allowed counterfeiting. The Electric Coin Co. stated in a blog post that they “believe that no one else was aware of the vulnerability and that no counterfeiting occurred in Zcash”. Electric Coin Co. announced a research project to increase the scalability of Zcash by 2021. One of the results of this research is the [Halo proving system](https://eprint.iacr.org/2019/1021). Blossom, the third network upgrade for Zcash, activated in December 2019. This upgrade halved the target block interval, to 75 seconds. Funding discussions culminated in early 2020 with community consensus around [ZIP 1014](https://zips.z.cash/zip-1014), a Zcash Improvement proposal that describes a structure for a newly established Zcash Development Fund. [Heartwood](https://z.cash/upgrade/heartwood/), the fourth network upgrade is scheduled to activate in July 2020. Heartwood includes Flyclient support and shielded coinbase. Canopy is the next network upgrade, which activates in November 2020, ahead of Zcash’s first halvening.