#!/usr/bin/env python3

"""Create and email a list of new items

Author: Gem Stone-Logan
Contact Info: gem.stone-logan@mountainview.gov or gemstonelogan@gmail.com
"""

import psycopg2
import csv
import requests
import os
import configparser
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

def listQueries():
	
    file_list = [f for f in os.listdir('.') if os.path.isfile(os.path.join('.', f)) and f.endswith('.sql')]
    print(file_list)

def runQuery(query,csvFile):

    # import configuration file containing our connection string
    # api_info.ini looks like the following
    #[db]
    #sql_host = [enter host for Sierra SQL server]
    #sql_user = [enter sql username]
    #sql_pass = [enter sql password]
    
    config = configparser.ConfigParser()
    config.read('api_info.ini')
    
    conn = psycopg2.connect("dbname='iii' user='" + config['api']['sql_user'] + "' host='" + config['api']['sql_host'] + "' port='1032' password='" + config['api']['sql_pass'] + "' sslmode='require'")

    #Opening a session and querying the database for weekly new items
    cursor = conn.cursor()
    
    cursor.execute(open(query,"r").read())
    #For now, just storing the data in a variable. We'll use it later.
    columns = [i[0] for i in cursor.description]
    rows = cursor.fetchall()
    conn.close()
    
    '''
    #use instead for Python 3.x
    with open(csvFile,'w', encoding='utf-8', newline='') as tempFile:
    '''
    with open(csvFile,'wb') as tempFile:
        myFile = csv.writer(tempFile, delimiter=',')
        myFile.writerow(columns)
        myFile.writerows(rows)
    tempFile.close()
    
    return csvFile

def main():
    print('\nWhich query do you wish to run?\n')
    #listQueries()
    #print('\n')
    Tk().withdraw()
    my_query = askopenfilename(initialdir = "Queries/",title = "Select query",filetypes=[("Query Files", "*.sql")])
    #use input instead of raw_input for Python 3.x
    my_file_name = raw_input('\nEnter a name for your output file and click enter:\n') + '.csv'
    path = 'Output/'
    csvFile = os.path.join(path,my_file_name)
    query_results = runQuery(my_query,csvFile)
    print('Your file has been created in the Output folder')

main()
