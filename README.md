# rssfeed-2-html
Fetches feed contents and generates a nice static website from the contents

## Installation (Local)

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

## Installation (Server)

You can easily set this app up to do some fancy work on a server, e.g. by engaging a crontab entry to execute the app. This would make it easy to setup your own static website for an rss feed wrapped in a nice webpage.

* See `crontab.txt` to have an idea how the crontab entry could lióok like. Btw you edit the crontab entries on your server usually by entering `crontab -e` which will edit the important file with `vi`.

* The entry in `crontab.txt` will trigger a script `cron.sh` which should be made executable by the cron daemon. So in doubt apply a `chmod ug+rx cron.sh` to make it available to cron.

* `cron` will trigger `cron.sh` and this in turn will trigger `update_feed.sh`. Why this? This helps to separate the script-context which is used for `update_feed.sh` from the usually used cron-environment which may differ from machien to machine.

Be careful with the paths to files and check the permissions and ownership and groupmembership of files if something fails. Often html-files need the ownership or group membership of `www-data` e.g. You could also do a `tail -f /var/log/syslog` to debug if your cronjob posts errors there. In some cases cron also sends local mails via postfix. You could check mails bei entering `mail` on your UNIX box.