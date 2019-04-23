from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home, name='Home'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='login_site'),
    path('cadastro/', signup, name='signup_site'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout_site'),
    path('perfil/<int:id_user>/', perfil, name='inventario_user'),
    path('marketplace/', home_marketplace, name='marketplace_site'),
    path('marketplace/boleto/', boleto_marketplace, name='boleto_final'),
    path('marketplace/cart/', cart_marketplace, name='marketplace_cart')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)