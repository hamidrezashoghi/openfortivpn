#!/usr/bin/python3

import psutil
import subprocess
import os

true = "openfortivpn" in (p.name() for p in psutil.process_iter())
bashCommand = "/usr/bin/openfortivpn"

if true == False:
    process = subprocess.Popen(bashCommand.split())
    process.stdout.close()
    process.communicate()
    notify = 'zenity --width=250 --warning --text "openfortivpn connected" --title="openfortivpn" --timeout=4'
    os.system(notify)

