from django.db import models

# Create your models here.
class UsersModel(models.Model):
    _id = models.UUIDField(primary_key=True)
    email = models.EmailField()
    name = models.CharField()
    # first_name = 

    def __str__(self):
        return f"{self.name} {self.email}"