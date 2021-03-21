# Backend Ticke
Proyecto ejemplo, con opcion de login con google y con angular de cierta forma 
embebido en django

### Pre - Requisitos para desarrollar:
* Tener la app en google creada para posteriormente vincularla al proyecto
* Tener instalado pipenv 

### Start/Running
Instalar las dependencias con 
````
pipenv install
`````
Actualizar los datos en el conf.json
````
vim conf/conf.json
`````
Ejecutar los migrations
````
python manage.py migrate
`````
Para ejecutar los test de la api rest
````
python manage.py test apps/soporte/tests

`````

### Proyecto de angular se encuntra en el siguiente link

