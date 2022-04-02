from rest_framework import serializers
from receptai.models import Receptas, Produktas 

class ReceptasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Receptas
        fields = '__all__'
