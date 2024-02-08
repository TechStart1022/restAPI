from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from .serializers import PollSerializer, ChoiceSerializer
from .models import Poll,Choice
from rest_framework.response import Response
from rest_framework import generics


def polls_list(request):
    MAX_OBJECTS = 20
    polls = Poll.objects.all()
    data = {"results":list(polls.values("question","created_by__username","pub_date"))}
    return JsonResponse(data)

def polls_detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {"results": {
        "question":poll.question,
        "created_by":poll.create_by.username,
        "pub_date":poll.pub_date,
    }}
    return JsonResponse(data)
# class PollList(APIView):
#     def get(self, request):
#         polls = Poll.objects.all()
#         data = PollSerializer(polls,many=True).data
#         return Response(data)
class PollList(generics.ListAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
class PollDetail(generics.RetrieveDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
# class PollDetail(APIView):
#     def get(self,request,pk):
#         poll = get_object_or_404(Poll,pk=pk)
#         data = PollSerializer(poll).data
#         return Response(data)
class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer



# Create your views here.
