#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 10:36:34 2020

@author: bernardintheo
"""

import mysql.connector as mysql

db = mysql.connect(
        host = "127.0.0.1",
        user = "theo",
        passwd = "jAuevImVJWTrPMBz",
        database = "data_twitter",
        port="8889"
        
)