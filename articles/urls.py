
from django.urls import path
from .import views
from django.conf.urls.static import static

urlpatterns = [

    path('',views.article_list,name="list"),

    path('<slug:slug>/',views.article_detail,name="detail"),
    path('create',views.create,name="create"),

]
