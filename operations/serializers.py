from .models import library_item
from pynamodb.attributes import *
from rest_framework import serializers
import uuid

class item_serializer(serializers.ModelSerializer):


    class Meta:
        model = library_item
        fields = {'title','author','isbn','url','image_url','create_date','modified_date','created_ts','modified_ts','uid',
                  'active','department'}


    def create(self,validated_data):
        '''given validated data instance is created'''
        validated_data.uid = uuid.uuid4()
        return library_item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title) #if the validated instance doesnt have title, instance title is retained
        instance.author = validated_data.get('author',instance.author)
        instance.isbn = validated_data.get('isbn',instance.isbn)
        instance.url = validated_data.get('url',instance.url)
        instance.image_url = validated_data.get('image_url',instance.image_url)
        instance.create_date = validated_data.get('create_date',instance.create_date)
        instance.modified_date = validated_data.get('modified_date',instance.modified_date)
        instance.created_ts = validated_data.get('created_ts',instance.created_ts)
        instance.modified_ts = validated_data.get('modified_ts',instance.modified_ts)
        instance.uid = validated_data.get('uid',instance.uid)
        instance.active = validated_data.get('active',instance.active)
        instance.department = validated_data.get('department',instance.department)



