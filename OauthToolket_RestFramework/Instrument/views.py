from django.http import JsonResponse
from oauth2_provider.contrib.rest_framework import TokenMatchesOASRequirements, OAuth2Authentication
from oauth2_provider.decorators import protected_resource
from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from .models import Instrument
from .serializers import InstrumentSerializer
from api_base.permissions import TokenRequirements


# Test Using ViewSet - using TokenMatchesOASRequirements
class InstrumentViewSet(viewsets.ModelViewSet):
    authentication_classes = [OAuth2Authentication]
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer
    permission_classes = [TokenRequirements]
    required_alternate_scopes = {
        "GET": [["instruments:read"], ["instruments:response"]],
        "POST": [["instruments:write"]],
        "PUT": [["instruments:write"]],
        "DELETE": [["instruments:write"]],
    }

    @action(methods=["get"], detail=False)
    def response_test(self, request):

        token = request.auth
        required_scopes = {
            "GET": [["instruments:response"]]
        }
        if not token:
            data = {
                'msg': "No scope provide"
            }
            return JsonResponse(data)

        for alt in required_scopes["GET"]:
            if token.is_valid(alt):
                data = {
                    'msg': "Success"
                }
                return JsonResponse(data)

        data = {
            'msg': "You do not have this permission"
        }
        return JsonResponse(data)
