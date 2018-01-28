# rssfeed-2-html
Python application which fetches rss-feed and generates a nice static website with high readability from the available feed entries.

## Installation (Local)

Create a `virtualenv` before you start installing. There do exist lots of tutorials on how to work with **virtualenv**.

Then run `pip install -r requirements.txt` to install all needed modules. There are some modules related to crypto which are needed to access TLS secured sites.

## Usage

Type `python app.py -h` to get following help:

```
usage: app.py [-h] [--feedurl FEEDURL] [--output OUTPUT] --readable {YES,NO}

Fetch an RSS-Feed and generate a Webpage from it.

optional arguments:
  -h, --help            show this help message and exit
  --feedurl FEEDURL, -f FEEDURL
                        url of feed to fetch
  --output OUTPUT, -o OUTPUT
                        filename of html to output
  --readable {YES,NO}, -r {YES,NO}
                        add css to make it readable

e.g: python app.py -f https://www.netzpolitik.org/feed -o index.html -r YES
```

There are **three arguments** you can provide to the commandline call:

* `-f` or `--feedurl` which expects the http/s-url to the rss-feed  
**Example:** `python app.py -f http://www.tagesschau.de/xml/rss2`
* `-o` or `--output` which expects an absolute or relative path to a filename where to store the static website  
**Example:** `python app.py -o /home/www/mywebsite/htdocs/index.html` 
* `-r` or `--readable` expects a `YES` or a `NO` (casesensitive) to render site with readability support or without  
**Example:** `python app.py -r YES` will render a page with readability support 

## Example

Type `python app.py -f https://www.hackerspace-bremen.de/feed -o space.html -r NO`
you will get an output file `space.html` which contains all the rss feed entries put into this file as a static website without any CSS / style infos.

## Installation (Server)

You can easily set this app up to do some fancy work on a server, e.g. by engaging a crontab entry to execute the app. This would make it easy to setup your own static website for an rss feed wrapped in a nice webpage.

* `cron` should trigger `cron.sh` on a regular basis to automate things and this in turn will trigger `update_feed.sh`. Why this? This helps to separate the script-context which is used for `update_feed.sh` from the usually used cron-environment which may differ from machien to machine.
* See `crontab.txt` to have an idea/example of how the crontab entry could look like. Btw you edit the crontab entries on your server usually by entering `crontab -e` which will edit the important file with `vi` then you need to add the lines from `crontab.txt` and change the serverdomain to activate it.
* The entry seen in the example of `crontab.txt` will trigger a script `cron.sh` which should be made executable by the cron daemon. So in doubt apply a `chmod ug+rx cron.sh` to make it available to cron.
* Test all these configured scripts **before adding the cron entry** by just entering `./cron.sh` on the commandline and look what happens.
* For **readability** to work, you need to copy the following folders into your site directory
  * `css`
  * `js`
  * `images`

Be careful with the paths to files and check the permissions and ownership and groupmembership of files if something fails. Often html-files need the ownership or group membership of `www-data` e.g. You could also do a `tail -f /var/log/syslog` to debug if your cronjob posts errors there. In some cases cron also sends local mails via postfix. You could check mails bei entering `mail` on your UNIX box.