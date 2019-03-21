# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     serializers
   Description :
   Author :       wsm
   date：          2019-03-11
-------------------------------------------------
   Change Activity:
                   2019-03-11:
-------------------------------------------------
"""
__author__ = 'wsm'

from rest_framework import serializers
from .models import Detail, SourceImg, SourceVideo

class DetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = "__all__"


class SourceImgSerializers(serializers.ModelSerializer):
    class Meta:
        model = SourceImg
        fields = ['img_url']


class SourceVideoSerializers(serializers.ModelSerializer):
    class Meta:
        model = SourceVideo
        fields = ['video_url']

