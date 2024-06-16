from rest_framework import serializers
from .models import Profesor,avales_tuto,avales_biblio


class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = '__all__'
class TutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = avales_tuto
        fields = '__all__'
class BiblioSerializer(serializers.ModelSerializer):
    class Meta:
        model = avales_biblio
        fields = '__all__'
