from abc import ABC

from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse
from .validators import validate_title_no_hello, unique_product_title
from api.serializers import UserPublicSerializer


class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk', read_only=True)
    title = serializers.CharField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True)
    # related_products = ProductInlineSerializer(source='user.product_set.all', read_only=True, many=True)
    # my_user_data = serializers.SerializerMethodField(read_only=True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')
    delete_url = serializers.HyperlinkedIdentityField(view_name='product-delete', lookup_field='pk')
    title = serializers.CharField(validators=[validate_title_no_hello, unique_product_title])

    # email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Product
        fields = [
            'owner',
            'url',
            'edit_url',
            'delete_url',
            'pk',
            'title',
            # 'name',
            'content',
            'price',
            'sale_price',
            'my_discount',
            'public',
            # 'my_user_data',
            # 'related_products',
            # 'email'
        ]

    #
    # def create(self, validated_data):
    #     obj = super().create(validated_data)
    #     # return Product.objects.create(validated_data)
    #     return obj
    #
    # def update(self, instance, validated_data):
    #     email = validated_data.pop('email')
    #
    #     return super().update(instance, validated_data)

    # def validate_title(self, value):
    #     request = self.context.get('request')
    #     user = request.user
    #     qs = Product.objects.filter(user=user, title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f'{value} is already a product name')
    #     return value

    # def get_my_user_data(self, obj):
    #     return {
    #         'username': obj.user.username
    #     }

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('product-edit', kwargs={"pk": obj.pk}, request=request)
