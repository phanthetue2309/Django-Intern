from oauth2_provider.contrib.rest_framework import TokenMatchesOASRequirements, OAuth2Authentication
from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from .models import Instrument
from .serializers import InstrumentSerializer


# Test Using ViewSet - using TokenMatchesOASRequirements
class InstrumentViewSet(viewsets.ModelViewSet):
    authentication_classes = [OAuth2Authentication]
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer
    permission_classes = [TokenMatchesOASRequirements]
    required_alternate_scopes = {
        "GET": [["instruments:read"], ["instruments:response"]],
        "POST": [["instruments:write"]],
        "PUT": [["instruments:write"]],
        "DELETE": [["instruments:write"]],
    }
