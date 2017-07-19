#!/bin/bash
sudo /etc/init.d/apache2 start

firefox http://localhost

sleep 5

sudo /etc/init.d/apache2 stop
