from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenMatchesOASRequirements
from rest_framework import viewsets, permissions
from .models import Instrument
from .serializers import InstrumentSerializer


# Test Using ViewSet - using TokenMatchesOASRequirements
class InstrumentViewSet(viewsets.ModelViewSet):

    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer
    permission_classes = [TokenMatchesOASRequirements]
    # Phân scope cho từng cụm
    required_alternate_scopes = {
        "GET": [["instruments:read"]],
        "POST": [["instruments:write"]],
        "PUT": [["instruments:write"]],
        "DELETE": [["instruments:write"]],
    }


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
