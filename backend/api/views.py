from product.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.serializers import ProductSerializer
from django.http import JsonResponse


@api_view(['POST'])
def api_home(request, *args, **kwargs):
    data = request.data

    serializer = ProductSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # instance = form.save()
        print(serializer.data)

        return Response(serializer.data)
    return Response({"Invalid": 'not good data'}, status=400)
