from django.urls import path
from . import views

urlpatterns=[
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('delete-message/<str:pk>/',views.deleteMessage,name="delete-message"),
    path('register/',views.registerUser,name="register"),
    path('',views.home,name="home"),
    path('rooms/<str:pk>/',views.room,name="room"),
    path('create-room/',views.createRoom,name="create-room"),
    path('update-room/<str:pk>/',views.updateRoom,name="update-room"),
    path('delete-room/<str:pk>/',views.deleteRoom,name="delete-room"),
    path('user-profile/<str:pk>/',views.userProfile,name="user-profile"),
    path('update-user/',views.updateUser,name="update-user"),
    path('topics-page/',views.topicsPage,name="topics-page"),
    path('activity-page/',views.activityPage,name="activity-page"),
]