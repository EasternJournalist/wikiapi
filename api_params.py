import requests
from typing import Literal, List, Union
import time
import functools

WIKIPEDIA_API_URL = 'https://en.wikipedia.org/w/api.php'


def params_info(
    titles: Union[str, List[str]] = None,
    pageids: Union[int, List[int]] = None,
    inprop: Literal['protection', 'talkid', 'watched', 'watchers', 'visitingwatchers', 'notificationtimestamp', 'subjectid', 'url', 'readable', 'preload', 'displaytitle'] = None,
):
    """
    Example URL: https://en.wikipedia.org/w/api.php?action=query&format=json&prop=info&titles=Algebra
    """
    assert (titles is None) ^ (pageids is None), 'Either titles or pageids must be specified.'
    params = {
        'action': 'query',
        'format': 'json',
        'prop': 'info',
        'titles': titles,
        'pageids': pageids,
        'inprop': inprop
    }
    params = {k: v for k, v in params.items() if v is not None}
    return params


def params_categorymembers(
    cmtitle: str = None,
    cmpageid: int = None,
    cmtype: Literal['page', 'subcat', 'file'] = None,
    cmlimit: int = 'max',
):
    """
    API Reference: https://www.mediawiki.org/wiki/API:Categorymembers
    
    Example URL: https://en.wikipedia.org/w/api.php?action=query&format=json&list=categorymembers&cmtype=subcat&cmtitle=Category:Algebra&cmlimit=max
    """

    assert (cmtitle is None) ^ (cmpageid is None), 'Either cmtitle or cmpageid must be specified.'
    assert cmtype in ['page', 'subcat', 'file'], 'cmtype must be one of "page", "subcat", "file".'

    params = {
        'action': 'query',
        'format': 'json',
        'list': 'categorymembers',
        'cmtitle': cmtitle,
        'cmpageid': cmpageid,
        'cmtype': cmtype,
        'cmlimit': cmlimit
    }
    params = {k: v for k, v in params.items() if v is not None}
    return params


def params_categories(
    titles: Union[str, List[str]] = None, 
    pageids: Union[int, List[int]] = None,
    cllimit: int = 'max',    
):
    """
    List all categories the pages belong to.

    Example https://en.wikipedia.org/w/api.php?action=query&prop=categories&titles=Albert%20Einstein&format=json
    """
    assert (titles is None) ^ (pageids is None), 'Either titles or pageids must be specified.'
    params = {
        'action': 'query',
        'format': 'json',
        'prop': 'categories',
        'titles': titles,
        'pageids': pageids,
        'cllimit': cllimit
    }
    params = {k: v for k, v in params.items() if v is not None}
    return params


def params_iwlinks(
        titles: Union[str, List[str]] = None, 
        pageids: Union[int, List[int]] = None,
        iwlimit: int = 'max',
    ):
    """
    Returns all interwiki links from the given pages.

    Example https://en.wikipedia.org/w/api.php?action=query&format=json&prop=iwlinks&titles=Albert%20Einstein
    """
    assert (titles is None) ^ (pageids is None), 'Either titles or pageids must be specified.'
    params = {
        'action': 'query',
        'format': 'json',
        'prop': 'iwlinks',
        'titles': titles,
        'pageids': pageids,
        'iwlimit': iwlimit
    }
    params = {k: v for k, v in params.items() if v is not None}
    return params


def params_links(
    titles: Union[str, List[str]] = None,
    pageids: Union[int, List[int]] = None,
    plnamespace: int = None,
    pllimit: int = 'max',
):
    """
    Returns all links from the given pages.

    Example https://en.wikipedia.org/w/api.php?action=query&format=json&prop=links&titles=Algebra&
    """
    assert (titles is None) ^ (pageids is None), 'Either titles or pageids must be specified.'
    params = {
        'action': 'query',
        'format': 'json',
        'prop': 'links',
        'titles': titles,
        'pageids': pageids,
        'plnamespace': plnamespace,
        'pllimit': pllimit
    }
    params = {k: v for k, v in params.items() if v is not None}
    return params


def params_extlinks(
    titles: Union[str, List[str]] = None,
    pageids: Union[int, List[int]] = None,
    elprotocol: Literal['http', 'https', 'ftp', 'ftps'] = None,
    ellimit: int = 'max',
):
    """
    Returns all external links from the given pages.

    Example https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extlinks&titles=Algebra
    """
    assert (titles is None) ^ (pageids is None), 'Either titles or pageids must be specified.'
    params = {
        'action': 'query',
        'format': 'json',
        'prop': 'extlinks',
        'titles': titles,
        'pageids': pageids,
        'elprotocol': elprotocol,
        'ellimit': ellimit
    }
    params = {k: v for k, v in params.items() if v is not None}
    return params


