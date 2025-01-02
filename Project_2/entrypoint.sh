#!/bin/bash

# Start Flask server in the background
cd /app/server
python3 app.py &

# Start Nginx
nginx -g 'daemon off;'