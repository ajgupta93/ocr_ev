from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^accounts/profile/$', 'ocr_evaluation.views.profile'),
#    (r'^accounts/login/$', 'ocr_evaluation.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}), 
    (r'^accounts/', include('allauth.urls')),
    url(r'^upload/$', 'ocr_evaluation.views.upload_file'),
    url(r'^mystats/$', 'ocr_evaluation.views.mystats'),
    url(r'^file_list/$', 'ocr_evaluation.views.file_list'),
    url(r'^download/(?P<id>\d+)', 'ocr_evaluation.views.download', name='file_download'),
    url(r'^ocr_performance/$', 'ocr_evaluation.views.ocr_performance'),
    url(r'^leaderboards/$', 'ocr_evaluation.views.leaderboards'),
    url(r'^seg_performance/$', 'ocr_evaluation.views.seg_performance'),
    url(r'^upload_file/$', 'ocr_evaluation.views.upload_file'),
    url(r'^$', include('ocr_evaluation.urls')),
    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
