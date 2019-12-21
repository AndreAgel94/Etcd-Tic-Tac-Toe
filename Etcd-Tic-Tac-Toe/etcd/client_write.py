from etcd import Client

host = '127.0.0.1'
cluster_ports = 12346, 12356, 12366  # portas configuradas para cada nó no comando etcd

chave = '0'
valor = 'valor de teste'

client = Client(host=host, port=cluster_ports[0])  # escrevendo no nó 0
client.write(chave, valor)
