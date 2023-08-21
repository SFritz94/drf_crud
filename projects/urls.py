from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()#Crea el crud

router.register('api/projects', ProjectViewSet, 'projects')#Se le pasa la ruta, bajo que viewset va a estar trabajando y el nombre de la ruta

urlpatterns = router.urls#Exporto las urls que se generaron