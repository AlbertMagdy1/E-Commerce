from django.contrib import admin
from django.urls import path
from shop import views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='main'),
    path('<int:id>/', views.details, name="details"),
    path('checkout/', views.checkout, name="checkout"),
    path('signup/', user_views.register, name="signup"),
    path('login/', user_views.CustomLoginView.as_view(template_name='user/login.html'), name="login"),
    path('logout/', user_views.logout_view, name='logout'),
    path('profile/', user_views.profilepage, name='profile'),
]

urlpatterns += [
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
