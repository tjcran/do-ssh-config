import digitalocean
manager = digitalocean.Manager(token="")
user = 'root'
port = '22'
interval = '30'
config = 'Host %s \n\t HostName %s \n\t User %s \n\t Port %s \n\t ServerAliveInterval %s \n\t StrictHostKeyChecking no \n\t UserKnownHostsFile=/dev/null \n\t IdentityFile ~/.ssh/lenny \n'

