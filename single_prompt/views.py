from django.shortcuts import render, HttpResponse
from .forms import InputForm
import os
from dotenv import load_dotenv
from openai._client import OpenAI
from django.conf import settings
#from translate import generate_response2


load_dotenv()  # This loads the .env file

#API_KEY = os.getenv('API_KEY')


# Create your views here.
def home(request):
    return render (request,'home.html')


def about(request):
    return render(request, 'about.html')

def single(request):
    return HttpResponse("this is single line response.")

def bulkfile(request):
    return HttpResponse("this is where you can upload the bulk file.")

def input_view(request):
    user_input = ''
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            form = InputForm() 
    else:
        form = InputForm()

    return render(request, 'input.html', {'form': form, 'user_input': user_input})



# function below this is to generate response using openAI api


client = OpenAI(api_key=settings.OPENAI_API_KEY)

def generate_message(system_input, user_input):
    message = [{
        'role':'system',
        'content':system_input},
        {'role':'user',
         'content':user_input
    }]
    return message

def generate_response(system_input, user_input, model='gpt-3.5-turbo', temperature = 0.2):
    
    messages = generate_message(system_input, user_input)

    response = client.chat.completions.create(model=model,
                                 messages = messages,
                                 temperature = temperature)
    
    return response.choices[0].message.content

def translate_view(request):
    
    response_text = None

    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            print("user_input",user_input)
            system_input = "You are a language expert who can translate any language into English.\
                Whatever the user input you will get, you just need to translate into basic English sentense without using complex words."


            response_text = generate_response(system_input, user_input)
            
    else:
        form = InputForm()

    return render(request, 'translator.html', {'form': form, 'response': response_text})


def chat_view(request):    
    response_text = None

    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            print("user_input",user_input)
            system_input = "You are a generalist who is expert in all the fields.Respond to user input to the best of your ability. You should sound friendly.\
                with every question user ask, chellange them to ask more tougher question and reply in short and crisp answer.\
                    If you do not know the answer, than say sorry in a funny way like you do not mean it and it's okay to not know some of the things.\
                        At the end, ask user if they need more assistance."


            response_text = generate_response(system_input, user_input)
            
    else:
        form = InputForm()

    return render(request, 'chat.html', {'form': form, 'response': response_text})
