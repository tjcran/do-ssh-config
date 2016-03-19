import digitalocean
manager = digitalocean.Manager(token="e27f9e754be5715465792f6be84d7de45bda0d47d0e608c804fa94f6417457cb")
user = 'root'
port = '22'
interval = '30'
config = 'Host %s \n\t HostName %s \n\t User %s \n\t Port %s \n\t ServerAliveInterval %s \n\t StrictHostKeyChecking no \n\t UserKnownHostsFile=/dev/null \n\t IdentityFile ~/.ssh/lenny \n'

