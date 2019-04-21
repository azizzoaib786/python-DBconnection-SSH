#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import pymysql
import sshtunnel
from sshtunnel import SSHTunnelForwarder

server = SSHTunnelForwarder(
    ('10.0.3.147', 22),
    ssh_username='deploy',
    ssh_pkey='~/.ssh/id_rsa',
    remote_bind_address=('127.0.0.1', 3306)
)
server.start()

con = pymysql.connect(host='127.0.0.1', user='root', passwd='mysql', db='backoffice_demo', port=server.local_bind_port)

with con:
    
    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    version = cur.fetchone()
    
    print("Database version: {}".format(version[0]))
