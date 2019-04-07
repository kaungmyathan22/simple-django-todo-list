from django.urls import path
from . import views

app_name="todo"

urlpatterns = [
	path('list/',views.TodoListView.as_view(), name="index_view"),
	path('api/',views.TodoAPIView.as_view(), name="api_view"),
	path('detail/<int:pk>/',views.TodoDetailView.as_view(), name="detail_view"),
	path('done/<int:pk>/',views.TodoItemDoneView.as_view(), name="done_view"),
	path('update/<int:pk>/',views.TodoUpdateView.as_view(), name="update_view"),
	path('delete/<int:pk>/',views.TodoDeleteView.as_view(), name="delete_view"),
	path('create/',views.TodoCreateView.as_view(), name="create_view"),

]