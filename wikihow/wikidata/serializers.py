from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Content


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ContentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Content
        fields = ('url', 'json_file')
