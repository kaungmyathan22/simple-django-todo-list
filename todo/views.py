from .models import Todo
from datetime import datetime
from .forms import TodoCreateForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
	)
# Create your views here.

def update_item_done(request,pk):

	object_ = get_object_or_404(Todo,pk=pk)

	object_.done = True

	object_.save()

	return redirect("todo:index_view")

def index_page_view(request):

	context = {

		"object_list" : Todo.objects.all(),

		"today": datetime.now(),

	}

	return render(request,"todo/todo_list.html",context)

def todo_detail_view_page(request,pk):

	object_ = get_object_or_404(Todo,pk=pk)

	context = {
		"object" : object_,
	}

	return render(request,"todo/todo_detail.html",context)

def todo_create_view_page(request):

	form = TodoCreateForm(request.POST or None)

	if request.method == "POST":

		if form.is_valid():

			created_todo_item = form.save()

			messages.success(request,f"{created_todo_item} have been added successfully to your todo list .")

			return redirect("todo:index_view")

	context = {

		"form": form,

	}

	return render(request,"todo/todo_form.html",context)

def todo_update_view_page(request,pk):

	instance = get_object_or_404(Todo, pk=pk)

	form = TodoCreateForm(request.POST or None,instance=instance)

	if request.method == "POST":

		if form.is_valid():

			created_todo_item = form.save()

			messages.success(request,f"{created_todo_item} have been updated successfully to your todo list .")

			return redirect("todo:detail_view",pk=created_todo_item.pk)

	context = {

		"form": form,

	}

	return render(request,"todo/todo_form.html",context)

def todo_delete_view_page(request,pk):

	instance = get_object_or_404(Todo, pk=pk)

	instance.delete()

	print("Hello")

	return redirect("todo:index_view")

class TodoListView(ListView):

	model = Todo

	def get_context_data(self,*args, **kwargs):

		ctx = super().get_context_data(*args, **kwargs)

		ctx["today"] = datetime.now().date()

		return ctx

class TodoDetailView(DetailView):

	model = Todo

class TodoUpdateView(UpdateView):

	model = Todo

	success_url = reverse_lazy("todo:detail_view")