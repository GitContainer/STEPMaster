#!/usr/bin/python

import os
import subprocess
os.chdir("main/")
subprocess.call("python getpip.py", shell=True)
subprocess.call("python setup.py", shell=True)