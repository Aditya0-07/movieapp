from django.contrib import admin
from django.urls import path
from movies import views

app_name="movies"

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home,name="home"),
    path('',views.HomeView.as_view(), name = "home"),
    # path('details/<int:n>/',views.details,name="details"),
    path('details/<int:pk>/',views.Detail.as_view(),name="details"),
    # path('update/<int:n>/',views.update,name="update"),
    path('update/<int:pk>',views.Update.as_view(), name = "update"),
    # path('delete/<int:n>',views.delete,name="delete"),
    path('delete/<int:pk>',views.Delete.as_view(), name = "delete"),
    # path('add/',views.add,name="add_movies"),
    path('add/',views.AddMovie.as_view(),name="add_movies"),
]

