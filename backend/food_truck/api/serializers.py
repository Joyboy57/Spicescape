from rest_framework import serializers
from food_truck.models import FoodTruckInfo

class FoodTruckInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodTruckInfo
        fields = "__all__"

class FoodTruckInfoBulkSerializer(serializers.ListSerializer):
    child = FoodTruckInfoSerializer()

    def create(self, validated_data):
        # Bulk create food trucks
        food_trucks = [FoodTruckInfo(**item) for item in validated_data]
        return FoodTruckInfo.objects.bulk_create(food_trucks)
