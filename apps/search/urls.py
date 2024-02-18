from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="root"),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('officers/<int:officer_id>/', views.viewOfficer),
    path('postreview/', views.postreview),
    path('searchresult', views.searchresult),
    # path('populate', views.populate),
    path('rated', views.rated, name="rated"),
    path('donate', views.donations_page, name="donate"),
    path('charge/', views.charge, name="charge"),
    path('success/<str:args>/', views.successMsg, name="success"),
]