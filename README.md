<h1 align="center"> Flask - Inicio de sesión y registro </h1>

Inicio de sesion y registro que utiliza cookies para la sesion. 

## :hammer:Librerias necesarias:

pip install flask <br>
mysql-connector-python<br>
pip install Werkzeug<br>
pip install Flask-WTF<br>


<h3>🛠️  Base de Datos: </h3>

CREATE TABLE `user` ( <br>
  `id_user` int(11) NOT NULL, <br>
  `username` varchar(10) NOT NULL, <br>
  `email` varchar(20) NOT NULL, <br>
  `password` longtext NOT NULL <br>
)  <br>
