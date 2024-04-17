#!/bin/bash
docker build -t play-app .
docker run -p 9000:9000 play-app &
ngrok http 9000