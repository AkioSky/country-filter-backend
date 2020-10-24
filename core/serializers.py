from rest_framework import serializers
from .models import Country


class CountrySerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    sub_category = serializers.SerializerMethodField()

    def get_category(self, obj):
        print(obj.pk)
        first_char = obj.name[0].upper()
        categories = Country.CATEGORY
        result = [category for category in categories if first_char in category]
        return result[0] if result else first_char

    def get_sub_category(self, obj):
        return obj.name[0].upper()

    class Meta:
        model = Country
        fields = ("id", "name", "banned", "category", "sub_category")


class CountryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("id", "banned")
