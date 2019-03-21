from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Detail, SourceImg, SourceVideo
from .serializers import DetailSerializers, SourceImgSerializers, SourceVideoSerializers

class DetailView(APIView):

    def post(self, request):
        year = request.POST.get('year')
        month = request.POST.get('month')
        if year and month:
            events = Detail.objects.filter(year=year, month=month)
            data = DetailSerializers(events, many=True)

        return Response(data.data)


class ImgView(APIView):

    def post(self, request):
        event_id = request.POST.get('event_id')
        if event_id:
            img_url = SourceImg.objects.filter(event_id=event_id)
            data = SourceImgSerializers(img_url, many=True)

        return Response(data.data)


class VideoView(APIView):

    def post(self, request):
        event_id = request.POST.get('event_id')
        if event_id:
            video_url = SourceVideo.objects.filter(event_id=event_id)
            data = SourceVideoSerializers(video_url, many=True)

        return Response(data.data)
