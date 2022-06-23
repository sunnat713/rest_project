from rest_framework import generics
from rest_framework.response import Response
from product.models import Product
from product.serializers import ProductSerializer, ProductInlineSerializer
from . import client


class SearchListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        user = None
        if request.user.is_authenticated:
            user = request.user.username
        query = request.GET.get('q')
        public = str(request.GET.get('public')) != '0'
        tag = request.GET.get('tag') or None
        if not query:
            return Response({'message': "product not found"}, status=400)
        results = client.perform_search(query, tags=tag, user=user, public=public)
        return Response(results)


class SearchListOldView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        results = Product.objects.none()
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        if q is not None:

            user = None
            if self.request.user.is_authenticated:
                user = self.request.user

            results = qs.search(q, user=user)
        return results
