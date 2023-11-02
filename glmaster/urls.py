from django.urls import path
from . import views

urlpatterns = [
    path('getGlMaster', views.GlMasterView),
    path('addGlMaster/', views.AddGLMasterView),
    path('removeGlMaster/<str:id>', views.RemoveGlMasterView),
    path('updateGlMaster/<str:id>', views.UpdateGlMasterView)
]