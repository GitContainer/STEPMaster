#!/usr/bin/python

import os
import subprocess
os.chdir("main/")
subprocess.call("python flush.py", shell=True)
subprocess.call("python check.py", shell=True)
subprocess.call("python splasherosion.py", shell=True)
subprocess.call("python sheeterosion.py", shell=True)
subprocess.call("python deposition.py", shell=True)