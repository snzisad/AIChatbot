from django.http.response import JsonResponse, HttpResponse
from .models import ConversationHistory
from rest_framework import viewsets
from .serializers import ConversationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import redirect, render
import uuid
import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

class ConversationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ConversationHistory.objects.all().order_by('-datetime')
    serializer_class = ConversationSerializer


def home(request):
    return render(request, "index.html", {"expenses" : "Hello"})


    # load_dummy_data()
    print(generate_prompt("token", "message"))

    # conversation_list = ConversationHistory.objects.all().order_by("datetime").values()
    # return Response({"data": list(conversation_list)})
    return HttpResponse("Congratulations!! Your server is working perfectly")

@api_view(['POST'])
def getMessage(request):
    if request.method == "POST":
        token = request.POST.get("token", "")
        message = request.POST.get("message", "")
        if len(token) == 0:
            token = uuid.uuid4()

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(token, message),
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
        )
        
        ai_response = response.choices[0].text
        if ai_response.startswith("\n"):
            ai_response = ai_response[1:]
        ConversationHistory(token = token, message = message, response = ai_response).save()

        return Response({"token": token, "response": ai_response}, status=200)
        

def generate_prompt(token, message):
    conversation_list = ConversationHistory.objects.filter(token=token).order_by("datetime")
    prompt = ""
    for conversation in conversation_list:
        prompt += "\nHuman: "+conversation.message+"\nAI: "+conversation.response

    prompt += "\nHuman: "+message+"\nAI: "

    return prompt



def load_dummy_data():
    conversation_list = [
        ConversationHistory(token="sfdfdsfdsfdsf", message = "WHo are you?", response = "I am AI"),
        ConversationHistory(token="sfdfdsfdsfdsf", message = "How do you work?", response = "I use natural language"),
        ConversationHistory(token="sfdfdsfdsfdsf", message = "How are you?", response = "I am fine"),
    ]
    ConversationHistory.objects.bulk_create(conversation_list)