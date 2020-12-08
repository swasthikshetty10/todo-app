from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from to_do.models import Todo
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")  # it will order by added date
    return render(request, 'to_do/index.html', {
        "todo_items": todo_items,
    })


@csrf_exempt
def add_todo(request):  # post method is used to get data  from index.html
    current_date = timezone.now()
    content = request.POST['content']
    created_obj = Todo.objects.create(added_date=current_date, text=content)  # creating object
    length_of_todos = Todo.objects.all().count()  # returns no of element in database
    return HttpResponseRedirect('/')


@csrf_exempt
def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')

