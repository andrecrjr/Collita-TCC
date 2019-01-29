from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='Home'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='login_site'),
    path('cadastro/', signup, name='signup_site'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout_site'),
    path('perfil/<int:id_user>/', perfil, name='inventario_user'),
    path('marketplace/', home_marketplace, name='marketplace_site'),
    #path('<int:item_id>/', perfil, name='sell_item')
]