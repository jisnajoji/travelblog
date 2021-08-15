from django.urls import path

from . import views

urlpatterns= [
    path('', views.fun, name='fun'),
    path('login',views.login, name="login"),
    path('regist', views.register, name="regist"),
    path('logout',views.logout,name="logout"),
    path('add_place',views.add,name="add_place"),
    path('update/<int:id>',views.updat,name='update'),
    path('delete/<int:id>/', views.delete, name='delete')

    # path('about', views.about,name="about"),
    # path('home', views.home,name="home")

    # path('add', views.add, name='add'),
    # path('addition', views.addition, name='addition')
    # path('logout',views.logout,name="logout")
]