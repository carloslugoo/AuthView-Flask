from wtforms import Form
from wtforms import StringField, EmailField, PasswordField
from wtforms import validators

class User(Form):
 username = StringField('Usuario:',
                        [validators.length(min=4, max=12, message='Ingrese un usuario de 4 a 25 letras!..'),
                         validators.data_required(message='Ingrese un Usuario!')])


 email = EmailField('Usuario:',
                        [validators.length(min=4, max=25, message='Ingrese un usuario de 4 a 25 letras!..'),
                         validators.data_required(message='Ingrese un Usuario!')])


 password = PasswordField('Contraseña:',
                    [validators.data_required(message='Ingrese un Contraseña!'),
                     validators.length(min=4, max=25, message='Ingrese un contraseña de 4 a 25 letras!..')])

 confirmpassword = PasswordField('Confirmar Contrasena',
                          [validators.data_required(message='Ingrese un Contraseña!'),
                           validators.length(min=4, max=25, message='Ingrese un contraseña de 4 a 25 letras!..')])


