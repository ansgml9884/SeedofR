# from django.urls import path
#
# from . import views
#
# urlpatterns = [
#     # main
#     path('', views.index, name='index'),
#     path('seedofr/new', views.post_new, name='post_new'),
#     path('seedofr/compare', views.post_compare, name='post_compare'),
#     path('seedofr/<int:seq>/', views.post_detail, name='post_detail'),
#     path('seedofr/list', views.post_list, name='post_list'),
# ]


from django.urls import path
from . import views

urlpatterns = [
  path('seedofr/new/', views.post_new, name='post_new'),
  path('', views.post_list, name='post_list'),
  path('seedofr/<int:pk>/edit/', views.post_edit, name='post_edit'),
  path('seedofr/<int:seq>/', views.post_detail, name='post_detail'),
]