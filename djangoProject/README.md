# Django OAuth 2 

## Authorization Code

- First we go to this link and create app : 
  ```
  http://127.0.0.1:8000/o/applications/register/ 
  ```
  
- Setting the app with uri-direct : 
  + http://127.0.0.1:8000/noexist/callback
  + Client ID=vW1RcAl7Mb0d5gyHNQIAcH110lWoOW2BmWJIero8
  + Client SECRET=DZFpuNjRdt5xUEzxXovAp40bU3lQvoMvF3awEStn61RXWE0Ses4RgzHWKJKTvUCHfRkhcBi3ebsEfSjfEO96vo2Sh6pZlxJ6f7KcUbhvqMMPoVxRwv4vfdWEoWMGPeIO
  + Client type : Confidential
  + Authorization grant type : Authorization code
  

- After saving go to this link :
  ```
  http://127.0.0.1:8000/o/authorize/?response_type=code&client_id=vW1RcAl7Mb0d5gyHNQIAcH110lWoOW2BmWJIero8&redirect_uri=http://127.0.0.1:8000/noexist/callback
  ```

![img.png](img.png)
  * After press authorize we have this code : 
    ![img_2.png](img_2.png)
  
    This is code : a1amczIAUbc0E15F87EXkUM0tqId4h
  
- Run in cmd 
  ```
  curl -X POST -H "Cache-Control: no-cache" -H "Content-Type: application/x-www-form-urlencoded" "http://127.0.0.1:8000/o/token/" -d "client_id"="vW1RcAl7Mb0d5gyHNQIAcH110lWoOW2BmWJIero8" -d "client_secret"="DZFpuNjRdt5xUEzxXovAp40bU3lQvoMvF3awEStn61RXWE0Ses4RgzHWKJKTvUCHfRkhcBi3ebsEfSjfEO96vo2Sh6pZlxJ6f7KcUbhvqMMPoVxRwv4vfdWEoWMGPeIO" -d "code"="a1amczIAUbc0E15F87EXkUM0tqId4h" -d "redirect_uri"="http://127.0.0.1:8000/noexist/callback" -d "grant_type"="authorization_code"
  ```
- After running in cmd we have : 
  ![img_3.png](img_3.png)
 
  ```
  {
    "access_token": "qwrf8CirPFR9UXXpUFEJOdvtZ7Xr1z", 
    "expires_in": 36000, 
    "token_type": "Bearer", 
    "scope": "read write", 
    "refresh_token": "xVaBe5e9Nv4wlU62Gt3Jl6m0ybqSJz"
  }
  ```

## Client Credential

- First we go to this link and create app : 
  ```
  http://127.0.0.1:8000/o/applications/register/ 
  ```
  
- Setting the app with uri-direct : 
  + http://127.0.0.1:8000/noexist/callback
  + Client ID=axXSSBVuvOyGVzh4PurvKaq5MHXMm7FtrHgDMi4u
  + Client SECRET=1fuv5WVfR7A5BlF0o155H7s5bLgXlwWLhi3Y7pdJ9aJuCdl0XV5Cxgd0tri7nSzC80qyrovh8qFXFHgFAAc0ldPNn5ZYLanxSm1SI1rxlRrWUP591wpHDGa3pSpB6dCZ
  + Client type : Confidential
  + Authorization grant type : client-credentials
  
- We need to encode client_id and client_secret as HTTP base authentication encoded in base64 I use the following code to do that.
- Running shell to code this : 
  ```
  >>> import base64
  >>> client_id = "axXSSBVuvOyGVzh4PurvKaq5MHXMm7FtrHgDMi4u"
  >>> secret = "1fuv5WVfR7A5BlF0o155H7s5bLgXlwWLhi3Y7pdJ9aJuCdl0XV5Cxgd0tri7nSzC80qyrovh8qFXFHgFAAc0ldPNn5ZYLanxSm1SI1rxlRrWUP591wpHDGa3pSpB6dCZ"
  >>> credential = "{0}:{1}".format(client_id, secret)
  >>> base64.b64encode(credential.encode("utf-8"))
  ```
- Final we will have this : 
  ```
  b'YXhYU1NCVnV2T3lHVnpoNFB1cnZLYXE1TUhYTW03RnRySGdETWk0dToxZnV2NVdWZlI3QTVCbEYwbzE1NUg3czViTGdYbHdXTGhpM1k3cGRKOWFKdUNkbDBYVjVDeGdkMHRyaTduU3pDODBxeXJvdmg4cUZYRkhnRkFBYzBsZFBObjVaWUxhbnhTbTFTSTFyeGxScldVUDU5MXdwSERHYTNwU3BCNmRDWg=='
  ```
- To start the Client Credential flow you call /token/ endpoint direct:
  ```
  curl -X POST -H "Authorization: Basic YXhYU1NCVnV2T3lHVnpoNFB1cnZLYXE1TUhYTW03RnRySGdETWk0dToxZnV2NVdWZlI3QTVCbEYwbzE1NUg3czViTGdYbHdXTGhpM1k3cGRKOWFKdUNkbDBYVjVDeGdkMHRyaTduU3pDODBxeXJvdmg4cUZYRkhnRkFBYzBsZFBObjVaWUxhbnhTbTFTSTFyeGxScldVUDU5MXdwSERHYTNwU3BCNmRDWg==" -H "Cache-Control: no-cache" -H "Content-Type: application/x-www-form-urlencoded" "http://127.0.0.1:8000/o/token/" -d "grant_type"="client_credentials"
  ```
  ![img_4.png](img_4.png)
  ```
  {
    "access_token": "yXHF3HXUKZYWp4QuSmOIYmdDIoZ5jH", 
    "expires_in": 36000, 
    "token_type": "Bearer", 
    "scope": "read write"
  }
  ```
  
