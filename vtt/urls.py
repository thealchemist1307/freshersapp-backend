from django.conf.urls import url 
from vtt import views 
 
urlpatterns = [ 
    url(r'^api/vtt$', views.vtt_response),
]