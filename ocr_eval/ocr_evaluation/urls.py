from django.conf.urls import patterns, include, url
from ocr_evaluation.views import *

urlpatterns = patterns('',
    url(r'^upload/$', upload_file),
    url(r'^upload_file/$', upload_file),
    url(r'^file_lost/$', file_list),
    url(r'^download/(?P<id>\d+)', download, name="file_download"),
    url(r'^ocr_performance/$', ocr_performance),
    url(r'^accounts/profile/$', profile),
    url(r'^$', home),
)
