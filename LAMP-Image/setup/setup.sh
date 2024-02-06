#!/bin/sh

chmod +x start.sh
service mariadb start
mysql -u root < ./database.sql