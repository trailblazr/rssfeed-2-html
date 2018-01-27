# rssfeed-2-html
Fetches feed contents and generates a nice static website from the contents

## Installation

Create a `virtualenv` before you start installing. There do exist lots of tutorials how to work with **virtualenv**

Then run `pip install -r requirements.txt` to install all needed modules.

## Usage

Type `python app.py -h` to get following help:

```
usage: app.py [-h] [--feedurl FEEDURL] [--output OUTPUT] --clean {YES,NO}

Fetch an RSS-Feed and generate a Webpage from it.

optional arguments:
  -h, --help            show this help message and exit
  --feedurl FEEDURL, -f FEEDURL
                        url of feed to fetch
  --output OUTPUT, -o OUTPUT
                        filename of html to output
  --clean {YES,NO}, -c {YES,NO}
                        clean output without any CSS/style

e.g: python app.py -f https://www.netzpolitik.org/feed -o index.html -c NO
```

## Example

Type `python app.py -f https://www.hackerspace-bremen.de/feed -o space.html -c YES`
you will get an output file `space.html` which contains all the rss feed entries put into this file as a static website without any CSS / style infos.
