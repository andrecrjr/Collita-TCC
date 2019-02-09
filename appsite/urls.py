from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apisite.urls')),
    path('api/', include('transacaosite.urls')),
    path('', include('website.urls')),
]
