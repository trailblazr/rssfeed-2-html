#!/home/www/yourserverdomain/webapp/bin/python
# set the bang path to your virtual environments python bianry

basedir=`dirname $0`
source $basedir/bin/activate
# use this to debug issues with the path
# echo "Basedir is ${basedir}"

# following command executes your python app
# give a nice output file path where to write the file on your server
# pipe any output to /dev/null otherwise cron will send you emails...
python $basedir/app.py -f https://netzpolitik.org/feed -o /home/www/yourserverdomain/htdocs/netzpolitik/index.html -r YES > /dev/null
