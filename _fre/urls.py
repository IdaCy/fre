from django.contrib import admin
from django.urls import path
from manageuser_app import views as manageuser_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', manageuser_views.login_view, name='login'),
]
