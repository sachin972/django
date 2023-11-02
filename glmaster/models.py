from django.db import models

from subgroups.models import SubGroupModel

# Create your models here.
class GlMasterModel(models.Model):
    _id = models.UUIDField(primary_key=True)
    gl_code = models.CharField()
    gl_name = models.CharField()
    gl_type = models.CharField()
    sub_group = models.ForeignKey(SubGroupModel, on_delete=models.CASCADE)
    gl_balance = models.BigIntegerField()
    gl_balance_type = models.CharField()

    def __str__(self):
        return f"{self.gl_name} {self.gl_code} \n{self.sub_group}"
    
    def to_json(self):
        return {
            "gl_id": str(self._id),
            'gl_name': self.gl_name,
            "sub_group": self.sub_group.to_json(),
            "gl_code": self.gl_code,
            "gl_balance": self.gl_balance,
            "gl_balance_type": self.gl_balance_type,
            "gl_type": self.gl_type,
            # "group_balance": self.group_balance
        }
