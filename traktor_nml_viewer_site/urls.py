from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('traktor_nml_viewer/', include('traktor_nml_viewer.urls')),
    path('admin/', admin.site.urls),
]
