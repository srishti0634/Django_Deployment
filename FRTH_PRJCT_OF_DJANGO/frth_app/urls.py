from frth_app import views
from django.conf.urls import url

app_name = 'frth_app'

urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.user_login, name='user_login'),
]
