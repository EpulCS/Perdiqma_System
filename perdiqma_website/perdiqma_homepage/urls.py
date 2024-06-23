from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login_selection/", views.login_selection, name="login_selection"),
    path("pin_admin", views.pin_pass, name="pin_pass"),
    path("register_admin", views.register_admin, name="register_admin"),
    path("adminlogin", views.adminlogin, name="adminlogin"),
    path("admin_dashboard", views.admin_dashboard, name="admin_dashboard"),
    path('gallery/', views.gallery, name='gallery'),
    path('activitylistuser', views.activitylistuser, name='activitylistuser'),
    path('activity_detailuser/<int:pk>/', views.activitylistdetailuser, name='activity_detailuser'),
    path('activitylist', views.activitylist, name='activitylistadmin'),
    path('activity_create', views.activitycreate, name='activity_create'),
    path('activities/<int:pk>/', views.activity_detail, name='activity_detail'),
    path('activities/<int:pk>/edit/', views.activity_update, name='activity_update'),
    path('activities/<int:pk>/delete/', views.activity_delete, name='activity_delete'),
    path('register_perd', views.register_perd, name='register_perd'),
    path('members/<str:perdiqmaID>/update/', views.update_member, name='update_member'),
    path('members/<str:perdiqmaID>/delete/', views.delete_member, name='delete_member'),
    path('perdiqma_list', views.perdiqma_list, name='perdiqma_list'),
    path("loginpage", views.loginpageperdiqma, name="loginpage"),
    path("perdiqma_dashboard", views.perdiqma_dashboard, name="perdiqma_dashboard"),
    path('assign/<int:pk>/', views.assign_activity, name='assign_activity'),
    path('track_activity', views.track_activity, name='track_activity'),
] 