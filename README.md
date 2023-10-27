# estacionamento
Projeto final do curso de Django - estacionamento

### Django Admin Super User

user: admin  
e-mail: admin@admin.com  
password: @Admin123  

### Criando novo app

```$ python3 manage.py startapp <app_name> .``` O ponto no final evita criar um subdiretório com o mesmo nome do app

Depois de criar um novo app é necessário registrar em settings.py do projeto na lista INSTALLED_APPS

### Criando tabelas no banco de dados baseadas nas models

Sempre que uma ou mais models forem criadas ou modificadas, precisamos atualiza-las no banco de dados, para isso rodamos os seguintes comandos:  
```$ python3 manage.py makemigrations```  
```$ python3 manage.py migrate```