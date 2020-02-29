#!/bin/bash
# Author : Paolo Saudin
# Description : run python script at startup
# Version 1

# --------- Info ---------
echo "running webapp script"

# --------- User Settings ---------
PROCESS2RUN="/home/pi/bin/webserver/webapp.py"

# --------- Run program ---------
cd "/home/pi/bin/webserver"
/usr/bin/python3 $PROCESS2RUN 2>&1 /home/pi/bin/webserver/log/sart_webapp.log &
VAR=`pgrep -f "$PROCESS2RUN"`
echo "program pid $VAR"

# ---------------------------------
echo "done"
