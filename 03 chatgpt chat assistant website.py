import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "Act like an Indian recipie recommender, your will be provided a set of ingredients seperated by commas, you have to reply with an Indian recipie that can be made using only these ingridients,reply with recipie in bullet points , and state the heading in capital and bold, try to keep it upto 100 words "}]
# messages = [{"role": "system", "content": "Act like a coding expert, you will be provided with a problem statement , your task is to write its code in c++"}]
def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "<b>AI RECIPIE RECOMMENDER<b>", css=""" 
                        body{background-color :rgb(162, 233, 242)}
                        """)
demo.launch(share=True)