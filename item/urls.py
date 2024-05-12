from django.urls import path

from . import views
app_name= 'item'
urlpatterns = [
    path('<int:pk>', views.detail, name='detail'),
    path('new/',views.new_item,name='new'),
    path('<int:pk>/delete', views.delete, name='delete'),
]
