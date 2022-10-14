from rest_framework.generics import RetrieveAPIView, UpdateAPIView, ListCreateAPIView, ListAPIView, DestroyAPIView
from .models import Product
from rest_framework import generics, mixins, authentication
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.permissions import SAFE_METHODS
from api.mixins import StaffEditorMixin, UserQuerySetMixin
from .permissions import IsOwner
from django_filters.rest_framework import DjangoFilterBackend


class ProductMixinsView(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                        generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)


class ProductListCreateAPIView(UserQuerySetMixin, StaffEditorMixin, ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        print(self.request.data)
        if content is None:
            content = title
        serializer.save(content=content, user=self.request.user)

    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     request = self.request
    #     user = request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     return qs.filter(user=request.user)


class ProductDetail(UserQuerySetMixin, StaffEditorMixin, RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdate(UserQuerySetMixin, StaffEditorMixin, UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class ProductDeleteView(UserQuerySetMixin, StaffEditorMixin, DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


# class ProductListView(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#     def post(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    if method == "GET":
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)

        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
    if method == 'POST':

        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content, title=title)

            return Response(serializer.data)
        return Response({"Invalid": 'not good data'}, status=400)


from django.contrib.auth import get_user_model
User = get_user_model()


# class ProductAllView(ListAPIView ):
#     queryset = Product.objects.all()
#     serializer_class = ProductAllSerializers
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['user_id']
#     permission_classes = [IsOwner]

    # def get_queryset(self, *args, **kwargs):
    #     # Get queryset of User Model
    #     queryset = Product.objects.all()
    #
    #     # Try to fetch the user_id param from url
    #     user_id = self.request.query_params.get('user', None)
    #
    #
    #    # def get_queryset(self, *args, **kwargs):
    #     # Get queryset of User Model
    #     queryset = Product.objects.all()
    #
    #     # Try to fetch the user_id param from url
    #     user_id = self.request.query_params.get('user_id', None)
    #
    #
    #
    #     # If user_id param is not None, filter using the obtained user_id
    #     if user_id is not None:
    #         queryset = Product.objects.filter(user_id=user_id)
    #
    #     return queryset

    #     # If user_id param is not None, filter using the obtained user_id
    #     if user_id is not None:
    #         queryset = Product.objects.filter(user_id=user_id)
    #
    #     return queryset
