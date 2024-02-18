#!/bin/bash

while true; do
    python naver.py  

    if [ -f "naver_copy_sample.csv" ]; then
        tail -n 1 naver_copy_sample.csv | sed -i '$ d' naver_copy_sample.csv
        echo "Removed the last line from 'naver_copy_sample.csv'"
    else
        echo "'naver_copy_sample.csv' not found. Continuing without removing the last line."
    fi
    
    echo "Script stopped. Restarting in 10 seconds..."
    sleep 10
done
