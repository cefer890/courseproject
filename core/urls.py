from django.urls import path
from core import views

urlpatterns = [
     path('',views.home),
     path('xiomi/',views.xiomi),
     path('xiomi/<int:xiomi_id>',views.xiomi_det, name='xiomi_det'),
     path('news/<int:news_id>',views.news_det, name='news_det'),
     path('reg/', views.reg_user, name='users_reg'),
     path('sides/', views.SidesList.as_view(), name='sides_list'),
     path('sides/<int:pk>', views.SidesDetail.as_view(), name='sides_det'),
     path('sides_upload/', views.sides_user, name='sides_upload'),
     path('sides_delete/<int:sides_id>', views.sides_delete, name='sides_delete'),
     path('sides_edit/<int:sides_id>', views.sides_update, name='sides_update'),
]