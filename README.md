# tcc-site

Estrutura das pastas

Appsite -> Settings do django(configuração principal do projeto, não alterar, grato)

Apisite -> API do site para o jogo e vice versa, onde está toda a logica de construção da API

Appsite -> Site do TCC onde está toda a logica para o site

Clone esse repositorio no PC

tenha o bash instalado ou use o terminal do rwindows python no path [pesquisa aí se não souber](http://lmgtfy.com/?q=python+terminal+windows) se for o caso

Vamos lá
1. Primeiro baixe o python mais recente no seu pc da xuxa.. 
 O django ele é uma plataforma via bash então não tem interface bonitinha tem que pelo terminal.

O ambiente virtual python é criado pelo terminal, você deve clonar esse repositorio no seu pc.
Com esse projeto já no seu computador, pelo terminal entre no diretorio do projeto no pc:
Digite:
> python3 -m venv venv 

Isso criará o ambiente virtual do python, dentro dele poderá ser instalado as dependencias externas necessarias(django por exemplo)

agora dentro da pasta pelo terminal voce vai precisar ativar esse ambiente do python dentro da pasta.

No prompt windows:

> venv\Scripts\activate

No bash pro windows 10 creio eu:
> . venv\Scripts\activate

Agora vai ter que instalar as dependencias desse ambiente que necessita espero que já esteja na branch de dev usando aquele turtoise(virtual env é tal qual java com maven). 

Agora só digitar no terminal:
> pip install -r requirements_env.txt

Ele vai baixar umas parada loca, são as dependencias para o site e API funcionar

Ao terminar você terá que subir o banco, no django ele fará esse trabalho sozinho mandando os seguintes comandos no terminal:

> python manage.py migrate

> python manage.py migrate apisite

pronto django criou o banco baseado nos modelos o primeiro é o banco do cadastro de usuario
o segundo é a api que vai ser alimentada.

> python manage.py runserver 

Os endereço da API:

> http:localhost:8000/api/{params}

> http:localhost:8000/api/items/{params}

> http:localhost:8000/api/inventario/{params}

Autenticação - POST no link abaixo com usuario e senha cadastrado

> localhost:8000/api/auth/login/

Retornará o token e o id do usuário para utilização geral do jogo.

Para as transações, o website irá redirecionar um item para o pagseguro, movido a microtransações.


