from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name="home"),
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('user',views.user,name="user"),
    path('user/Myprofile',views.profile,name="profile"),
    path('user/profile/edit',views.edit,name="edit"),
    path('user/profile/photoedit',views.photoedit,name="photoedit"),
    path('',views.logout,name="logout"),
    path('dellProfile/', views.dellProfile, name='dellProfile'),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)