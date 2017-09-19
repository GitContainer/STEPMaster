#!/usr/bin/python


########## HERE IS THE INITIAL SECTION OF SETUP WSP CLASS ##########
# Install program modules, packages and dependencies
# Before starting WSP, user should fulfill the dependencies by running the script.
# Active the script below if your Python have no needed modules (PyFiglet, NumPy, and Pandas).
# Here is a function to install python and the needed packages.
  
  # Installing PyFiglet, NumPy, and Pandas

import pip
def install(package1, package2, package3, package4, package5):
    pip.main(['install', package1, package2, package3, package4, package5])

if __name__ == '__main__':
    install('pyfiglet','pandas','numpy','setuptools','wheel')
########## HERE IS THE LAST SECTION OF SETUP WSP CLASS ##########

########## HERE IS THE INITIAL SECTION OF FLUSH OUPUT FOLDER CLASS ##########
# FLUSH OUTPUT FOLDER
  # Flush and clean up content of output folder to make sure there is no files inside

import os
my_directory = '../output'
for dirpath, dirnames, filenames in os.walk(my_directory):
    # Remove regular files and ignore directories
    for filename in filenames:
        os.unlink(os.path.join(dirpath, filename))
########## HERE IS THE LAST SECTION OF FLUSH OUPUT FOLDER CLASS ##########