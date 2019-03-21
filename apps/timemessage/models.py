from django.db import models


# Create your models here.

class Detail(models.Model):
    year = models.CharField(max_length=100, verbose_name='事件发生年代', null=True, blank=True)
    month = models.CharField(max_length=100, verbose_name='事件发生月份', null=True, blank=True)
    location = models.CharField(max_length=50, verbose_name='事件发生地点', null=True, blank=True)
    event_name = models.CharField(max_length=50, verbose_name='事件名称', null=True, blank=True)
    event_message = models.TextField(verbose_name='事件内容', null=True, blank=True)

    class Meta:
        verbose_name = '事件信息记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.event_name


class SourceImg(models.Model):
    event_id = models.ForeignKey(Detail, on_delete=models.CASCADE)
    img_url = models.TextField(verbose_name='事件图片链接', null=True, blank=True)

    class Meta:
        verbose_name = '事件图片资源'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.event_id.event_name + '图片链接添加成功'


class SourceVideo(models.Model):
    event_id = models.ForeignKey(Detail, on_delete=models.CASCADE)
    video_url = models.TextField(verbose_name='事件视频/音频链接', null=True, blank=True)

    class Meta:
        verbose_name = '事件视频资源'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.event_id.event_name + '视频/音频链接添加成功'

