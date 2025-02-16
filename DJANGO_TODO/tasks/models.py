from django.db import models

class Task(models.Model):
    text = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
