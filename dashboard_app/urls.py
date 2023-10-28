from django.urls import path
from dashboard_app import views

urlpatterns = [
    path('createApp', views.createApp),
    path('addSub', views.addSubscription),
    path('updateSub', views.updateSubscription),
    path('cancelSub', views.cancelSubscription),
    path('listSub', views.listSubscription),
]
