from rest_framework import serializers
from .models import Contribuyente,Direccion,CondContribuyente,ContribuyentePredio,Deuda,EstDeuda,Regimen,PredioExon,Predio,Resolucion,Unidad,ReciboAgua,Recibo,Auxiliar,Distrito,Provincia,Departamento, UsuarioModel

class ContribuyenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribuyente
        fields = '__all__'
    
class DeudaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Deuda
        fields ='__all__'


class RegistroUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = UsuarioModel
        # extra_kwargs > sirve para modificar configuracion de los atributos del modelo
        # puedo indicar el atributo y decirle que quiero que sea 'write_only' (solo escritura) 'read_only' (solo lectura)
        extra_kwargs = {
            'password': {
                'write_only': True
            },
        }
