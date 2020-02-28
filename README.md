Arpa IonoPi Webserver
==========================
Web server to interact with the iono board

Setup
---------------------

  * sudo apt-get install python3-pip
  * sudo apt-get install git-core

  * mkdir -p ~/bin/webserver
  * git clone https://github.com/ecometer/arpa_ionopi_webserver.git ~/bin/webserver/
  * chmod +x ~/bin/webserver/*.py

  * pip3 install -r ~/bin/pydas/requirements.txt

  * python3 ~/bin/webserver/webapp.py
  * ~/bin/webserver/start_webapp.sh
  * ~/bin/webserver/stop_webapp.sh
