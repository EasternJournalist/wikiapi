"""
WikiAPI is a Python wrapper for PART OF the MediaWiki API.

WikiAPI is designed as low-level interface to the MediaWiki API, to ensure performance and flexibility.
There are two versions of WikiAPI: blocking and async. All functions have implementations in both versions. The functionality is the same.
- The blocking version is easy to use, but it is not suitable for concurrent requests.
- The async version allows concurrent requests with `asyncio` and `aiohttp`, requiring aynchronized context which is more complicated to use.

If you want deeper insights, check [MediaWiki official API reference](https://www.mediawiki.org/wiki/API:Main_page)
"""

from .async_api import *
from .blocking_api import *
from .exception import *
