#!/usr/bin/env bash

sudo -E apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo -E tee /etc/apt/sources.list.d/mongodb.list
sudo -E apt-get update
sudo -E apt-get install mongodb-org
