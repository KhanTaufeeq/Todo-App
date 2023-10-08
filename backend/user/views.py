from django.shortcuts import render
from . models import User 
from . mixins import CustomLoginRequiredMixin 
from . serializers import UserSerializer, UserSignInSerializer, UserSignUpSerializer 
from rest_framework import generics 
from rest_framework.response import Response
# Create your views here.

class UserSignUp(generics.CreateAPIView):

    queryset = User.objects.all() 
    serializer_class = UserSignUpSerializer  

class UserSignIn(generics.CreateAPIView): 

    queryset = User.objects.all() 
    serializer_class = UserSignInSerializer 

class UserProfile(CustomLoginRequiredMixin, generics.ListAPIView):

    serializer_class = UserSerializer 
    pagination_class = None 

    def get(self, request, *args, **kwargs):
        serializer = UserSerializer([request.login_user],many=True)
        return Response(serializer.data[0])


# The code defines three views:

# UserSignUp: This view allows users to sign up for an account.
# UserSignIn: This view allows users to sign in to their account.
# UserProfile: This view allows users to view their profile information.
# The UserSignUp and UserSignIn views are both subclasses of the generics.CreateAPIView class. This means that they both provide the functionality for creating new objects. In this case, the UserSignUp view creates new users and the UserSignIn view creates new user tokens.

# The UserProfile view is a subclass of the generics.ListAPIView class. This means that it provides the functionality for listing objects. In this case, the UserProfile view lists the profile information of the currently logged-in user.

# The UserProfile view also subclasses the CustomLoginRequiredMixin mixin. This means that the user must be logged in in order to access the view.

# The get() method of the UserProfile view gets the profile information of the currently logged-in user and returns it as a JSON response.

# The get() method of the UserProfile view gets the profile information of the currently logged-in user and returns it as a JSON response. 
# The get() method first creates a UserSerializer object with the currently logged-in user as the data. 
# The get() method then serializes the user data using the UserSerializer object. 
# Finally, the get() method returns a Response object with the serialized user data.
