from django.urls import path, include
from . import views

app_name = 'zanine' # >>> referenciar como {% url 'links:name' %}


# home_patterns = [
#     path('', views.index, name='index'),
#     path('pessoas/', views.index, {'pessoas':True}, name='index-pessoas'),
#     path('<int:pk>/', views.index, name='index-link'),
#     path('<str:tag>/', views.index, name='index-tag'),
# ]

urlpatterns = [
    # path('links/', include(home_patterns)),
    path('', views.tl, {'tipo':''}, name='index'),
    path('<str:tipo>/', views.tl, name='tl'),
]
