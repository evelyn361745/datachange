# coding:utf-8
from rest_framework import serializers
from manna.models import InfoDatabase
class  InfoDatabaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoDatabase
        fields = "__all__"
