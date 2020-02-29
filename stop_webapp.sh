#!/bin/bash
# Author : Paolo Saudin
# Description : stop python script
# Version 1

# --------- Info ---------
echo "stopping webapp script"

# --------- User Settings ---------
PROCESS2KILL="/home/pi/bin/webserver/webapp.py"

# --------- Run program ---------
echo "killing process id [`pgrep -f $PROCESS2KILL`]"
pkill -f "$PROCESS2KILL"

# --------- End ---------
echo "done"
