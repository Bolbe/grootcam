#!/bin/bash

echo "Starting Trunkled"
python trunkled.py 35023 &

# Start servo process
echo "Starting servo HS645MG process on pin GPIO6"
GPIOZERO_PIN_FACTORY=pigpio python servoHS645MG.py 6 35021 &

echo "Starting Eyeled"
python eyeled.py 35022 &

# block until network and server OK
echo "Waiting for network and server..."
python waitforconnection.py

echo "Starting Grootcam"
python grootcam.py &
