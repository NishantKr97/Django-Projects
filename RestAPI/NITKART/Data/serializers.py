from rest_framework import serializers
from .models import DataModel


class DataModelsSerializers(serializers.ModelSerializer):

    class Meta:
        model = DataModel
        #fields = ('username', 'password')            # This data is in Suyash's code(get data)
        fields = '__all__'
