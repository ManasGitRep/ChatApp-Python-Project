import os

from groq import Groq

def get_response(prompt):


    client = Groq(
        api_key="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",
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-70b-8192",
    )

    return(chat_completion.choices[0].message.content)