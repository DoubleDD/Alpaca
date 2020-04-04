#!/bin/bash

process_count=`ps -ef|grep wallpaper.sh -c`

echo $process_count
if [ $process_count -gt 1 ];
then
    echo 'restart wallpaper'
    killall wallpaper.sh
    sleep 0.5
fi

~/script/wallpaper.sh &
