
from django.conf.urls import url,include
from django.contrib import admin
from blog_post import views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', include('blog_post.urls'), name='home'),

]
