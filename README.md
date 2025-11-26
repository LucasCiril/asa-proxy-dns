<html  lang="pt-br">
<head>
</head>

<body>
    <h1> ☆ Projeto DNS + HTTP + Proxy Reverso e Automatização ☆</h1><br>
    <h3 style="text-align:center" >Saudações, Invocador! Vejo que retornou e está bem. Lucas Cirilo aqui, novamente. </a></h3>
    <img class="hi" src="https://github.com/LucasCiril/Asa-IFRN/blob/main/imagens/oi-meu.gif" width="300" heigth="300" /> 
    <p>&emsp;&emsp;Este README informa como foi feito o projeto sobre HTTP, DNS, Proxy Reverso e automatização, utilizando Docker e Shell Script, para a matéria de Administração de Sistemas Abertos. Segue abaixo o escopo do que foi pedido pelo professor:
        </p>
  
<p>Essa atividade tem como objetivo implementar um servidor web usando Docker.

O que fazer:


1- Repositório público no github (asa-proxy-dns) contendo todos os arquivos da infraestrutura;


2- Implementar o estrutura web com 01 proxy reverso e 02 servidores de aplicação;


3- Implementar o estrutura com 01 servidor de DNS primário com zona de resolução direta;


4- Script de automatização de criação, exclusão, início e parada dos serviços;


5- Domínios de DNS:
- Composto pelo primeiro nome do aluno + .asa.br (Ex.: edmar.asa.br)


O que entregar:
- Repositório completo (Github)</p>
<img src="https://github.com/LucasCiril/asa-proxy-dns/blob/main/images/example.png" style="width:70%"><br>
<p>Para executar testes em sua máquina, basta clonar o repositório e ter o Docker Desktop instalado em sua máquina. Antes de qualquer teste, abra o seu CMD e digite ipconfig. Você precisará trocar o IP que está setado no arquivo db.asa.br pelo ip da sua máquina.<br>
<img src="https://github.com/LucasCiril/asa-proxy-dns/blob/main/images/att%20captura.png" style="width:70%"><br>

Uma vez trocado, você já pode iniciar um interpretador de comandos Shell. Normalmente, o VScode já disponibiliza o PowerShell/Git Bash. Todos os comandos estão automatizados, e aqui estão a lista de cada um:

1- ./ez.sh criar         
- #build as imagens e inicia o serviço<br>

2- ./ez.sh parar
- #para o serviço sem o excluir<br>

3- ./ez.sh iniciar
- #caso você tenha parado o serviço, esse comando retornará os containers à ativa<br>

4- ./ez.sh excluir       
- #exclui os containers criados<br>

5- ./ez.sh logs          
- #mostra os logs de todos os containers ups<br>

6- ./ez.sh reiniciar     
- #reinicia os containers<br>


Por fim, use o comando para criar e após, você irá precisar trocar o seu servidor de DNS padrão para colocar em Localhost (127.0.0.1).

<img src="https://github.com/LucasCiril/asa-proxy-dns/blob/main/images/trocar%20dns.png" style="width:40%"><br>

E então, você já pode pesquisar pelo endereço em seu navegador de preferência:

<img src="https://github.com/LucasCiril/asa-proxy-dns/blob/main/images/web1.png" style="width:70%"><br>
www.cirilo.asa.br

<img src="https://github.com/LucasCiril/asa-proxy-dns/blob/main/images/web2.png" style="width:70%"><br>
mail.cirilo.asa.br

<h3 style="text-align:center" >☆   Finalizamos então por aqui. Até a próxima aventura, Invocador!   ☆ </a></h3>

 <img class="hi" src="https://github.com/LucasCiril/asa-proxy-dns/blob/main/images/backyardigans-pablo-austin-cute-dance-x4t43fgxt1lkiqu9.gif" width="300" heigth="300" /><br>