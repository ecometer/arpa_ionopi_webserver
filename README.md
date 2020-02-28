Arpa IonoPi Webserver
==========================
Web server to interact with the iono board

Setup
---------------------

  * sudo apt-get install python3-pip
  * sudo apt-get install git-core

  * mkdir -p $HOME/bin/webserver
  * git clone https://github.com/ecometer/arpa_ionopi_webserver.git $HOME/bin/webserver/
  * chmod +x $HOME/bin/webserver/*.py

  * pip3 install -r $HOME/bin/webserver/requirements.txt

  * python3 $HOME/bin/webserver/webapp.py
  * $HOME/bin/webserver/start_webapp.sh
  * $HOME/bin/webserver/stop_webapp.sh
