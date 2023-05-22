"""
# WikiAPI

A low-level asynchronized Python wrapper for the MediaWiki API, which simplifies the requests and adds error handling.

WikiAPI is designed towards `low-level` wraps of the MediaWiki API, to ensure performance and flexibility.

The async API allows concurrent requests with `asyncio` and `aiohttp`, requiring aynchronized context which is more complicated to use. But the performance is much better, since Wikipedia API generally allows concurrent requests of up to 200/s and 50 pages per request, which is a huge number (You are allowed to query up to 10,000 pages per second!). The async version is recommended for large-scale requests.
"""

from .async_api import *
from .exception import *
