from rest_framework.authentication import TokenAuthentication as token
from rest_framework.authtoken.models import Token


class TokenAuthentication(token):
    keyword = 'Bearer '
