import requests
from bs4 import BeautifulSoup as bs
from listhtml import h0, diffs, prompts

beautify = lambda s: bs(s, 'html.parser').prettify()

# prompt = prompts[0]
# html1, html2 = h0[1]
# html1, html2 = beautify(html1), beautify(html2)

# prompt = f"""
# {prompt}

# "initial-html":
# {html1}

# "post-html":
# {html2}

# What are the changes?
# """

diff = diffs[0]
prompt = prompts[1]
prompt = f"""
{prompt}

diff:
{diff}
"""

# print(prompt)

url = "https://api.perplexity.ai/chat/completions"

payload = {
    "model": "mixtral-8x7b-instruct",
    "messages": [
        {
            "role": "system",
            "content": "Be precise and concise."
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    "temperature": 0
}

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "Bearer API_KEY"
}

try:
    response = requests.post(url, json=payload, headers=headers)
    print(response.text)
    print("-----------------")
    print()
    content = response.json()['choices'][0]['message']['content']
    print(content)
    print("="*10)

    prompt2 = "Summarise these changes. Omit things you are not sure about, and insignificant things. Be breif and high-level. Use logic and reason to correct any mistakes made by you earlier. Write like you are describing the changes to a non-technical person. Dont describe what events took place, simply mention the differences. Use points."

    payload['messages'].extend([
        {'role': 'assistant', 'content': content}, 
        {'role': 'user', 'content': prompt2}])
    
    # print('payload', payload)

    # response = requests.post(url, json=payload, headers=headers)
    # print(response.text)
    # print("-----------------")
    # print()
    # content = response.json()['choices'][0]['message']['content']
    # print(content)

except Exception as e:
    print(f'excpetion occured: {e}')

