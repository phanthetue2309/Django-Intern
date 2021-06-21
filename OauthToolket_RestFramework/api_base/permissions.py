from django.core.exceptions import ImproperlyConfigured
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAuthenticated
import logging

log = logging.getLogger("oauth2_provider")


class TokenRequirements(BasePermission):

    def has_permission(self, request, view):
        token = request.auth

        if not token:
            return False

        if hasattr(token, "scope"):  # OAuth 2
            required_alternate_scopes = self.get_required_alternate_scopes(request, view)

            m = request.method.upper()
            if m in required_alternate_scopes:
                log.debug(
                    "Required scopes alternatives to access resource: {0}".format(
                        required_alternate_scopes[m]
                    )
                )
                for alt in required_alternate_scopes[m]:
                    if token.is_valid(alt):
                        return True
                return False
            else:
                log.warning("no scope alternates defined for method {0}".format(m))
                return False

        assert False, (
            "TokenMatchesOASRequirements requires the"
            "`oauth2_provider.rest_framework.OAuth2Authentication` authentication "
            "class to be used."
        )

    def get_required_alternate_scopes(self, request, view):
        try:
            return getattr(view, "required_alternate_scopes")
        except AttributeError:
            raise ImproperlyConfigured(
                "TokenMatchesOASRequirements requires the view to"
                " define the required_alternate_scopes attribute"
            )
