from django.urls import path
from myapp import views
urlpatterns = [
    path('',views.user_list),
    path('Add/',views.AddUser),
    path('Edit/<id>',views.EditUser),
    path('Delete/<id>',views.DeleteUser),
    path('View/<id>',views.ViewUser),

]
