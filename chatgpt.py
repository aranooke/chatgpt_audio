import openai
import os

# set up OpenAI API key
openai.api_key = "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"

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
    return message;

#res = ask_gpt("Make this text lower:Мадара Учіха - вигаданий персонаж у манзі Наруто та аніме-серіалі, створеному Масасі Кісімото. Він був легендарним ніндзя, який заснував клан Учіха і село Конохагакуре разом зі своїм молодшим братом Ізуною Учіха. Амбиції Мадари полягали в тому, щоб стати Хокаге Конохагакуре, титул, якого він не зміг досягти. Він також є головним антагоністом серії.")
