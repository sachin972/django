import json
import uuid
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from groups.models import GroupModel

# Create your views here.
def GetGroupDetails(request):
    # data = GroupModel.objects.all()
    data = [json.dumps(model.to_json()) for model in GroupModel.objects.all()]
    # return render(request,'group_data/file.html')
    return JsonResponse(data, safe=False)

def AddNewGroup(request):
    print(request.body)
    data = json.loads(request.body)
    print(data)
    newData = GroupModel.objects.create(
        group_id=data["id"],
        group_code=data["code"],
        group_name=data["name"],
        group_type=data["type"],
        group_balance=data["balance"]
    )
    # newData.save()
    print(GroupModel.objects.all())
    return HttpResponse({"message":"Group added successfully"})



def RemoveGroup(request, id):
    print(id)
    if(request.method == "DELETE"):
        data = GroupModel.objects.get(pk=uuid.UUID(id))
        print(data)
        # if(len(data) == 0):
        # return HttpResponse({'error': "Group with id not found"}).status_code(404)
        
        # else:
        data.delete()
        print(GroupModel.objects.all())
        return HttpResponse({'message' : "Successfully removed the group"})
    else:
        return HttpResponse({'message': "Bad request"})

    # return HttpResponse("hello")

def UpdateGroup(request, id):
    print(id)

    if(request.method == "POST"):
        data = json.loads(request.body)
        curr = GroupModel.objects.get(pk=id)
        print(curr)
        # GroupModel.objects.update()

        curr.group_code=data["code"]
        curr.group_name=data["name"]
        curr.group_type=data["type"]
        curr.group_balance=data["balance"]
        curr.save()
        
        return HttpResponse({'message': "Successfully updated"})
    
    else:
        return HttpResponse({'message': "Bad request"})