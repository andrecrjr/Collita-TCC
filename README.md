# tcc-site
# pra entrar na API precisa estar pela branch dev (depois mergirei e criarei outra dev)

Clone esse cretino no PC

tenha o bash instalado ou use o terminal do rwindows python no path [pesquisa aí se não souber](http://lmgtfy.com/?q=python+terminal+windows]) se for o caso

# Vamos lá
primeiro baixe o python mais recente no seu pc da xuxa.

O django ele é uma plataforma via bash então não tem interface bonitinha tem que ser por aqui.


crie o ambiente virtual dentro da pasta(tem que entrar pelo bash na pastinha)
que voce clonou(ou seja o repositorio) (digitar no terminal estará de cinza de fundo)

> python3 -m venv venv 

Esse é o ambiente virtual do python, dentro dele poderá ser instalado as dependencias externas necessarias(django por exemplo)

agora dentro da pasta pelo terminal

> pip install -r requirements_env.txt

beleza ele vai baixar umas parada loca, são as dependencias pro bagulho funfar
agora o django vai funfar no nosso projetinho

> python manage.py migrate

> python manage.py migrate apisite

pronto django criou o banco baseado nos modelos o primeiro é o banco do cadastro de usuario
o segundo é a api que vai ser alimentada.

> python manage.py runserver 

##agora vai rodar o servidor web, só bater o localhost:8000 no navegador

para a api ele baterá no link localhost:8000/api/ já listando todos os usuários para cadastrar
só cadastrar no site (depois vou arrumar pra ele rotear os links da api toda nessa pagina)
localhost:8000/api/<id:usuario>
localhost:8000/api/items/<id:item>



