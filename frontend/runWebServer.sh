#!/usr/bin/env bash
# This script is used to run the web server
cd ../logging/
./ logListen.php &
python3 app.py