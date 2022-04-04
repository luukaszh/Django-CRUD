from django.contrib import admin
from django.urls import path
from Bees.views import list_bees, create_bee, update_bee, delete_bee

urlpatterns = [
    path('', list_bees),
    path('admin/', admin.site.urls),
    path('create_bee', create_bee, name='create_bee'),
    path('', list_bees, name='list_bees'),
    path('update/<int:id>/', update_bee, name='update_bee'),
    path('delete/<int:id>/', delete_bee, name='delete_bee'),
]
