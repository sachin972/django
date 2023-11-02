import json
import uuid
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from groups.models import GroupModel

from subgroups.models import SubGroupModel


# Create your views here.
def GetSubGroups(request):
    data = [json.dumps(model.to_json()) for model in SubGroupModel.objects.all()]

    return JsonResponse(data, safe=False)


def AddNewSubGroup(request):
    data = json.loads(request.body)
    print(data)

    newData = SubGroupModel.objects.create(
        sub_group_id=data["id"],
        sub_group_code=data["code"],
        sub_group_name=data["name"],

        # group_type=data["type"],
        # group_balance=data["balance"]
        group=GroupModel.objects.get(pk=data["group"])
    )
    # newData.save()
    print(SubGroupModel.objects.all())
    return HttpResponse({"message":"Group added successfully"})

def RemoveSubGroup(request, id):
    print(request.body)
    data = SubGroupModel.objects.get(pk = uuid.UUID(id))
    data.delete()
    return HttpResponse({'message': "Removed"})

def UpdateSubGroup(request, id):
    print(request.body)
    data = SubGroupModel.objects.get(pk = id)
    recieved = json.loads(request.body)
    
    data.sub_group_code=recieved["code"],
    data.sub_group_name=recieved["name"],

    # group_type=data["type"],
    # group_balance=data["balance"]
    data.group=GroupModel.objects.get(pk=recieved["group"])
    data.save()
    
    return HttpResponse({'message': "Updated"})