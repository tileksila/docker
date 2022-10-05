from email import message
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from mainapp.serializers import  InnerTraid, InnerTraidDashboardSerializer
from rest_framework import filters



class InnerTraidDashboardView(ModelViewSet):
    queryset = InnerTraid.objects.all()
    serializer_class = InnerTraidDashboardSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('status', )

    def get_permissions(self):
        if self.action == 'partial_update' or self.action == 'update':
            permission_classes = (IsAdminUser,)
        else:
            permission_classes = (AllowAny,)
        return [permission() for permission in permission_classes]

    @action(methods=['get', ], detail=False)
    def get_date_range_trainds(self, request, *args, **kwargs):
        date_create = request.query_params.get('date_from', None)
        date_update = request.query_params.get('date_to', None)
        if date_create == None or date_update == None:
            return Response({'message': 'Set dates in query pararms'})
        elif date_create == None and date_update == None:
            return Response({'message': 'Set dates in query pararms'})
        inner_traides = InnerTraid.objects.filter(date__gte=date_create, date__lte=date_update)
        return Response(InnerTraidDashboardSerializer(inner_traides, many=True).data)