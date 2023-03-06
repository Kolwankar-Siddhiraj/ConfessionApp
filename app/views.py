from django.http import HttpResponse
from django.contrib.auth.models import User, auth

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializer import *

# Create your views here.


class HandleConfession(APIView):

    def get(self, request):

        confessions_objects = Confession.objects.filter(is_deleted=False, state="approved").values("id", "confession_title", "confession_note", "sender_info", "state", "comment_allowed", "created_at", "updated_at")

        return Response({"success": True, "error": False, "data": confessions_objects})
    
    
    def post(self, request):

        rdata = request.data
        print("rdata :: ", rdata)

        cb = Confession.objects.filter(confession_title=rdata['title'], confession_note=rdata['note'], secret_key=rdata['secret_key'], sender_info=rdata['sender_info']).first()
        
        print("cb :: ", cb)

        if cb == None:
            new_confession = Confession.objects.create(confession_title=rdata['title'], confession_note=rdata['note'], secret_key=rdata['secret_key'], sender_info=rdata['sender_info'])
            data = ConfessionSerializer(new_confession).data
        else:
            data = None
        return Response({"success": True, "error": False, "data": data})
    
    
    def delete(self, request):

        rdata = request.data

        Confession.objects.filter(id=rdata['id']).update(is_deleted=True)

        return Response({"success": True, "error": False})



class AdminLogin(APIView):

    def post(self, request):

        rdata = request.data

        user = auth.authenticate(username=rdata['username'], password=rdata['password'])
        if user is not None:
            auth.login(request, user)
        
        else:
            pass

        return Response({"success": True, "error": False, "message": "Success!"})



