from django.urls import path
from MainApp import views
urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('item/<int:id>', views.get_item, name='item-page'),
    path('items', views.items_list, name='items-list'),

]
