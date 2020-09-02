# Developer Tools

Here are the most helpful tools to test and debug code.

## Zcashd/Zcash-cli RPC Docs

Thee [Zcash RPC webpage](https://zcash-rpc.github.io/) makes it easy to look at zcashd commands, their parameters, and examples. The content on that page is the formatted help text for each of the Zcash RPC calls, extracted by an open sourced tool. This is one of the most frequently used resources by core developers. 

## Public Test Network

The [Zcash testnet](testnet_guide.html) is a blockchain that attempts to mimic the main Zcash network for testing purposes, with its own coins that hold no monetary value (TAZ). It's used by developers to experiment with Zcash apps having to use Zcash (ZEC) and test network upgrades before activating on the main Zcash network. Since it's public and long-running, you can see a lot of historical data, and interact with many peers. 

## Private Containerized Network

The [Zcash testnet-in-a-box (TNB)](https://github.com/zcash-hackworks/zcash-testnet-in-a-box) will deploy a collection of monitored and peered zcashd instances to a Kubernetes cluster. This is useful for isolated testing in a controlled environent, giving you the control of how many node are on the network, how many transactions are sent and mined, etc. New protocol development, or research on new RPCs will benefit greatly from this tool. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/1360lSmfhnw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Block Explorer

By default, zcashd will operate as a full node and wallet. However, zcashd can alternatively be run as a [full node with access to a block explorer](insight_explorer.html), which allows it to see and fetch additonal fields (i.e. utxos, spent txid). This zcashd mode is commonly used along with zcash-cli to service exchanges, wallets, and other zcash services, but cannot be used as a wallet itself since it will contain no private keys.

<!--## todo-->
<!--grafana dashboard-->
<!--testnet in a box-->