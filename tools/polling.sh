#!/bin/bash

while true
do  
  # curl -LI 127.0.0.1 -o /dev/null -w '%{http_code}\n' -s  
  echo [$(date)] - $(curl -LI 127.0.0.1 -s | head -n 1)
  sleep 1
done