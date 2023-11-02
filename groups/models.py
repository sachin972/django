from django.db import models

# Create your models here.
class GroupModel(models.Model):
    group_id = models.UUIDField(primary_key=True)
    group_code = models.CharField(max_length=20, blank=False)
    group_name = models.CharField(max_length=50, blank=False)
    group_balance = models.CharField(max_length=20, blank=False)
    group_type = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return f'{self.group_code} {self.group_name} having type {self.group_type}'
    
    def to_json(self):
        return {
            "group_id": str(self.group_id),
            'group_name': self.group_name,
            "group_type": self.group_type,
            "group_code": self.group_code,
            "group_balance": self.group_balance
        }