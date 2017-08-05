from django.conf.urls import url   
from blog_post import views


urlpatterns = [ 
    url(r'^home/', views.home),    
    url(r'^post-list/', views.post_list, name='post-list'),
    url(r'^single-post/(?P<post_id>[0-9]+)/', views.single_post, name='single-post'),
    url(r'^about/', views.about, name='about'),
    url(r'^contact/', views.contact, name='contact'),
  ]