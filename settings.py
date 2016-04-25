import digitalocean
manager = digitalocean.Manager(token="03b535f0110a027f987045ced775860caef613b6a66be365084f23d5cffd0df6")
user = 'root'
port = '22'
interval = '30'
config = 'Host %s \n\t HostName %s \n\t User %s \n\t Port %s \n\t ServerAliveInterval %s \n\t StrictHostKeyChecking no \n\t UserKnownHostsFile=/dev/null \n\t IdentityFile ~/.ssh/lenny \n'
star = 'Host github.com \n\t  IdentityFile ~/.ssh/github \n'
