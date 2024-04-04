from django.contrib import admin
from django.urls import path

from Backend import views
urlpatterns = [
    path('display/',views.display,name="display.html"),
    path('edit_page/<int:dataid>', views.edit_page, name="edit_page"),
    path('update_data/<int:dataid>',views.update_data,name="update_data"),
    path('delete_video/<int:dataid>',views.delete_video,name="delete_video")
]