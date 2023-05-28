import openai
import gradio

openai.api_key = "api_key_here"

messages = [{"role": "system", "content": "You are an intelligent AI and you can answer on any topic"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo-0301",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Anubhav Madhav GPT")

demo.launch(share=True)