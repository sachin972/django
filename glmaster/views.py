import json
import uuid
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from glmaster.models import GlMasterModel
from subgroups.models import SubGroupModel

# Create your views here.
def GlMasterView(request):
    print(request)
    data = [json.dumps(model.to_json()) for model in GlMasterModel.objects.all()]
    return JsonResponse(data, safe=False)

def AddGLMasterView(request):
    print(request)
    print(request.body)
    if(request.method == "POST"):
        data = json.loads(request.body)
        print(data)
        GlMasterModel.objects.create(
            _id=data["id"],
            gl_code=data["code"],
            gl_name=data["name"],
            gl_type=data["type"],
            gl_balance=data["balance"],
            # gl_type=data[""],
            gl_balance_type=data["balanceType"],
            sub_group=SubGroupModel.objects.get(pk=data["subGroup"])
        )
        print(GlMasterModel.objects.all())
        return HttpResponse({"message" : "Successfully added"})
    else:
        return HttpResponse({"message": "Invalid request"})
    
def RemoveGlMasterView(request, id):
    print(request)
    if(request.method == "DELETE"):
        GlMasterModel.objects.get(pk=uuid.UUID(id)).delete()
        return HttpResponse({"message": "Deleted"})
    else:
        return HttpResponse({"Some Error Occured"})
    

def UpdateGlMasterView(request, id):
    data = json.loads(request.body)
    curr = GlMasterModel.objects.get(pk=id)
    print(curr)
    # GroupModel.objects.update()

    curr.gl_code=data["code"],
    curr.gl_name=data["name"],
    curr.gl_type=data["type"],
    curr.gl_balance=data["balance"],
    # curr.# gl_type=data[""],
    curr.gl_balance_type=data["balanceType"],
    curr.sub_group=SubGroupModel.objects.get(pk=data["subGroup"])
    curr.save()
    
    return HttpResponse({'message': "Successfully updated"})