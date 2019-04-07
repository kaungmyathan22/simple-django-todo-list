from django.urls import path
from . import views

app_name="todo"

urlpatterns = [

	path('',views.TodoListView.as_view(), name="index_view"),
	path('detail/<int:pk>/',views.TodoDetailView.as_view(), name="detail_view"),
	path('done/<int:pk>/',views.update_item_done, name="done_view"),
	path('update/<int:pk>/',views.todo_update_view_page, name="update_view"),
	path('delete/<int:pk>/',views.todo_delete_view_page, name="delete_view"),
	path('create/',views.todo_create_view_page, name="create_view"),

]