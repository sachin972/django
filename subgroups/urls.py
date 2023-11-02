from django.urls import path
from . import views
urlpatterns = [
    path('getSubGroupsData', views.GetSubGroups),
    path('removeSubGroup/<str:id>', views.RemoveSubGroup),
    path('updateSubGroup/<str:id>', views.UpdateSubGroup),
    path('addNewSubGroup/', views.AddNewSubGroup),
]