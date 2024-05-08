from django.urls import path, include
from . import views

app_name = 'links' # >>> referenciar como {% url 'links:name' %}

user_patterns = [
    path('', views.perfil, name='user'),
    path('<str:tag>/', views.perfil, name='user-tag'),
    path('<int:pk>/', views.perfil, name='user-link'),
]

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.index, name='index-link'),
    path('<str:tag>/', views.index, name='index-tag'),
    # user
    path('<str:nome>/', include(user_patterns)),

]
