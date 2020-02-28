#!/usr/bin/python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------
#  Copyright (c) 1995-2020, Ecometer s.n.c.
#  Author: Paolo Saudin.
#
#  Desc : Main script
#  File : WebApp.py
#
#  Date  : 2020-02-26 11:51
#  Update: 2020-02-26 11:51
# ----------------------------------------------------------------------
"""
    main template script

    --include
    py -3.4 -m py2exe.build_exe pydas.py -i logging.py -W setup-script.py
    sudo apt-get install python3-pip
    pip3 install cherrypy
    pip3 install Jinja2
    pip3 install simplejson
"""

# resouces
# http://www.cherrypy.org/chrome/common/2.2/docs/book/chunk/index.html
# http://jinja.pocoo.org/docs/
# http://jinja.pocoo.org/docs/tricks/

# run
# http://localhost:3000

#- ----------------------------------------------------------------------------
#- imports
#- ----------------------------------------------------------------------------
import os.path
import cherrypy
from cherrypy import _cperror
from jinja2 import Environment, FileSystemLoader, PackageLoader, Template
import sys
import subprocess
import platform
import datetime
import time
import simplejson
import re
import logging
import logging.handlers

#- ----------------------------------------------------------------------------
#- sub routines
#- ----------------------------------------------------------------------------
""" Handle errors
"""
def handle_error():
    cherrypy.response.status = 500
    cherrypy.response.body = ["<html><body>Sorry, an error occured</body></html>"]

""" Tail like function
"""
def tail(f, window=1):
    """
    Returns the last `window` lines of file `f` as a list of bytes.
    """
    if window == 0:
        return b''
    BUFSIZE = 1024
    f.seek(0, 2)
    end = f.tell()
    nlines = window + 1
    data = []
    while nlines > 0 and end > 0:
        i = max(0, end - BUFSIZE)
        nread = min(end, BUFSIZE)

        f.seek(i)
        chunk = f.read(nread)
        data.append(chunk)
        nlines -= chunk.count(b'\r')
        end -= nread
    return b'<br>'.join(b''.join(reversed(data)).splitlines()[-window:])

def runCommand(command, option):
    try:
        return simplejson.dumps({
            'result': 'success',
            'digitalin' : {
                'di1' : 1,
                'di2' : 0,
                'di3' : 0,
                'di4' : 0,
                'di5' : 0,
                'di6' : 1
            },
            'analog' : {
                'a1' : 1.222,
                'a2' : 0.4444
            },
            'wire' : {
                'w1' : 22.2323
            },
            'digitalout' : {
                'do1' : 1,
                'do2' : 0,
                'do3' : 1,
                'do4' : 0,
            }
        })

    except ValueError:
        return simplejson.dumps({
            'result' : 'fail',
            'msg' : 'Errore!'
        })


#- ----------------------------------------------------------------------------
#- main routine
#- ----------------------------------------------------------------------------
class WebApp(object):
    def __init__(self):
        pass

    @cherrypy.expose
    def index(self):
        #self.response.headers['Cache-Control'] = 'public, max-age=300;'
        #template = Template('Hello {{ name }}!')
        #return template.render(name='John Doe')

        #Testing logger
        today = datetime.datetime.today()
        cherrypy.log("{0} -- Main pahe".format(today.strftime("%Y%m%d-%H%M%S")))

        tmpl = env.get_template('index.html')
        return tmpl.render(title='OPAS - Gestione degli allarmi tramite Iono PI', target='WebApp')

    @cherrypy.expose
    def log(self):
        #self.response.headers['Cache-Control'] = 'public, max-age=300;'
        #template = Template('Hello {{ name }}!')
        #return template.render(name='John Doe')

        #Testing logger
        today = datetime.datetime.today()
        cherrypy.log("{0} -- Main pahe".format(today.strftime("%Y%m%d-%H%M%S")))

        tmpl = env.get_template('log.html')
        return tmpl.render(title='OPAS | LOG - Gestione degli allarmi tramite Iono PI', target='WebApp')


    #
    # ajax
    #
    @cherrypy.expose
    def get_status(self):
        cherrypy.log("Get Iono status")
        json_res = runCommand('/home/ecometer/vpn/connect2cva.sh', 'start')
        return json_res


    @cherrypy.expose
    def get_log(self):
        try:
            cherrypy.log("Read the current log file")
            # check file exists
            log_filename = '/Users/alessiatreves/Downloads/webapp/log/Web.log'
            if not os.path.isfile(log_filename):
                return simplejson.dumps({
                   'result': 'error',
                   'msg': 'File di log non esiste!'
                })

            with open(log_filename, 'rb') as f:
               last_lines = tail(f, 60).decode('utf-8')

            #cherrypy.log("Data:"+data)
            return simplejson.dumps({'result' : 'success', 'data' : last_lines })

        except ValueError:
            return simplejson.dumps({'result' : 'error' })


#- ----------------------------------------------------------------------------
#- global
#- ----------------------------------------------------------------------------
env = Environment(loader=FileSystemLoader('templates'))
#current_dir = os.path.dirname(os.path.abspath(__file__))
cherrypy.config.update({'request.error_response': handle_error})


#- ----------------------------------------------------------------------------
#- entry point
#- ----------------------------------------------------------------------------
if __name__ == '__main__':
    """__main__"""
    now = datetime.datetime.now()
    logging.info("Web app start @ %s on %s", now.strftime("%Y-%m-%d %H:%M:%S"), platform.system())

    # application log path
    app_path = os.path.dirname(os.path.realpath(__file__))
    log_path = os.path.join(app_path, 'log')
    if not os.path.exists(log_path):
        os.mkdir(log_path)

    config_path = os.path.join(app_path, 'config.ini')
    app = cherrypy.quickstart( WebApp(), config = config_path )
