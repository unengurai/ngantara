#!/bin/sh

SPATH=`dirname $(readlink -f $0)`

#if [ $PYTHONPATH -eq '' ] 
#then
	export PYTHONPATH=$PYTHONPATH:$SPATH/handler
#else 
#	export PYTHONPATH=$SPATH
#fi

echo "server started..."
echo $PYTHONPATH
python3 client.py

