#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Fetches feed contents an generates a nice static website from the contents
#
# Notes:
# - You need to provide a source URL for an RSS feed
# - You should provide a filename and path where to store the result
#
# by trailblazr in Jan 2018

import requests
import feedparser
import BeautifulSoup
import bs4 as bs
import argparse
from readability import Document
import traceback

from feedparser import parse as parse_feed
from mako.template import Template

APP_DEBUG = False

DEFAULT_TITLE       = 'Feedtitle'
DEFAULT_FEED_SOURCE = 'https://www.hackerspace-bremen.de/feed'
DEFAULT_STATIC_SITE = 'index.html'
DEFAULT_IS_CLEAN    = False

def make_site_with_rssfeed_readable_again(url, filename, is_clean):
    """Convert feed to an HTML."""
    with open(filename, 'w') as file_object:
        print "\nOPENING URL: "+url+"\n\n"
        response = requests.get( url )
        mystr = response.text

        # remove heigh and width in images because CSS will do that
        mystr = mystr.replace(u"height=", "whatever=")
        mystr = mystr.replace(u"width=", "whatever=")

        # remove unwanted strings in output
        mystr = mystr.replace(u'<hr id=', '<hr class="spenden" id=')
        mystr = mystr.replace(u"<p><strong>Hilf mit!</strong>", "")
        mystr = mystr.replace(u"Mit Deiner finanziellen Hilfe unterstützt Du unabhängigen Journalismus.", "")
        
        if APP_DEBUG:
            print "FEED:\n"+mystr+"\n****************************"

        feedtitle = None
        try:
            root  = parse_feed( mystr )
            entries = root.entries

            # access feedtitle
            feedtitle = root.feed.title 
        except Exception, e:
            print "PARSING-ERROR: " + str( e )
            print( traceback.format_exc() )

        if not feedtitle:
            feedtitle = DEFAULT_TITLE

        if is_clean:
            template = 'template_clean.html'
        else:
            template = 'template_dark.html'

        html_content = Template(filename=template, output_encoding='utf-8').render(feedurl=url,entries=entries,feedtitle=feedtitle)
        
        if APP_DEBUG:
            print "HTML:\n"+ html_content+"\n****************************"
        
        if is_clean:
            clean = Document( html_content )
            file_object.write( clean.content() )

        else:
            file_object.write( html_content )

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fetch an RSS-Feed and generate a Webpage from it.', 
        epilog='e.g: python %(prog)s -f https://www.netzpolitik.org/feed -o index.html -c NO')
    parser.add_argument('--feedurl', '-f', dest='feedurl', required=False, help='url of feed to fetch')
    parser.add_argument('--output', '-o', dest='output', required=False, help='filename of html to output')
    parser.add_argument('--clean', '-c', dest='clean', required=True, default=False, choices=['YES','NO'] ,help='clean output without any CSS/style')
    args = parser.parse_args()

    if not args:
        parser.print_help()
        exit(1)

    should_print_hint = False
    
    inputurl = args.feedurl
    if not inputurl:
        inputurl = DEFAULT_FEED_SOURCE

    ouputfile = args.output
    if not ouputfile:
        ouputfile = DEFAULT_STATIC_SITE

    clean = args.clean
    is_clean = DEFAULT_IS_CLEAN
    if not clean:
        is_clean = DEFAULT_IS_CLEAN
    else:
        if clean.decode('utf-8').lower() == 'yes':
            is_clean = True
        else:
            is_clean = False

    if should_print_hint:
        parser.print_help()
    else:
        make_site_with_rssfeed_readable_again( inputurl, ouputfile, is_clean)
