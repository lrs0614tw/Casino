from rest_framework import serializers
from turntableApp.models import heysongUid


class heysongUidSerializer(serializers.ModelSerializer):
    class Meta:
        model = heysongUid
        # fields = '__all__'
        fields = ('id', 'uid','time')