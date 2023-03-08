from django.urls import path
from .views import RegistroUsuarioApiView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    # cuando se acceda a la ruta /categorias/ se mandara a llamar a la funcionabilidad de nuestro CategoriaApiView
    path('registro/', RegistroUsuarioApiView.as_view()),
    path('login/', TokenObtainPairView.as_view())
]