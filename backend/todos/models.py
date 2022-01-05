from django.db import models


class Todo(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=50, null=False, blank=False)
    completed = models.BooleanField(null=False, default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'todo'
