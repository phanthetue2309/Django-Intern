from rest_framework import viewsets, permissions
from .models import Instrument
from .serializers import InstrumentSerializer
from rest_framework.permissions import IsAuthenticated


# Test Using ViewSet - using TokenMatchesOASRequirements
class InstrumentViewSet(viewsets.ModelViewSet):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer
    permission_classes = [TokenMatchesOASRequirements]

# Test view_set using TokenHasReadWriteScope
# class InstrumentViewSet(viewsets.ModelViewSet):
#     queryset = Instrument.objects.all()
#     serializer_class = InstrumentSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     required_scopes = []
#
#     def list(self, request, *args, **kwargs):
#         return super(InstrumentViewSet, self).list(request)
#
#     def create(self, request, *args, **kwargs):
#         required_scopes = ['instruments:write']
#         return super(InstrumentViewSet, self).create(request)
