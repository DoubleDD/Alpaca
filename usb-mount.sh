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

mkdir -p /mnt/$device
echo "mount /dev/$device /mnt/$device" >> $logsDir/usb-mount.log
#mount /dev/$device /mnt/$device

echo "$date_time:  设备接入：$device" >> $logsDir/usb-mount.log
