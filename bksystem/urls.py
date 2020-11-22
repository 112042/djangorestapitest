from django.conf.urls import url #針對api新增函示
from bksystem import views_book
from django.urls import path


urlpatterns=[
    #sign system interface:
    
    # api:
    # ex : /api/add_event/
    path('add_event/', views_book.add_event, name='add_event'),
    # ex : /api/add_guest/
    #path('add_guest/', views_if.add_guest, name='add_guest'),
    # ex : /api/get_event_list/
    path('get_event_list/', views_book.get_event_list, name='get_event_list'),
    # ex : /api/get_guest_list/
    #path('get_guest_list/', views_if.get_guest_list, name='get_guest_list'),
    # ex : /api/user_sign/
    #path('user_sign/', views_if.user_sign, name='user_sign'),

]