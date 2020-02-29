#!/bin/bash
# Author : Paolo Saudin
# Description : purge old files
# Version 1

echo "analizzo $HOME/bin/webserver/log/*.log"
find $HOME/bin/webserver/log/ -name '*.log' -mtime +120 -type f -exec rm -vr {} \;
find $HOME/bin/webserver/log/ -name '*log*' -mtime +120 -type f -exec rm -vr {} \;
#find $HOME/bin/webserver/log/ -name '*.log' -mtime +120 -type f -exec echo {} \;
