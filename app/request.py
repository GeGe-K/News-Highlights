import os
import urllib.request, json
from .models import Headline, Source, Article
from newsapi import NewsApiClient



# Getting api key
api_key = None

newsapi= None


#Getting base url
# base_url = None
# sources_url = None
# articles_url = None



def configure_request(app):
    global api_key, newsapi
    api_key = app.config['NEWS_API_KEY']
    newsapi = NewsApiClient(api_key = api_key)
    # base_url = app.config["TOP_HEADLINES_API_BASE_URL"]
    # sources_url = app.config["SOURCE_API_BASE_URL"]
    # articles_url = app.config["ARTICLES_API_BASE_URL"]
    


def get_headlines(source):
    """
    Function that gets the json response to our url request
    """
    
    get_headlines_url = base_url.format(source, api_key)

    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)
        print(get_headlines_response)
        headlines_results = None

        if get_headlines_response['articles']:
            headlines_results_list = get_headlines_response['articles']
            headlines_results = process_results(headlines_results_list)

    return headlines_results


def process_results(headlines_list):
    '''
    Function  that processes the headlines result and transform them to a list of Objects
    Args:
        headlines_list: A list of dictionaries that contain headlines details
    Returns :
        headlines_results: A list of headlines objects
    '''
    headlines_results = []
    for headlines_item in headlines_list:
        author = headlines_item.get('author')
        title = headlines_item.get('title')
        description = headlines_item.get('description')
        urlToImage = headlines_item.get('urlToImage')
        url = headlines_item.get('url')
        publishedAt = headlines_item.get('publishedAt')

        if urlToImage:
            headlines_object = Headline(
                author, title, description, urlToImage, url, publishedAt)
            headlines_results.append(headlines_object)

    return headlines_results


def get_sources(category):
    # api_key = os.environ.get('NEWS_API_KEY')
    # get_sources_url = sources_url.format(category, api_key)

    # with urllib.request.urlopen(get_sources_url) as url:
    #     get_sources_data = url.read()
    #     get_sources_response = json.loads(get_sources_data)
    newsapi = NewsApiClient(api_key)
    get_sources_response = newsapi.get_sources(category = category)
    print(get_sources_response)

    sources_results = None
    if get_sources_response['sources']:
        sources_results_list = get_sources_response['sources']
        sources_results = process_sources(sources_results_list)

    return sources_results


def process_sources(sources_list):
    '''
    Function  that processes the sources result and transform them to a list of Objects
    Args:
        sources_list A list of dictionaries that contain catnews details
t:
    Returns :
        sources_results: A list of sources objects
    '''
    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')

        if id:
            sources_object = Source(id, name, description, url)
            sources_results.append(sources_object)

    return sources_results


def get_articles(source):
    '''
    Function that gets the json response to our url request
    '''
    # get_articles_url = articles_url.format(id, api_key)
    # print(get_articles_url)
    # with urllib.request.urlopen(get_articles_url) as url:
    #     get_articles_data = url.read()
    #     get_articles_response = json.loads(get_articles_data)
    get_articles_response = newsapi.get_everything(sources=source)

    articles_results = None

    if get_articles_response['articles']:
        articles_results_list = get_articles_response['articles']
        articles_results = process_articles(articles_results_list)

    return articles_results


def process_articles(articles_list):
    '''
    Function  that processes the article result and transform them to a list of Objects
    Args:
        articles_list: A list of dictionaries that contain article details
    Returns :
        articles_results: A list of article objects
    '''
    articles_results = []
    for articles_item in articles_list:
        id = articles_item.get('id')
        author = articles_item.get('author')
        title = articles_item.get('title')
        description = articles_item.get('description')
        url = articles_item.get('url')
        urlToImage = articles_item.get('urlToImage')
        publishedAt = articles_item.get('publishedAt')

        if urlToImage:
            articles_object = Article(
                id, author, title, description, url, urlToImage, publishedAt)
            articles_results.append(articles_object)

    return articles_results
