#!/bin/bash
# Call this file from a crontab entry on any server
# it calls itself a shell script to launch the python application

sh /home/www/config.seewetterpro.de/webapp/update_feed.sh
