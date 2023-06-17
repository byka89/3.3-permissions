from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as fil

from .permissions import IsOwner
from .serializers import AdvertisementSerializer
from .models import Advertisement
from .filters import AdvertisementFilter


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [fil.DjangoFilterBackend]
    filterset_class = AdvertisementFilter

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров


    def get_permissions(self):
        """Получение прав для действий."""
        print(self.action)
        if self.action in ["create", "update", "partial_update", "destroy"]:
            permission_classes = [IsAuthenticated, IsOwner]
            print('up')
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]
            print('list')

        return [permission() for permission in permission_classes]