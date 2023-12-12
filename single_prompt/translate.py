from openai._client import OpenAI
import settings
from django.conf import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def generate_message(system_input, user_input):
    message = [{
        'role':'system',
        'content':system_input},
        {'role':'user',
         'content':user_input
    }]
    return message

def generate_response2(user_input, model='gpt-3.5-turbo', temperature = 0.2):
    system_input = "You are a language expert who can translate any language into English.\
        Whatever the user input you will get, you just need to translate into basic English sentense without using complex words."

    messages = generate_message(system_input, user_input)

    response = client.chat.completions.create(model=model,
                                 messages = messages,
                                 temperature = temperature)
    
    return response.choices[0].message.content