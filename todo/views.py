from .models import Todo
from datetime import datetime
from .forms import TodoCreateForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic import (
	View,
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
	)
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.

class TodoItemDoneView(View):

	def get(self,request,pk):

		object_ = get_object_or_404(Todo,pk=pk)

		object_.done = True

		object_.save()

		return redirect("todo:index_view")

class TodoDeleteView(DeleteView):

	model = Todo

	success_url = reverse_lazy("todo:index_view")

class TodoListView(ListView):

	model = Todo

	def get_context_data(self,*args, **kwargs):

		ctx = super().get_context_data(*args, **kwargs)

		ctx["today"] = datetime.now().date()

		return ctx

class TodoDetailView(DetailView):

	model = Todo

class TodoCreateView(SuccessMessageMixin, CreateView):

	model = Todo

	form_class = TodoCreateForm

	success_message = "Todo Item have been created successfully"

	def get_success_url(self):

		return reverse_lazy("todo:detail_view",kwargs={"pk":self.object.pk})

class TodoUpdateView(SuccessMessageMixin, UpdateView):

	model = Todo

	form_class = TodoCreateForm

	success_message = "Todo Item have been updated successfully"

	def get_success_url(self):

			return reverse_lazy("todo:detail_view",kwargs={"pk":self.object.pk})
	

class TodoAPIView(View):

	http_method_names = ['get',]

	def get(self, request, *args, **kwargs):

		objects = Todo.objects.all().values("pk","title","description")

		return JsonResponse({"todo":list(objects)})