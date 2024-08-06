import gradio as gr
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# pass the api key
client = OpenAI(
    api_key = os.getenv('OPEN_AI_API_KEY')
)

messages = []
messages.append({
    'role': 'system',
    'content':  '''You are an interviewer at a tech company.
            You want to know if the user has good technical knowledge in game programming at a senior level.
            Present the user with questions.
            Give 4 different answers to each question (a, b, c, d).
            Reply to the user whether their answer is correct or not, and continue with a new question.'''
})

def respond(history, new_message):
    
    # add the user input to the messages
    messages.append({
        'role': 'user',
        'content': new_message
    })

    # api call
    response = client.chat.completions.create(
        messages=messages, 
        model="gpt-4o-mini"
    )

    # obtain response text
    assistant_message = response.choices[0].message
    messages.append(assistant_message)

    return history + [[new_message, assistant_message.content]]

with gr.Blocks() as interview_bot:
    chatbot = gr.Chatbot()
    user_input = gr.Text()

    user_input.submit(respond, [chatbot, user_input], chatbot)


interview_bot.launch()