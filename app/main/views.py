from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_articles, get_sources
from ..models import Article, Source, Headline

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    sources = get_sources(None)
    title = 'NewsArena'
    return render_template('index.html', title = title, sources = sources)


@main.route('/articles/<source>')
def articles(source):
    '''
    View articles page function that returns the articles page and its data
    '''
    all_articles = get_articles(source)

    return render_template('articles.html', articles=all_articles)


@main.route('/sources/<category>')
def categories(category):
    '''
    View articles page function that returns the articles page and its data
    '''
    all_sources = get_sources(category)
    title = f'All {category} sources'

    return render_template('index.html', title=title, sources=all_sources)
