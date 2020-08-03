# Developer Tools

Here are the most helpful tools to test and debug code.

## Zcashd RPC Docs

Thee [Zcash RPC webpage](https://zcash-rpc.github.io/) makes it easy to look at zcashd commands, their parameters, and examples. The content on that page is the formatted help text for each of the Zcash RPC calls, extracted by an open sourced tool. This is one of the most frequently used resources by core developers. 

## Test Network

The [Zcash testnet](testnet_guide.html) is a blockchain that attempts to mimic the main Zcash network for testing purposes, with its own coins that hold no monetary value (TAZ). It's used by developers to experiment with Zcash apps having to use Zcash (ZEC) and test network upgrades before activating on the main Zcash network. We  recommend developers to use testnet for development and testing. 

## Block Explorer

By default, zcashd will operate as a full node and wallet. However, zcashd can alternatively be run as a [full node with access to a block explorer](insight_explorer.html), which allows it to see and fetch additonal fields (i.e. utxos, spent txid). This zcashd mode is commonly used along with zcash-cli to service exchanges, wallets, and other zcash services, but cannot be used as a wallet itself since it will contain no private keys.

<!--## todo-->
<!--grafana dashboard-->
<!--testnet in a box-->