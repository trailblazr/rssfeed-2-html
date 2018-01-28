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

import sys
# fucking encoding!!!!!!!!!!!!!!!!!!!!!!!
reload(sys)
sys.setdefaultencoding( 'utf-8' )

# needed for basic file I/O
import os, traceback, argparse

import requests
import feedparser
import BeautifulSoup
import bs4 as bs
from readability import Document
from datetime import datetime, date

from feedparser import parse as parse_feed
from mako.template import Template

APP_BRANDNAME       = 'FeedReadability'
APP_BUILD           = 10
APP_RELEASE         = '1.0'
APP_PATH            = os.path.dirname(os.path.abspath(__file__))
APP_DEBUG           = False

DEFAULT_TITLE       = 'Feedtitle'
DEFAULT_FEED_SOURCE = 'https://www.hackerspace-bremen.de/feed'
DEFAULT_STATIC_SITE = 'index.html'
DEFAULT_IS_CLEAN    = False

def make_site_with_rssfeed_readable_again(url, filename, is_clean):
    """Convert feed to an HTML."""
    with open(filename, 'w') as file_object:
        print "\nOPENING URL: "+url+"\n\n"
        headers = {'User-Agent': APP_BRANDNAME+'/'+APP_RELEASE+' (Unix; Intel OS Nine 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36' }

        response = requests.get( url, headers=headers )
        mystr = response.text

        # remove heigh and width in images because CSS will do that
        mystr = mystr.replace(u"height=", "whatever=")
        mystr = mystr.replace(u"width=", "whatever=")

        # remove unwanted strings in output
        mystr = mystr.replace(u'<hr id=', '<hr class="spenden" id=')
        mystr = mystr.replace(u"<p><strong>Hilf mit!</strong>", "")
        mystr = mystr.replace(u"Mit Deiner finanziellen Hilfe unterstützt Du unabhängigen Journalismus.", "")
        
        if APP_DEBUG:
            print "FEED:\n"+ str( mystr )+"\n****************************"

        feedtitle = None
        try:
            root  = parse_feed( mystr )
            entries = root.entries

            # access feedtitle
            feedtitle = root.feed.title 
        except Exception, e:
            print "PARSING-ERROR: " + str( e )
            print( traceback.format_exc() )
            pass


        if not feedtitle:
            feedtitle = DEFAULT_TITLE

        if is_clean:
            template = APP_PATH+'/'+'template_clean.html'
        else:
            template = APP_PATH+'/'+'template_readable.html'

        if APP_DEBUG:
            print "\n ENTRIES TO RENDER: "+ str( len(entries) ) +"\n"
        html_footer = site_footer_html()
        html_content = Template(filename=template, output_encoding='utf-8').render(feedurl=url,entries=entries,feedtitle=feedtitle,footer=html_footer)
        
        if APP_DEBUG:
            print "HTML:\n"+ html_content+"\n****************************"
        
        if is_clean:
            clean = Document( html_content )
            file_object.write( clean.content() )

        else:
            file_object.write( html_content )

# footer
def site_footer_html():
    STYLE_HR = 'border: 0;height: 0;border-top: 1px solid rgba(0, 0, 0, 0.1);'
    today = datetime.now()
    version_info = 'Release '+str(APP_RELEASE)+' (build '+str(APP_BUILD)+') of '+APP_BRANDNAME
    footer = '<hr style="margin-top:50px;" class="style3" /><div style="margin-top:10px;margin-bottom:10px;">'
    footer = footer + '<div style="text-align:center;color:gray;"><small>'
    footer = footer + 'created 2018-'+str( today.year )+', by trailblazr &middot; '+version_info
    footer = footer + '</small></div>'
    return footer

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fetch an RSS-Feed and generate a Webpage from it.', 
        epilog='e.g: python %(prog)s -f https://www.netzpolitik.org/feed -o index.html -r YES')
    parser.add_argument('--feedurl', '-f', dest='feedurl', required=False, help='url of feed to fetch')
    parser.add_argument('--output', '-o', dest='output', required=False, help='filename of html to output')
    parser.add_argument('--readable', '-r', dest='readable', required=True, default=False, choices=['YES','NO'] ,help='add css to make it readable')
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

    readable = args.readable
    is_clean = DEFAULT_IS_CLEAN
    if not readable:
        is_clean = DEFAULT_IS_CLEAN
    else:
        if readable.decode('utf-8').lower() == 'yes':
            is_clean = False
        else:
            is_clean = True

    if should_print_hint:
        parser.print_help()
    else:
        make_site_with_rssfeed_readable_again( inputurl, ouputfile, is_clean)
