from rest_framework.generics import ListAPIView, DestroyAPIView, CreateAPIView, ListCreateAPIView
from .models import Contribuyente,Direccion,CondContribuyente,ContribuyentePredio,Deuda,EstDeuda,Regimen,PredioExon,Predio,Resolucion,Unidad,ReciboAgua,Recibo,Auxiliar,Distrito,Provincia,Departamento, UsuarioModel
from . serializers import ContribuyenteSerializer, DeudaSerializers, RegistroUsuarioSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from .permissions import SoloAdministradores, SoloClientes


class DeudaApiView(ListAPIView):
    queryset = Deuda.objects.all()

    def get(self, request: Request):
        resultado = Deuda.objects.all()
        print(resultado)

        serializador = DeudaSerializers(instance=resultado, many=True)
        print(serializador.data)

        return Response(data={
            'content':serializador.data
        })





class RegistroUsuarioApiView(CreateAPIView):
    def post(self, request: Request):
        serializador = RegistroUsuarioSerializer(data = request.data)
        validacion = serializador.is_valid()

        if validacion is False:
            return Response(data={
                'message': 'error al crear el usuario',
                'content': serializador.errors
            }, status=400)
        
        # inicializo el nuevo usuario con la informacion validada
        nuevoUsuario = UsuarioModel(**serializador.validated_data)
        # ahora genero el hash de la contraseña
        nuevoUsuario.set_password(serializador.validated_data.get('password'))
        # guardo el usuario en la base de datos
        nuevoUsuario.save()

        return Response(data={
            'message': 'Usuario creado exitosamente'
        }, status=201)