# [
#    {
#       "role_name":"access album role",
#       "scopes":[
#          {
#             "albums:read":"read"
#          },
#          {
#             "albums:write":"write"
#          }
#       ]
#    },
#    {
#       "role_name":"access instrument role",
#       "scopes":[
#          {
#             "instruments:read":"read"
#          },
#          {
#             "instruments:write":"write"
#          }
#       ]
#    },
#    {
#       "role_name":"admin_role",
#       "scopes":[
#          {
#             "read":"read"
#          },
#          {
#             "write":"write"
#          }
#       ]
#    }
# ]
from oauth2_provider.scopes import BaseScopes
from accounts.models import Permission


class ScopesBackend(BaseScopes):
    def get_all_scopes(self):
        queryset_scopes = Permission.objects.all().values('scope', 'description')
        scopes = dict()
        for scope in queryset_scopes:
            key = f'{scope.key}'
            value = f'{scope.value}'
            scopes.update({key: value})
        return scopes

    def get_available_scopes(self, application=None, request=None, *args, **kwargs):
        queryset_scopes = Permission.objects.all().values('scope', 'description')
        scopes = dict()
        for scope in queryset_scopes:
            key = f'{scope.get("scope")}'
            value = f'{scope.get("description")}'
            scopes.update({key: value})
        return scopes

    def get_default_scopes(self, application=None, request=None, *args, **kwargs):
        queryset_scopes = Permission.objects.all().values('scope', 'description')
        scopes = dict()
        for scope in queryset_scopes:
            key = f'{scope.key}'
            value = f'{scope.value}'
            scopes.update({key: value})
        return scopes
