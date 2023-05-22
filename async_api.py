import asyncio
import aiohttp
from typing import Dict, Any
import warnings

from .api_params import *
from .exception import WikiError
from ratelimit import rate_limit


def _merge_results(result, more):
    if isinstance(result, dict):
        for k, v in more.items():
            if k not in result:
                result[k] = v
            else:
                _merge_results(result[k], v)
    elif isinstance(result, list):
        result.extend(more)
    else:
        pass


@rate_limit(rps=100)
async def _aiohttp_get(params):
    async with aiohttp.ClientSession() as session:
        params = {k: str('|').join(map(str, v)) if isinstance(v, list) else v for k, v in params.items()}
        async with session.get(WIKIPEDIA_API_URL, params=params) as resp:
            return await resp.json()    


async def _get_till_complete(params):
    result = {}
    while True:
        resp_json = await _aiohttp_get(params)
        _merge_results(result, resp_json)
        if 'error' in resp_json:
            raise WikiError(resp_json['error'])
        if 'warnings' in resp_json:
            warnings.warn(resp_json['warnings'])
        if 'continue' not in resp_json:
            break
        params.update(resp_json['continue'])
    return result


async def query_info_async(
    titles: Union[str, List[str]] = None,
    pageids: Union[int, List[int]] = None,
    inprop: Literal['protection', 'talkid', 'watched', 'watchers', 'visitingwatchers', 'notificationtimestamp', 'subjectid', 'url', 'readable', 'preload', 'displaytitle'] = None,
) -> Dict[str, Dict[str, Any]]:
    """
    Example: https://en.wikipedia.org/w/api.php?action=query&format=json&prop=info&titles=Algebra
    """
    params = params_info(titles, pageids, inprop)
    result = await _get_till_complete(params)
    return result['query']['pages']


async def query_categorymembers_async(
    cmtitle: str = None,
    cmpageid: int = None,
    cmtype: Literal['page', 'subcat', 'file'] = None,
    cmlimit: int = 'max',
) -> List[Dict[str, Any]]:
    """
    API Reference: https://www.mediawiki.org/wiki/API:Categorymembers
    
    Example: https://en.wikipedia.org/w/api.php?action=query&format=json&list=categorymembers&cmtype=subcat&cmtitle=Category:Algebra&cmlimit=max
    """
    params = params_categorymembers(cmtitle, cmpageid, cmtype, cmlimit)
    result = await _get_till_complete(params)
    return result['query']['categorymembers']


async def query_categories_async(
    titles: Union[str, List[str]] = None, 
    pageids: Union[int, List[int]] = None,
    cllimit: int = 'max',    
) -> Dict[str, Dict[str, Any]]:
    """
    List all categories the pages belong to.

    Example: https://en.wikipedia.org/w/api.php?action=query&format=json&prop=categories&titles=Algebra
    """
    params = params_categories(titles, pageids, cllimit)
    result = await _get_till_complete(params)
    return result['query']['pages']


async def query_iwlinks_async(
    titles: Union[str, List[str]] = None, 
    pageids: Union[int, List[int]] = None,
    iwprefix: str = None,
    iwnamespace: int = None,
    iwlimit: int = 'max',    
) -> Dict[str, Dict[str, Any]]:
    """
    List all interwiki links from the given pages.

    Example: https://en.wikipedia.org/w/api.php?action=query&format=json&prop=iwlinks&titles=Algebra&iwlimit=max
    """
    params = params_iwlinks(titles, pageids, iwprefix, iwnamespace, iwlimit)
    result = await _get_till_complete(params)
    return result['query']['pages']


async def query_extlinks_async(
    titles: Union[str, List[str]] = None, 
    pageids: Union[int, List[int]] = None,
    elprotocol: Literal['http', 'https', 'ftp', 'ftps'] = None,
    ellimit: int = 'max',    
) -> Dict[str, Dict[str, Any]]:
    """
    List all external links from the given pages.

    Example: https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extlinks&titles=Algebra&ellimit=max
    """
    params = params_extlinks(titles, pageids, elprotocol, ellimit)
    result = await _get_till_complete(params)
    return result['query']['pages']


