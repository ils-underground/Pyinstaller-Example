# Pyinstaller Example

An executable Python script for running Sierra SQL queries and exporting the results to a csv.  Created using the pyinstaller module.

### About Pyinstaller

Pyinstaller is a Python module that easily packages up a Python script along with all of its dependencies into a form that can be deployed and executed by others without having to install Python or build an appropriate environment themselves.

For a good introduction to Pyinstaller I recommend the [Inforworld article here](https://www.infoworld.com/article/3543792/how-to-use-pyinstaller-to-create-python-executables.html).

### Pyinstaller Considerations

Dist folders created by Pyinstaller can be quite large (in the 100's of MBs) depending on the script and the environment in use.  The infoworld article linked above discusses some methods for reducing the size but in general I have found it best build a new environment the only contains the modules needed for the particular script.

### Example script

The Pyinstaller Example.py script in the main directory here is an extremely basic script for the sake of demonstration.  It prompts the user to select a query located in the Queries folder and will then export the results into a .csv file in the Output folder.

In the dist folder you will find what is produced by running ```pyinstaller "Pyinstaller Example.py"``` from the command prompt.  That folder can then be placed on another windows workstation or on a shared drive (along with the completed certificates and .ini file described under prerequistes) and others may then run the script via the executable file in the directory.

### Prerequistes

In order to function you must complete the api_info.ini file in the same directory
and add your cacert.pem file to the certifi folder within the dist directory.

api_info.ini

Requires valid credentials for both the Sierra holds API and sql access
The file should be formatted like so

```
[api]

sql_host = [enter host for Sierra SQL server]

sql_user = [enter sql username]

sql_pass = [enter sql password]
```
cacert.pem file

To find where this file is located on your computer you may run the following python script
```
import certifi
certifi.where()
```
Once you've located the file, copy it to a certifi folder within the same directory