# Tutorial 

## Part 1 - Make a Provider in a Minute

- install django-oauth-toolkit and django-cors-middleware:
  ```
  pip install django-oauth-toolkit django-cors-middleware
  ```
  
- Start a Django project, add oauth2_provider and corsheaders to the installed apps, and enable admin:
  ```
  INSTALLED_APPS = {
      'django.contrib.admin',
      # ...
      'oauth2_provider',
      'corsheaders',
  }
  ```
  
- Include the Django OAuth Toolkit urls in your urls.py, choosing the urlspace you prefer. For example:

  ```
  urlpatterns = [
      path("admin", admin.site.urls),
      path("o/", include('oauth2_provider.urls', namespace='oauth2_provider')),
      # ...
  ]
  ```

- Include the CORS middleware in your settings.py:
  ```
  MIDDLEWARE = (
      # ...
      'corsheaders.middleware.CorsMiddleware',
      # ...
  )
  ```
- Allow CORS requests from all domains (just for the scope of this tutorial):

  ```
  CORS_ORIGIN_ALLOW_ALL = True
  ```
  
- Include the required hidden input in your login template, registration/login.html. The {{ next }} template context variable will be populated with the correct redirect value. See the Django documentation for details on using login templates.

  ```
  <input type="hidden" name="next" value="{{ next }}" />
  ```

As a final step, execute the migrate command, start the internal server, and login with your credentials.


## Part 2 - protect your APIs

### Make your API

- Django OAuth Toolkit provides a set of generic class based view you can use to add OAuth behaviour to your views. Open your views.py module and import the view:

  ```
  from oauth2_provider.views.generic import ProtectedResourceView
  from django.http import HttpResponse
  ```
  
- Then create the view which will respond to the API endpoint:
  ```
  class ApiEndpoint(ProtectedResourceView):
      def get(self, request, *args, **kwargs):
          return HttpResponse('Hello, OAuth2!')
  ```
  

- That’s it, our API will expose only one method, responding to GET requests. Now open your urls.py and specify the URL this view will respond to:

  ```
  from django.urls import path, include
  import oauth2_provider.views as oauth2_views
  from django.conf import settings
  from .views import ApiEndpoint
  
  # OAuth2 provider endpoints
  oauth2_endpoint_views = [
      path('authorize/', oauth2_views.AuthorizationView.as_view(), name="authorize"),
      path('token/', oauth2_views.TokenView.as_view(), name="token"),
      path('revoke-token/', oauth2_views.RevokeTokenView.as_view(), name="revoke-token"),
  ]
  
  if settings.DEBUG:
      # OAuth2 Application Management endpoints
      oauth2_endpoint_views += [
          path('applications/', oauth2_views.ApplicationList.as_view(), name="list"),
          path('applications/register/', oauth2_views.ApplicationRegistration.as_view(), name="register"),
          path('applications/<pk>/', oauth2_views.ApplicationDetail.as_view(), name="detail"),
          path('applications/<pk>/delete/', oauth2_views.ApplicationDelete.as_view(), name="delete"),
          path('applications/<pk>/update/', oauth2_views.ApplicationUpdate.as_view(), name="update"),
      ]
  
      # OAuth2 Token Management endpoints
      oauth2_endpoint_views += [
          path('authorized-tokens/', oauth2_views.AuthorizedTokensListView.as_view(), name="authorized-token-list"),
          path('authorized-tokens/<pk>/delete/', oauth2_views.AuthorizedTokenDeleteView.as_view(),
              name="authorized-token-delete"),
      ]
  
  urlpatterns = [
      # OAuth 2 endpoints:
      # need to pass in a tuple of the endpoints as well as the app's name
      # because the app_name attribute is not set in the included module
      path('o/', include((oauth2_endpoint_views, 'oauth2_provider'), namespace="oauth2_provider")),
      path('api/hello', ApiEndpoint.as_view()),  # an example resource endpoint
  ]
  ```

- You will probably want to write your own application views to deal with permissions and access control, but the ones packaged with the library can get you started when developing the app.

- Since we inherit from ProtectedResourceView, we’re done, and our API is OAuth2 protected - for the sake of the lazy programmer.

## Part 3 - OAuth2 token authentication
### Setup a provider

- To enable OAuth2 token authentication you need a middleware that checks for tokens inside requests, and a custom authentication backend which takes care of token verification. In your settings.py:

  ```
  AUTHENTICATION_BACKENDS = (
      'oauth2_provider.backends.OAuth2Backend',
      # Uncomment following if you want to access the admin
      #'django.contrib.auth.backends.ModelBackend'
      '...',
  )
  
  MIDDLEWARE = (
      '...',
      'oauth2_provider.middleware.OAuth2TokenMiddleware',
      '...',
  )
  ```
  
## Part 4 - Revoking an OAuth2 Token
