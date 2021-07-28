# Pyinstaller Example
 An executable Python script for running Sierra SQL queries and exporting the results to a csv.  Created using the pyinstaller module.

Prerequistes

In order to function you must complete the api_info.ini file in the same directory
and add your cacert.pem file to the certifi folder within the dist directory.

api_info.ini

Requires valid credentials for both the Sierra holds API and sql access
The file should be formatted like so

[api]

base_url = https://[local domain]/iii/sierra-api/v6

client_key = [enter Sierra API key]

client_secret = [enter Sierra API secret]

sql_host = [enter host for Sierra SQL server]

sql_user = [enter sql username]

sql_pass = [enter sql password]

cacert.pem file

To find where this file is located on your computer you may run the following python script

import certifi
certifi.where()

Once you've located the file, copy it to a certifi folder within the same directory
