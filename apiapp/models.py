from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tags"


class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    due_date = models.DateTimeField(blank=True, null=True, verbose_name="Дедлайн")
    is_done = models.BooleanField(default=False, verbose_name="Выполнено")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "tasks"


class TaskTag(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="task_tags")
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="task_tags")

    def __str__(self):
        return f"{self.task.title} — {self.tag.name}"

    class Meta:
        db_table = "task_tags"
        unique_together = ("task", "tag") 