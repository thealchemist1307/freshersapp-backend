from django.conf.urls import url 
from library import views 
 
urlpatterns = [ 
    url(r'^api/library$', views.library_timings),
    
]