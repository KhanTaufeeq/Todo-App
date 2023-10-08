from rest_framework import status
from . models import User 
import datetime 
from django.http import HttpResponseServerError
# from config.helpers.error_response import error_response

class CustomLoginRequiredMixin(): 

    def dispatch(self, request, *args, **kwargs): 

        # check if authorization header is present in the request.

        if 'Authorization' not in request.headers:
            return HttpResponseServerError('Please set Auth-Token', status.HTTP_401_UNAUTHORIZED)
        
        # Extract the token form the header. 
        token = request.headers['Authorization'] 

        # Get the user from the database who has the matching token.
        now = datetime.datetime.now() 
        login_user = User.objects.filter(token = token, token_expires__gt = now)

        # If no matching user is found, return an error response.
        if len(login_user) == 0:
            return HttpResponseServerError('The token is invalid or expired.', status.HTTP_401_UNAUTHORIZED)
        
        # set the login_user attribute on the request.
        request.login_user = login_user[0] 

        # call the dispatch method of the parent class.

        return super().dispatch(request, *args, **kwargs)
