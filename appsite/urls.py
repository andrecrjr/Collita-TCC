from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apisite.urls')),
    path('', include('website.urls')),
    path('marketplace/', include(('transacaosite.urls','transacaosite'), namespace='transacaosite'))
]