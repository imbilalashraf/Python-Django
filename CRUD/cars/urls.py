from django.urls import path
from cars import views

urlpatterns = [
    path('', views.car_data, name='car_data'),
    path('show/', views.show_car_data, name='show_car_data'),
    path('delete/<int:id>/', views.delete_data, name='delete_data'),  # Unique path for delete
    path('update/<int:id>/', views.update_data, name='update_data'),  # Unique path for update
]
