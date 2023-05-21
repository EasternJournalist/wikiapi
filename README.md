# WikiAPI

WikiAPI is a Python wrapper for the MediaWiki API, which simplifies the requests and adds error handling.

WikiAPI is designed towards `low-level` wraps of the MediaWiki API, to ensure performance and flexibility.
There are two versions of WikiAPI: **blocking** and **async**. All functions have implementations in both versions. The functionality is the same.
- The blocking version is easy to use, but it is not suitable for concurrent requests. (NOTE: actually it is not ready yet because personally I don't have high demand for it, but it will be added in the future)
- The async version allows concurrent requests with `asyncio` and `aiohttp`, requiring aynchronized context which is more complicated to use. But the performance is much better, since Wikipedia API allows concurrent requests of up to 200/s and 50 pages per request generally, which is a huge number (You are allowed to query up to 10,000 pages per second!). The async version is recommended for large-scale requests.

Additionally, I wish to add a `Page` class to represent a page on a wiki site, which will be more convenient to use, following the popular `wikipedia` package [https://github.com/goldsmith/Wikipedia](https://github.com/goldsmith/Wikipedia), which is a high-level wrapper of the MediaWiki API and extremely easy to use, but less supported functionalities. Actually I will recommend you to use `wikipedia` if you don't have high demand for large-scale requests and extensive data that can not be accessed from package `wikipedia`.

Currently, this `WikiAPI` only supports a small part of the MediaWiki API. More functions will be added in the future. There are really a lot of APIs in the MediaWiki API, which is amazing. To wrap all of them is a huge project but mostly repetitive. I will add more functions if I need them in the future. If you need more functions, you can also add them yourself and make a pull request.

If you want deeper insights about the APIs, check [MediaWiki official API reference](https://www.mediawiki.org/wiki/API:Main_page)