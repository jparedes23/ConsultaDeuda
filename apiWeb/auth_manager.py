from django.contrib.auth.models import BaseUserManager

class usuarioManager(BaseUserManager):
    def create_superuser(self, correo, nombre, apellido, tipoUSuario, password):
        if not correo:
            raise ValueError("El Usuario no proporciono el correo")
        
        correo_normalizado = self.normalize_email(correo)

        nuevo_usuario = self.model(correo = correo_normalizado, nombre = nombre, apellido = apellido, tipoUSuario = tipoUSuario )

        nuevo_usuario.set_password(password)
        nuevo_usuario.is_superuser = True
        nuevo_usuario.is_staff = True
        nuevo_usuario.save()
        