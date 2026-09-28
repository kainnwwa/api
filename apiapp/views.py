from django.views import View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
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
                'is_done': task.is_done,
            })
        return JsonResponse({'data': task_list})

    def post(self, request):
        new_data = loads(request.body)
        form = TaskForm(new_data)
        if form.is_valid():
            form.save()
            return self.get(request)
        return JsonResponse({'status': 'error'}, status=400)

    def put(self, request, pk):
        original = get_object_or_404(Task, pk=pk)
        new_data = loads(request.body)
        form = TaskForm(new_data, instance=original)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'ok'})
        return JsonResponse({'status': 'error'}, status=400)

    def patch(self, request, pk):
        original = get_object_or_404(Task, pk=pk)
        new_data = loads(request.body)
        form = TaskForm(new_data, instance=original, partial=True)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'ok'})
        return JsonResponse({'status': 'error'}, status=400)

    def delete(self, request, pk):
        obj = get_object_or_404(Task, pk=pk)
        obj.delete()
        return JsonResponse({'status': 'ok'})


@method_decorator(csrf_exempt, 'dispatch')
class ViewTag(View):

    def get(self, request):
        tags = Tag.objects.all()
        tag_list = []
        for tag in tags:
            tag_list.append({
                'id': tag.id,
                'name': tag.name,
            })
        return JsonResponse({'data': tag_list})

    def post(self, request):
        new_data = loads(request.body)
        form = TagForm(new_data)
        if form.is_valid():
            form.save()
            return self.get(request)
        return JsonResponse({'status': 'error'}, status=400)

    def put(self, request, pk):
        original = get_object_or_404(Tag, pk=pk)
        new_data = loads(request.body)
        form = TagForm(new_data, instance=original)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'ok'})
        return JsonResponse({'status': 'error'}, status=400)

    def patch(self, request, pk):
        original = get_object_or_404(Tag, pk=pk)
        new_data = loads(request.body)
        form = TagForm(new_data, instance=original, partial=True)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'ok'})
        return JsonResponse({'status': 'error'}, status=400)

    def delete(self, request, pk):
        obj = get_object_or_404(Tag, pk=pk)
        obj.delete()
        return JsonResponse({'status': 'ok'})


@method_decorator(csrf_exempt, 'dispatch')
class ViewTaskTag(View):

    def get(self, request):
        task_tags = TaskTag.objects.all()
        task_tag_list = []
        for tt in task_tags:
            task_tag_list.append({
                'id': tt.id,
                'task': tt.task_id,
                'tag': tt.tag_id,
            })
        return JsonResponse({'data': task_tag_list})

    def post(self, request):
        new_data = loads(request.body)
        form = TaskTagForm(new_data)
        if form.is_valid():
            form.save()
            return self.get(request)
        return JsonResponse({'status': 'error'}, status=400)

    def put(self, request, pk):
        original = get_object_or_404(TaskTag, pk=pk)
        new_data = loads(request.body)
        form = TaskTagForm(new_data, instance=original)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'ok'})
        return JsonResponse({'status': 'error'}, status=400)

    def patch(self, request, pk):
        original = get_object_or_404(TaskTag, pk=pk)
        new_data = loads(request.body)
        form = TaskTagForm(new_data, instance=original, partial=True)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'ok'})
        return JsonResponse({'status': 'error'}, status=400)

    def delete(self, request, pk):
        obj = get_object_or_404(TaskTag, pk=pk)
        obj.delete()
        return JsonResponse({'status': 'ok'})