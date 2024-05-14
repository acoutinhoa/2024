from django.urls import path, include
from . import views

app_name = 'links' # >>> referenciar como {% url 'links:name' %}


home_patterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.index, name='index-link'),
    path('<str:tag>/', views.index, name='index-tag'),
]

ps_patterns = [
    path('', views.ps_info, name='ps-info'),
    path('delete/', views.ps_delete, name='ps-delete'),
    path('edit/', views.ps_edit, name='ps-edit'),
]

user_patterns = [
    path('', views.index, name='perfil'),
    path('<int:pk>/', views.index, name='perfil-link'),
    path('<str:tag>/', views.index, name='perfil-tag'),
    path('link/<int:pk>/', include(ps_patterns)), # prints
]

urlpatterns = [
    path('links/', include(home_patterns)),
    path('<str:nome>/links/', include(user_patterns)), # user
    path('links/link/<int:pk>/', include(ps_patterns)), # prints
]
