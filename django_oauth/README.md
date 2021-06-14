#Oauth2 Learning

Link Project : 

    https://halvorboe.medium.com/guide-to-an-oauth2-api-with-django-6ba66a31d6d


Remember when using this link you have to change host from : 0.0.0.0 to 127.0.0.1
## Register App
- Login
- To register new application using : http://127.0.0.1:8000/o/applications/register/
- Then we have this : 
    ![register_app](image/register_app.PNG)
- Add client key : vPFYpy2nq43NOWrWYPbIG0JLMydXeU0B0Z6bGAGE

## Authorize App 
- Go to this link : http://127.0.0.1:8000/o/authorize/?response_type=code&client_id=vPFYpy2nq43NOWrWYPbIG0JLMydXeU0B0Z6bGAGE&redirect_uri=http://127.0.0.1:8000/noexist/callback
- We have this in link : 
    + response_type: code
    + client_id: **vPFYpy2nq43NOWrWYPbIG0JLMydXeU0B0Z6bGAGE**
    + redirect_uri: http://127.0.0.1:8000/noexist/callback
- After authorize we have added data to grand like this : 
    ![grant](image/grants_add.PNG)
- Detail of this : 
    ![grant](image/detail_grants.PNG)


## Request Access Token 
Run in cmd : 
```
curl -X POST -d "grant_type=password&username=tue&password=Thetue2309" -u"vPFYpy2nq43NOWrWYPbIG0JLMydXeU0B0Z6bGAGE:3C0LwDBzdVmtlO2Q1X0thsHpLtfugSEUTO4YVlK8V3cL0Gk8OlUKFIv1KDv7aDOxMYjAGtqX85r4PCxsHJXAhTU2ezU8f5uPvfrGH9J8XsHodvF2BMtTIX116AeGucLs" http://localhost:8000/o/token/

```
Then you will have access token and refresh token: 
    ![access_token](image/access_token.PNG)

D0RCqjc7Ffpe5Hp5BhCKBOdK7DxUxE

## Credential App 
- Add client key : Q7UsRYuJHAofupiRHiAQ4lXslwsMjDDa6Rc21Myy
- Go to this link : http://127.0.0.1:8000/o/authorize/?response_type=code&client_id=Q7UsRYuJHAofupiRHiAQ4lXslwsMjDDa6Rc21Myy&redirect_uri=http://127.0.0.1:8000/noexist/callback

    + User: the owner of the Application (e.g. a developer, or the currently logged in user.)
    + Redirect uris: Applications must register at least one redirection endpoint before using the authorization endpoint. The Authorization Server will deliver the access token to the client only if the client specifies one of the verified redirection uris. For this tutorial, paste verbatim the value http://django-oauth-toolkit.herokuapp.com/consumer/exchange/
    + Client type: this value affects the security level at which some communications between the client application and the authorization server are performed. For this tutorial choose Confidential.
    + Authorization grant type: choose Authorization code
    + Name: this is the name of the client application on the server, and will be displayed on the authorization request page, where users can allow/deny access to their data.
    
Test Register 

    curl -d "username=thetue&password=Thetue2309" "127.0.0.1:8000/authentication/register/"

    {
    "access_token":"9oD074E6OZixcuagEa1DGfpuYrr9B0",
    "expires_in":36000,
    "token_type":"Bearer",
    "scope":"read write",
    "refresh_token":"iHZkLDk6AZTGOl8Jr4sRpVCGTM7r5V"
    }

- Create the unicorn :
    
      curl -H "Authorization: Bearer 9oD074E6OZixcuagEa1DGfpuYrr9B0" -d "name=TheTue&age=34" 127.0.0.1:8000/api/unicorn-model-viewset/

    + Result : 
    {"name":"TheTue","age":34}

- Show all unicorn : 
  
        curl -H "Authorization: Bearer 9oD074E6OZixcuagEa1DGfpuYrr9B0" 127.0.0.1:8000/api/unicorn-model-viewset/
