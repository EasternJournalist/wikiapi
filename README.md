# WikiAPI

A low-level asynchronized Python wrapper for the MediaWiki API, which simplifies the requests and adds error handling.

WikiAPI is designed towards `low-level` wraps of the MediaWiki API, to ensure performance and flexibility.

The async API allows concurrent requests with `asyncio` and `aiohttp`, requiring aynchronized context which is more complicated to use. But the performance is much better, since Wikipedia API generally allows concurrent requests of up to 200/s and 50 pages per request, which is a huge number (You are allowed to query up to 10,000 pages per second!). The async version is recommended for large-scale requests.

Currently, this `WikiAPI` only supports a small part of the MediaWiki API. More functions will be added in the future. There are really a lot of APIs in the MediaWiki API. To wrap all of them is a huge project but mostly repetitive.

Actually I will recommend you to use [wikipedia](https://github.com/goldsmith/Wikipedia) or [mediawiki](https://github.com/barrust/mediawiki) if you don't have high demand for large-scale requests and extensive data that can not be accessed with those packages. This repository is mainly for my own use and learning purpose. But I still hope it can be helpful for you as examples of how to use the MediaWiki API.

If you want deeper insights about the APIs, check [MediaWiki official API reference](https://www.mediawiki.org/wiki/API:Main_page)