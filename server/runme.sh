#!/bin/sh

SPATH=`dirname $(readlink -f $0)`

export PYTHONPATH=$PYTHONPATH:$SPATH
echo "server started..."
python3 server.py

