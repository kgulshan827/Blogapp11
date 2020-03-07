from django.urls import path
from .import views
from django.conf.urls.static import static
urlpatterns = [
   path('',views.signup,name="signup"),
   path('login/',views.login_view,name="login"),
   path('logout/',views.logout_view,name="logout"),
]

