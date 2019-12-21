from etcd import Client

host = '127.0.0.1'
cluster_ports = 12346, 12356, 12366  # portas configuradas para cada nó no comando etcd

chave = 'Estado_do_Jogo127.0.0.1127.0.0.1agel.txt'
chave7 = '7'
chave2 = '2'

client = Client(host=host, port=cluster_ports[2])  # lendo do nó 2
valor = client.read(chave).value
print(valor)

client = Client(host=host, port=cluster_ports[2])  # lendo do nó 2
valor = client.read(chave7).value


client = Client(host=host, port=cluster_ports[2])  # lendo do nó 2
valor = client.read(chave2).value



client = Client(host=host, port=cluster_ports[2])  # lendo do nó 2
valor = client.get('')
for r in valor.children:
	print(valor.key)
	print(valor.value)
