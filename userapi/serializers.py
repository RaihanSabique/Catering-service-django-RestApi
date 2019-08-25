from rest_framework import serializers
from .models import Location

class locationSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Location
        fields = ('location_id', 'level','house_no','street_name',
                  'area_name', 'postal_code','district','long','lat')

#
# class userSerializer(serializers.ModelSerializer):
#     date_joined = serializers.ReadOnlyField()
#
#     class Meta(object):
#         model = User
#         fields = ('user_id','user_name', 'facebook_access_token','contact_no','location_id',
#                   'date_joined', 'profile_image')
#
#         def to_representation(self, instance):
#             self.fields['location_id'] = locationSerializer(read_only=True)
#             return super(userSerializer, self).to_representation(instance)