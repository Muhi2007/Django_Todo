from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import TaskGroup
from .forms import TaskCreationForm, TaskEditForm

def about(request):
    return render(request, template_name='todos/about.html')

class TaskListView(ListView):
    model = TaskGroup
    template_name = 'todos/home.html'
    context_object_name = 'task_group'
    paginate_by = 6

class UserTaskView(ListView):
    model = TaskGroup
    template_name = 'todos/home.html'
    context_object_name = 'task_group'
    paginate_by = 6

    def get_queryset(self):
        username = self.kwargs.get('username')
        return TaskGroup.objects.filter(author__username=username)

class TaskCreateView(LoginRequiredMixin ,CreateView):
    model = TaskGroup
    template_name = 'todos/task_create.html'
    form_class = TaskCreationForm
    success_url = reverse_lazy('todo-home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TaskEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = TaskGroup
    template_name = 'todos/task_create.html'
    form_class = TaskEditForm
    success_url = reverse_lazy('todo-home')

    def test_func(self):
        task = self.get_object()
        return task.author == self.request.user
    
class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = TaskGroup
    template_name = 'todos/task_confirm_delete.html'
    success_url = reverse_lazy('todo-home')

    def test_func(self):
        task = self.get_object()
        return task.author == self.request.user