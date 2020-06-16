from django.conf.urls import url 
from clubs import views 
 
urlpatterns = [ 
    url(r'^api/clubs$', views.club_list),
    url(r'^api/clubs/(?P<pk>[0-9]+)$', views.club_detail),
]