from django.db import models

# Create your models here.
class Todo(models.Model):
    # The Todo model
    title = models.CharField(max_length=120, blank=True)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title
