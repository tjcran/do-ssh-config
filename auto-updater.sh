#!/bin/bash
path='/home/tyler/Scripts/do/auto-updater'
python $path/sshconfig.py
echo "generating temporary ssh config file"
mv /home/$USER/.ssh/config /home/$USER/.ssh/config.bak
echo "backing up original ssh config file..."
mv ssh-config.txt /home/$USER/.ssh/config

for i in `awk '/Host / {print $2;}' /home/$USER/.ssh/config`; do
	ssh-keygen -R $i
	ssh   -oStrictHostKeyChecking=no $i "apt-get -y update && DEBIAN_FRONTEND=noninteractive  apt-get -y -o Dpkg::Options::='--force-confdef' -o Dpkg::Options::='--force-confold' upgrade"
done

mv /home/$USER/.ssh/config.bak /home/$USER/.ssh/config