def params_linkshere(
    titles: Union[str, List[str]] = None,
    pageids: Union[int, List[int]] = None,
    lhnamespace: int = None,
    lhshow: Literal['redirect', 'nonredirect'] = None,
    lhlimit: int = 'max',
):
    """
    Returns all pages that link to the given pages.

    Example https://en.wikipedia.org/w/api.php?action=query&format=json&list=backlinks&bltitle=Algebra&bllimit=max
    """
    assert (titles is None) ^ (pageids is None), 'Either titles or pageids must be specified.'
    params = {
        'action': 'query',
        'format': 'json',
        'list': 'backlinks',
        'titles': titles,
        'pageids': pageids,
        'lhnamespace': lhnamespace,
        'lhshow': lhshow,
        'lhlimit': lhlimit
    }
    params = {k: v for k, v in params.items() if v is not None}
    return params


def params_images(
    titles: Union[str, List[str]] = None, 
    pageids: Union[int, List[int]] = None,
    imlimit: int = 'max',
):
    """
    Returns all images from the given pages.

    Example https://en.wikipedia.org/w/api.php?action=query&prop=images&titles=Astronomy&format=json
    """
    assert (titles is None) ^ (pageids is None), 'Either titles or pageids must be specified.'
    params = {
        'action': 'query',
        'format': 'json',
        'prop': 'images',
        'titles': titles,
        'pageids': pageids,
        'imlimit': imlimit
    }
    params = {k: v for k, v in params.items() if v is not None}
    return params


def params_pageviews(
    titles: Union[str, List[str]] = None, 
    pageids: Union[int, List[int]] = None,
    pvipdays: int = 30,  
):
    """
    Returns the number of pageviews for the given pages.

    Example https://en.wikipedia.org/w/api.php?action=query&format=json&titles=Mathematics&prop=pageviews&pvipdays=30
    """
    assert (titles is None) ^ (pageids is None), 'Either titles or pageids must be specified.'
    params = {
        'action': 'query',
        'format': 'json',
        'prop': 'pageviews',
        'titles': titles,
        'pageids': pageids,
        'pvipdays': pvipdays
    }
    params = {k: v for k, v in params.items() if v is not None}
    return params


def params_siteviews():
    """
    Returns the number of views of wiki site.

    Example https://en.wikipedia.org/w/api.php?action=query&format=json&meta=siteviews
    """
    params = {
        'action': 'query',
        'format': 'json',
        'meta': 'siteviews',
    }
    return params


def params_mostviewed():
    """
    Returns the most viewed pages. (based on last day's pageview count)
    Example https://en.wikipedia.org/w/api.php?action=query&format=json&list=mostviewed
    """
    params = {
        'action': 'query',
        'format': 'json',
        'list': 'mostviewed',
    }
    return params


def params_content_parse(
    page: str = None,
    prop: Literal['text', 'wikitext'] = None
):
    """
    Returns content of given pages, either as HTML or wikitext.

    Example https://en.wikipedia.org/w/api.php?action=parse&format=json&page=Algebra&prop=text&formatversion=2
    """
    params = {
        'action': 'query',
        'format': 'json',
        'prop': prop,
        'page': page,
    }
    params = {k: v for k, v in params.items() if v is not None}
    return params


def params_content_extracts(
    titles: Union[str, List[str]] = None, 
    pageids: Union[int, List[int]] = None,
    exchars: int = None,
    exsentences: int = 'max',
    exlimit: int = 'max',
):
    """
    Returns content of given pages, as extracts.

    Example https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exsentences=10&exlimit=1&titles=Pet_door&explaintext=1&formatversion=2
    """
    assert (titles is None) ^ (pageids is None), 'Either titles or pageids must be specified.'
    assert (exchars is None) ^ (exsentences is None), 'Either exchars or exsentences must be specified.'

    params = {
        'action': 'query',
        'format': 'json',
        'prop': 'extracts',
        'titles': titles,
        'pageids': pageids,
        'exchars': exchars,
        'exsentences': exsentences,
        'exintro': None if isinstance(titles, str) or isinstance(pageids, int) else "",
        'exlimit': exlimit,
        'explaintext': 1,
        'formatversion': 2,
    }
    params = {k: v for k, v in params.items() if v is not None}
    return params