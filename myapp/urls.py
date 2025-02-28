from django.urls import path
from myapp import views
urlpatterns = [
    path('',views.user_list),
    path('Add/',views.AddUser)
]