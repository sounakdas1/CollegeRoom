
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LogoutView
from usersauthentications import views
from chattings  import views as chat_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.signup,name='signup'),
    path('', views.basenew, name='base'),
    path('my_account/<int:user_id>/', views.account , name='account'),
    path('home/', views.home, name='home'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('chats/', include('chattings.urls')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)