async def query_links_async(
    titles: Union[str, List[str]] = None, 
    pageids: Union[int, List[int]] = None,
    plnamespace: int = None,
    pllimit: int = 'max',    
) -> Dict[str, Dict[str, Any]]:
    """
    List all links from the given pages.

    Example: https://en.wikipedia.org/w/api.php?action=query&format=json&prop=links&titles=Algebra&pllimit=max
    """
    params = params_links(titles, pageids, plnamespace, pllimit)
    result = await _get_till_complete(params)
    return result['query']['pages']


async def query_linkshere_async(
    titles: Union[str, List[str]] = None, 
    pageids: Union[int, List[int]] = None,
    lhnamespace: int = None,
    lhshow: Literal['redirect', 'nonredirect'] = None,
    lhlimit: int = 'max',    
) -> Dict[str, Dict[str, Any]]:
    """
    List all pages that link to the given pages.

    Example: https://en.wikipedia.org/w/api.php?action=query&format=json&list=linkshere&titles=Algebra&lhlimit=max
    """
    params = params_linkshere(titles, pageids, lhnamespace, lhshow, lhlimit)
    result = await _get_till_complete(params)
    return result['query']['pages']


async def query_images_async(
    titles: Union[str, List[str]] = None, 
    pageids: Union[int, List[int]] = None,
    imlimit: int = 'max',    
) -> Dict[str, Dict[str, Any]]:
    """
    List all images on the given pages.

    Example: https://en.wikipedia.org/w/api.php?action=query&format=json&prop=images&titles=Algebra&imlimit=max
    """
    params = params_images(titles, pageids, imlimit)
    result = await _get_till_complete(params)
    return result['query']['pages']


async def query_pageviews_async(
    titles: Union[str, List[str]] = None, 
    pageids: Union[int, List[int]] = None,
    pvipdays: int = 30,    
) -> Dict[str, Dict[str, Any]]:
    """
    Get pageview counts for the given pages.

    Example: https://en.wikipedia.org/w/api.php?action=query&format=json&prop=pageviews&titles=Algebra&pvipdays=30
    """
    params = params_pageviews(titles, pageids, pvipdays)
    result = await _get_till_complete(params)
    return result['query']['pages']


async def query_siteviews() -> Dict[str, int]:
    """
    Get siteview counts for the given sites.

    Example: https://en.wikipedia.org/w/api.php?action=query&format=json&meta=siteviews&sites=en.wikipedia&pvipdays=30
    """
    params = params_siteviews()
    result = await _get_till_complete(params)
    return result['query']['siteviews']


async def query_mostviewed() -> List[Dict[str, Any]]:
    """
    Get most viewed pages for the given sites.

    Example: https://en.wikipedia.org/w/api.php?action=query&format=json&list=mostviewed
    """
    params = params_mostviewed()
    result = await _get_till_complete(params)
    return result['query']['mostviewed']


async def query_content_parse(
    page: str = None,
    prop: Literal['text', 'wikitext'] = None
) -> Dict[str, Dict[str, Any]]:
    """
    Get content for the given pages.

    Example: https://en.wikipedia.org/w/api.php?action=parse&format=json&page=Algebra&prop=text&formatversion=2
    """
    params = params_content_parse(page, prop)
    result = await _get_till_complete(params)
    return result['query']['pages']


async def query_content_extracts(
    titles: Union[str, List[str]] = None, 
    pageids: Union[int, List[int]] = None,
    exchars: int = None,
    exsentences: int = 'max',
) -> Dict[str, Dict[str, Any]]:
    """
    Get extracts for the given pages.

    Example: https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exsentences=10&exlimit=1&titles=Algebra&explaintext=1&formatversion=2
    """
    params = params_content_extracts(titles, pageids, exchars, exsentences)
    result = await _get_till_complete(params)
    return {str(page['pageid']): page for page in result['query']['pages']}