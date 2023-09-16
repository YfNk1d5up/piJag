#!/bin/bash

  if (ps aux | grep "piJagClimApp/main.py" | grep -v grep > /dev/null)
  then
DISPLAY=:0.0 XAUTHORITY=/home/pi/.Xauthority xdotool search --desktop 0 --name "piJagClim" windowactivate

  else

DISPLAY=:0.0 XAUTHORITY=/home/pi/.Xauthority python3 /home/pi/piJag/Software/piJagClimApp/main.py &
while [[ !
DISPLAY=:0.0 XAUTHORITY=/home/pi/.Xauthority wmctrl -l|grep piJagClim
]] ; do
  true
done
DISPLAY=:0.0 XAUTHORITY=/home/pi/.Xauthority xdotool search --desktop 0 --name "piJagClim" windowactivate

  fi