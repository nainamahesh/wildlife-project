from django.conf.urls import url
from . import views

app_name='animal_details'
urlpatterns = [

    url(r'^$', views.IndexView.as_view(),name='index'),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
    url(r'animal/add/$',views.AnimalCreate.as_view(),name='animal-add'),

    url(r'animal/(?P<pk>[0-9]+)/$', views.AnimalUpdate.as_view(), name='animal-update'),

    url(r'animal/(?P<pk>[0-9]+)/delete/$', views.AnimalDelete.as_view(), name='animal-delete'),

    url(r'medicines/$',views.MedicineDetail.as_view(),name='med-detail'),
    url(r'medicines/add/$',views.MedicineCreate.as_view(),name='medicine-add'),
    url(r'medicines/(?P<pk>[0-9]+)/$',views.MedicineUpdate.as_view(),name='medicine-update'),
    ]