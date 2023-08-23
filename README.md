<h1 align="center"> Flask - Inicio de sesión y registro </h1>

Inicio de sesion y registro que utiliza cookies para la sesion. <br> 
# Objetivos 
✔️ Uso de cookies. <br>
✔️ Encriptar datos del usuario. <br>
✔️ Validacion y autenticación. <br>
![image](https://github.com/Luguitoo/LoginyRegister.Flask-Python/assets/112581880/86ce4a79-bb5f-4501-920a-1cc3bf4fa7ae)
## :hammer:Librerias necesarias:

pip install flask <br>
mysql-connector-python<br>
pip install Werkzeug<br>
pip install Flask-WTF<br>

## 🛠️  Base de Datos: </h3>

CREATE TABLE `user` ( <br>
  `id_user` int(11) NOT NULL, <br>
  `username` varchar(10) NOT NULL, <br>
  `email` varchar(20) NOT NULL, <br>
  `password` longtext NOT NULL <br>
)  <br>

