

from django.contrib import admin
from django.urls import path,include

heanler404='practice.views.custom_page_not_found'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('user.urls'))
]
