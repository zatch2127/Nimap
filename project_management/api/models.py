from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Client(models.Model):
    client_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)  # ✅ Allow NULL
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.pk:  # ✅ Update only if the object already exists
            original = Client.objects.get(pk=self.pk)
            if original.client_name != self.client_name:  # ✅ Only update `updated_at` if `client_name` changes
                self.updated_at = now()
        else:
            self.updated_at = None  # ✅ Ensure `updated_at` is NULL on creation
        super().save(*args, **kwargs)

    def __str__(self):
        return self.client_name

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    users = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_projects')

    def __str__(self):
        return self.project_name
