#!/bin/bash

declare -a process_list=(
    "[p]ython servoHS645MG.py"
    "[p]ython eyeled.py"
    "[p]ython grootcam.py"
)

for i in "${process_list[@]}"
do
    pid=`ps -ef | grep "$i" | awk '{print $2}'`
    if [ -z "$pid" ]
    then
        echo "Cannot find any process called {$i}"
    else
        echo "Killing process {$i} with pid $pid"
        kill -9 $pid
    fi
done
