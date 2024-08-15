from django.urls import path
from.views import *

urlpatterns=[
    path('Tlist',TodoList.as_view(),name='tlist'),
    path('Tadd',TodoAdd.as_view(),name='tadd'),
    path('Tdel/<int:id>',TodoDelete.as_view(),name='tdel'),
    path('Tupd/<int:id>',TodoUpdate.as_view(),name='tupd'),
    path('statusupd/<int:id>',UpdateStatus,name='statusupd'),
]