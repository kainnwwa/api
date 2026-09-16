from django.views import View
from django.http import JsonResponse
from json import loads
from .models import Task, Tag, TaskTag
from .forms import TaskForm, TagForm, TaskTagForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, 'dispatch')
class ViewTask(View):
    def get(self, request):
        tasks = Task.objects.all()
        task_list = []
        for task in tasks:
            task_list.append({
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'due_date': task.due_date,
                'is_done': task.is_done,})
        obj = {
            'data': task_list
        }
        return JsonResponse(obj)

def post(self, request):
        raw_json = request.body
        new_data = loads(raw_json)

        form = TaskForm(new_data)
        if form.is_valid():
            form.save()
            return self.get(request)
        else:
            return JsonResponse(
                {'status': 'error', 'code': 400},
                status=400
            )



class ViewTag(View):
    def get(self, request):
        tags = Tag.objects.all()
        tag_list = []
        for tag in tags:
            tag_list.append({
                'id': tag.id,
                'name': tag.name,})
        obj = {
            'data': tag_list
        }
        return JsonResponse(obj)

def post(self, request):
        raw_json = request.body
        new_data = loads(raw_json)

        form = TagForm(new_data)
        if form.is_valid():
            form.save()
            return self.get(request)
        else:
            return JsonResponse(
                {'status': 'error', 'code': 400},
                status=400
            )


class ViewTaskTag(View):
    def get(self, request):
        task_tags = TaskTag.objects.all()
        task_tag_list = []
        for tt in task_tags:
            task_tag_list.append({
                'id': tt.id,
                'task': tt.task.title,
                'tag': tt.tag.name,
            })
        obj = {
            'data': task_tag_list
        }
        return JsonResponse(obj)

def post(self, request):
        raw_json = request.body
        new_data = loads(raw_json)

        form = TaskTagForm(new_data)
        if form.is_valid():
            form.save()
            return self.get(request)
        else:
            return JsonResponse(
                {'status': 'error', 'code': 400},
                status=400
            )