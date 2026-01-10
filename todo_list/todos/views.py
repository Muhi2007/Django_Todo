from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import TaskGroup, Todo
from .forms import TaskCreationForm, TaskEditForm, TodoForm, TodoEditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def about(request):
    return render(request, template_name='todos/about.html')

class TaskListView(ListView):
    model = TaskGroup
    template_name = 'todos/home.html'
    context_object_name = 'task_group'
    paginate_by = 4
    ordering = ['-time_create']

class UserTaskView(ListView):
    model = TaskGroup
    template_name = 'todos/home.html'
    context_object_name = 'task_group'
    paginate_by = 4
    ordering = ['-time_create']

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
    context_object_name = 'task_group'
    success_url = reverse_lazy('todo-home')

    def test_func(self):
        task = self.get_object()
        return task.author == self.request.user

@login_required
def task_group_detail(request, pk):
    group = get_object_or_404(TaskGroup, pk=pk)

    if group.author != request.user:
        messages.warning(request, f"You do not have the premission to visit {group.author}'s tasks")
        return redirect('todo-home')
    
    if request.method == 'POST':
        if 'action' in request.POST and request.POST['action'] == 'toggle':
            todo_id = request.POST.get('todo_id')
            todo = get_object_or_404(Todo, id=todo_id, parent=group)
            todo.done = not todo.done
            todo.save()

            next_url = request.POST.get('next') or request.GET.get('next')
            return redirect(next_url or reverse_lazy('todo-home'))
        else:
            form = TodoForm(request.POST)
            if form.is_valid():
                todo = form.save(commit=False)
                todo.parent = group
                todo.save()
                return redirect('task-group-detail', pk=pk)
    else:
        form = TodoForm()

    todos = group.tasks.all()
    context = {
        'form': form,
        'group': group,
        'todos': todos
    }
    return render(request, template_name='todos/task_group_detail.html', context=context)

class TaskGroupListView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = 'todos/task_group_view.html'
    context_object_name = 'todos'

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        group = get_object_or_404(TaskGroup, pk=pk)
        return group.tasks.all().order_by('-time_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['group'] = getattr(self, 'group', get_object_or_404(TaskGroup, pk=self.kwargs.get('pk')))
        return context

    def post(self, request, *args, **kwargs):
        if 'action' in request.POST and request.POST['action'] == 'toggle':
            pk = self.kwargs.get('pk')
            todo_id = request.POST.get('todo_id')
            todo = get_object_or_404(Todo, id=todo_id, parent__pk=pk, parent__author=request.user)
            todo.done = not todo.done
            todo.save()

            next_url = request.POST.get('next') or request.GET.get('next')
            return redirect(next_url or reverse_lazy('todo-home'))

        return super().post(request, *args, **kwargs)

class TodoEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Todo
    form_class = TodoEditForm
    template_name = 'todos/todo_edit.html'

    def get_success_url(self):
        next_url = self.request.POST.get('next') or self.request.GET.get('next')
        return next_url or reverse_lazy('todo-home')

    def test_func(self):
        todo = self.get_object()
        return todo.parent.author == self.request.user