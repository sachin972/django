from django.urls import path
from . import views

urlpatterns = [
    path('addGroup/', views.AddNewGroup),
    path('getGroup/', views.GetGroupDetails),
    path('removeGroup/<str:id>', views.RemoveGroup),
    path('updateGroupDetails/<str:id>', views.UpdateGroup),
]