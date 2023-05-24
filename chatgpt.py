import openai
import os

# set up OpenAI API key
openai.api_key = "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";

# get response from GPT-3
def ask_gpt(prompt, model='text-davinci-003', temperature=0.8, max_tokens=250, stop=None):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        n=1,
        stop=stop
    )
    message = response.choices[0].text.strip()
    print(message);
    return message;
# res = ask_gpt('tell me about math');
