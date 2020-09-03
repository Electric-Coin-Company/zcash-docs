# Development Best Practices

We pledge to respect all contributors. In the interest of fostering an open and welcoming community, we also expect contributors to adhere to the [contributor code of conduct](https://zcash.readthedocs.io/en/latest/rtd_pages/code_of_conduct.html).

## Development workflow

The [Development workflow and guidelines](https://zcash.readthedocs.io/en/latest/rtd_pages/development_guidelines.html) will get you up to speed and contribute to Zcash projects. It talks about the Zcash Github workflow, which has a few quirks from the general git flow, how Zcash core developers code and test, and the nuts and bolts of operation (CI, versioning, and release process). 

## Handling Zcash features
The [Zcash feature UX checklist](https://zcash.readthedocs.io/en/latest/rtd_pages/ux_wallet_checklist.html) will give you an idea of how Zcash features are standardly treated, and how you should design for them. For instance, shielded addresses should be used long term, since using a new one per transaction (industry standard) does not provide additional privacy. These lessons learned over time will save you some technical complexity and support calls if you follow these guidelines. 