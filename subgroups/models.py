from django.db import models

from groups.models import GroupModel

# Create your models here.
class SubGroupModel(models.Model):
    sub_group_id = models.UUIDField(primary_key=True)
    sub_group_code = models.CharField(max_length=20, blank=False)
    sub_group_name = models.CharField(max_length=50, blank=False)
    # group_code = models.CharField(max_length=20, blank=False)
    group = models.ForeignKey(GroupModel,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.sub_group_code} {self.sub_group_name} having type {self.group}'
    
    def to_json(self):
        return {
            "sub_group_id": str(self.sub_group_id),
            'sub_group_name': self.sub_group_name,
            "group": self.group.to_json(),
            "sub_group_code": self.sub_group_code,
            # "group_balance": self.group_balance
        }