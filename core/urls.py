from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name="index"),
    path('contact/',views.contactPage,name="contact"),
    path('detail/<int:pk>/',views.detail,name="detail"),
    path('signup/',views.signupUser,name="signup"),
    path('login/',views.loginUser,name="login"),
    path('new/',views.newitem,name="new"),
    path('dashboard/',views.dashboardthings,name="dashboard"),
    path('delete/<int:pk>/',views.deleteItem,name="delete"),
    path('edit/<int:pk>/',views.editItem,name="edit"),
    path('browse/',views.browse,name="browse"),
    path('new/<int:item_pk>/',views.new_message,name="new"),
    path('inbox/',views.inbox,name="inbox"),
    path('conversation/<int:pk>/',views.detail_con,name="conversation"),
]

