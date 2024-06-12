from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.contrib.auth import views
from django.conf.urls.static import static


urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # login/logout
    path('login/', views.LoginView.as_view(), name='login'),
    path('accounts/login/', views.LoginView.as_view()), # precisa ter essa url pra redirecionar as paginas de erro do django
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    # include app urls
    path('', include('pf.urls')),
    path('', include('links.urls')),
    path('zanine/', include('zanine.urls')),
]

# static urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
