#/bin/bash
path="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
python $path/sshconfig.py
mv ssh-config.txt /home/$USER/.ssh/config
