from django.contrib import admin
from django.urls import path, include

from core import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('secret/', views.secret_page, name='secret'),
    path('secret2/', views.SecretPage.as_view(), name='secret2'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]

"""
django.contrib.auth.urls, inclui (login, logout, password_change, password_done, password_reset,
password_reset_done, password_reset_confirm and password_reset_complete)
"""