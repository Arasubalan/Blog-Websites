from django.urls import path
from . import views
app_name='user'
urlpatterns = [
    path('', views.home,name='home'),
    path('detail/<str:slug>',views.detail,name='detail'),
    path('new_small_url',views.new_urls_qwe,name='new_url'),
    path('old_url',views.old_urls_qwe,name='old_urls'),
    path('contact',views.contact_view,name='contact'),
    path('about',views.about,name='about'),
    
    
]
