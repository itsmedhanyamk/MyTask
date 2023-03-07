from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login,name='login'),
    path('register/',views.register,name='registers'),
    path('logout/',views.logout,name='logout'),
    path('user_details/',views.user_details,name='udetails'),
    path('get_branches_ajax/',views.get_branches_ajax,name='get_branches_ajax'),
]