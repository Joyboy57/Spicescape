from django.db import models
from geopy.distance import geodesic
from django.db.models import Q

# Create your models here.
class FoodTruckInfo(models.Model):
    location_id = models.IntegerField()
    applicant = models.CharField(max_length=255)
    facility_type = models.CharField(max_length=100)
    cnn = models.IntegerField()
    location_description = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    block_lot = models.CharField(max_length=255)
    block = models.CharField(max_length=50)
    lot = models.CharField(max_length=50)
    permit = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    food_items = models.TextField()
    x_coordinates = models.DecimalField(null=True, max_digits=18, decimal_places=10)
    y_coordinates = models.DecimalField(null=True, max_digits=18, decimal_places=10)
    latitude = models.DecimalField(max_digits=18, decimal_places=15)
    longitude = models.DecimalField(max_digits=18, decimal_places=15)
    schedule = models.TextField()
    days_hours = models.TextField(null=True, blank=True)
    noi_sent = models.CharField(max_length=255, null=True, blank=True)
    approved = models.DateField(null=True, blank=True)
    received = models.DateField(null=True, blank=True)
    prior_permit = models.IntegerField(null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255)
    fire_prevention_districts = models.IntegerField(null=True)
    police_districts = models.IntegerField(null=True)
    supervisor_districts = models.IntegerField(null=True)
    zip_codes = models.IntegerField(null=True)
    neighborhoods_old = models.IntegerField(null=True)

    @classmethod
    def get_nearby_trucks(cls, latitude, longitude, radius):
        """
        Retrieve nearby food trucks within a specified radius (in miles) of a given location
        with optimized pre-filtering using a bounding box.
        """
        # Define a rough bounding box (latitude/longitude range) around the user's location
        lat_range = radius / 69.0  # Roughly 69 miles per degree latitude
        lon_range = radius / (69.0 * abs(latitude))

        # Pre-filter trucks within bounding box
        bounding_box_trucks = cls.objects.filter(
            latitude__gte=latitude - lat_range, latitude__lte=latitude + lat_range,
            longitude__gte=longitude - lon_range, longitude__lte=longitude + lon_range
        )

        # Calculate exact distances for bounding box trucks
        user_location = (latitude, longitude)
        nearby_trucks = []
        for truck in bounding_box_trucks:
            truck_location = (truck.latitude, truck.longitude)
            distance = geodesic(user_location, truck_location).miles
            if distance <= radius:
                truck.distance = distance
                nearby_trucks.append(truck)

        return nearby_trucks

    @classmethod
    def filter_by_cuisine(cls, cuisine_type):
        """
        Filter food trucks by a specific cuisine type based on food items served,
        with improved token-based matching for accuracy.
        """
        # Split input and food items into tokens
        tokens = cuisine_type.lower().split()
        query = Q()
        for token in tokens:
            query |= Q(food_items__icontains=token)
        
        # Retrieve trucks that match any of the cuisine tokens
        filtered_trucks = cls.objects.filter(query)
        return filtered_trucks

    def __str__(self):
        return self.applicant
