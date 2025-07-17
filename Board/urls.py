from django.urls import path
from . import views

app_name='Board'
urlpatterns = [
    path('', views.board_list, name='list'),
    path('board_detail/', views.board_detail, name='detail'),
    path('board_form/', views.board_form, name='detail'),
    path('board_form_update/', views.board_form_update),
    path('board_login/', views.board_login),
    path('board_signup/', views.board_signup),
]
