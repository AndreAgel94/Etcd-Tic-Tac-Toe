# Etcd-Tic-Tac-Toe
Projeto feito com o objetivo de aprender mais sobre a criação e implementação de um sistema distribuído. Feito na discipila de Sistemas Distribuidos.

**Aluno**<br>
Andre Agel<br>


## Jogo da velha (tic-tac-toe)
![Erro, Gif indisponível!](https://thumbs.gfycat.com/PoisedGrippingFox-small.gif)


### Ideia
A ideia é criar um jogo da velha para que a turma inteira possa jogar em um servidor, cada um em sua thread

O servidor suportará até 30 pessoas conectadas, sendo que a cada duas conexõe, uma thread diferente será separada para aqueles jogadores jogarem um contra o outro.

As partidas e o estado dos jogos estarão salvos em um cluster de servidores

As regras do jogo sao simples e estão claramente explicadas no link abaixo:
[LINK PARA AS REGRAS](https://www.bigmae.com/regras-jogo-da-velha/)

### Funcionamento
* Ao abrir o servidor, dois usuários devem se conectar. Quando eles entrarem, será criada uma thread para rodar a função principal do jogo. Isso pode ser feito para até 30 usuários, ou seja, 15 threads serão criadas. 
* Após os dois jogadores se conectarem, o administrador do servidor deverá perguntar se eles querem começar um novo jogo ou recuperar um estado de jogo anterior (caso tenha havido algum erro no servidor ou se alguem precisou sair). O jogador Bola é
o mestre da sala, e deve dar um nome ao jogo.
* Com a resposta dos usuários, o administrador irá dar um comando para o servidor, que irá realizar uma dessas duas opções.
* Caso recupere um estado anterior, serão recuperados do ultimo jogo: o tabuleiro, a pontuação do circulo, pontuação do xis e o numero da jogada (a vez de quem iria jogar).
* Caso escolha para iniciar um novo jogo, uma nova sala será criada e o jogador bola deve dar nome a ela.
* A cada jogada de cada jogador o jogo é salvo em um cluster de servidores. Para recuperar, o servidor utiliza o nome da sala 
que foi dada pelo jogador bola.

### Linguagem de implementação
O jogo é implementado em Python.

### Componentes
Clients (jogadores), 1 interface para rodar o jogo (terminal), 1 servidor para as pessoas acessarem e um cluster de servidores com 3 nós que se comunica com o servidor da aplicação.

### Instalação do Etcd server:
* sudo apt-get update
* sudo apt-get install etcd
* sudo apt-get install etcd-server

### Como executar?
1. Clone o projeto

2. Entre na pasta etcd e abra 3 terminais(que serão os nós do cluster), para subir o cluster execute cada um dos comandos
em cada um dos terminais, respectivamente.

etcd --name infra0 --initial-advertise-peer-urls http://localhost:12345 --listen-peer-urls http://localhost:12345 --listen-client-urls http://localhost:12346 --advertise-client-urls http://localhost:12346 --initial-cluster-token etcd-cluster-1 --initial-cluster infra0=http://localhost:12345,infra1=http://localhost:12355,infra2=http://localhost:12365 --initial-cluster-state new

etcd --name infra1 --initial-advertise-peer-urls http://localhost:12355 --listen-peer-urls http://localhost:12355 --listen-client-urls http://localhost:12356 --advertise-client-urls http://localhost:12356 --initial-cluster-token etcd-cluster-1 --initial-cluster infra0=http://localhost:12345,infra1=http://localhost:12355,infra2=http://localhost:12365 --initial-cluster-state new

etcd --name infra2 --initial-advertise-peer-urls http://localhost:12365 --listen-peer-urls http://localhost:12365 --listen-client-urls http://localhost:12366 --advertise-client-urls http://localhost:12366 --initial-cluster-token etcd-cluster-1 --initial-cluster infra0=http://localhost:12345,infra1=http://localhost:12355,infra2=http://localhost:12365 --initial-cluster-state new

3. Na pasta do projeto abra um terminal e execute o servidor: > python server.py

4. Abra mais dois terminais e execute os clients: > python client.py

5. Nos clients, será pedido o a porta do servidor, basta colocar a porta para se conectar.

6. Pronto, tudo certo para jogar, basta escolher uma opção no servidor (Jogar ou recuperar jogo anterior) , caso deseje recuperar um jogo, basta escolher a opção 2 e entrar o nome da sala, que foi dado pelo jogador bola.
