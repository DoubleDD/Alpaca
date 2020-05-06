#!/bin/bash

device=$1
date_time=`date`
logsDir="/home/kedong/logs/udev"
if [ -d $logsDir ];
then
    echo ""
else
    echo "mkdir -p $logsDir"
    mkdir -p $logsDir
fi

echo "$date_time:  设备断开：$device" >> $logsDir/usb-mount.log

echo `umount -v /mnt/$device` >> $logsDir/usb-mount.log

