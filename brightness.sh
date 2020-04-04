#!/bin/bash

times=$[255/6]

darker(){
    echo "降低亮度"
    brightness=$(cat /sys/class/backlight/amdgpu_bl0/brightness)
    after=$(expr $brightness - $times)
    if [ $after -lt 0 ]; then
        after=0
    fi

    echo $after
    echo $after > /sys/class/backlight/amdgpu_bl0/brightness
}

lighter(){
    echo "提高亮度"
    brightness=$(cat /sys/class/backlight/amdgpu_bl0/brightness)
    after=$(expr $brightness + $times)
    if [ $after -gt 255 ]; then
        after=255
    fi
    echo $after
    echo $after > /sys/class/backlight/amdgpu_bl0/brightness
}

arg=$1


echo "${arg}"
if [ "$arg" == "dark" ];
then
    darker
elif [ "$arg" == "light" ];
then
    lighter
else
    echo "[options] 取值：dark, light"
fi
