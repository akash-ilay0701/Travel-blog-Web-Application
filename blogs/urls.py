from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [

    path('', views.home, name='home'),
    # path('createdBlog/', views.createdBlog, name='createdBlog'),
    path('confirmed/', views.confirmed, name='confirmed'),
    path('seeMore/<int:pk>', views.seeMore, name='seeMore'),
    path('addBlog/', views.AddBlog.as_view(), name='addBlog')



]

urlpatterns += staticfiles_urlpatterns()
