import requests
from bs4 import BeautifulSoup as bs
from listhtml import h0, diffs, prompts, prompt2
from subprocess import Popen, PIPE

beautify = lambda s: bs(s, 'html.parser').prettify()


url = "https://api.perplexity.ai/chat/completions"

key = "API_KEY"

def takeinput(t):
    print(t, "- ctrl-d to end input")
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    return ''.join(contents)

def inputhtml():
    html1 = takeinput('html1')
    html2 = takeinput('html2')
    # with open('html1.html', 'w') as f:
    #     f.write(html1)
    # with open('html2.html', 'w') as f:
    #     f.write(html2)
    return html1, html2

def main():
    prompt = prompts[0]
    html1, html2 = inputhtml()
    # with open('html1.html', 'r') as f:
    #     html1 = ''.join(f.readlines())
    # with open('html2.html', 'r') as f:
    #     html2 = ''.join(f.readlines())
    html1, html2 = beautify(html1), beautify(html2)

    prompt = f"""
    {prompt}

    "initial-html":
    {html1}

    "post-html":
    {html2}

    What are the changes?
    """

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
        "temperature": 0,
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": f"Bearer {key}"
    }


    try:
        response = requests.post(url, json=payload, headers=headers)
        print(response.text)
        print("-----------------")
        print()
        content = response.json()['choices'][0]['message']['content']
        print(content)
        print("="*10)


        payload['messages'].extend([
            {'role': 'assistant', 'content': content}, 
            {'role': 'user', 'content': prompt2}])
        
        # print('payload', payload)

        response = requests.post(url, json=payload, headers=headers)
        print(response.text)
        print("-----------------")
        print()
        print('*'*20)
        content = response.json()['choices'][0]['message']['content']
        print(content)

    except Exception as e:
        print(f'excpetion occured: {e}')

if __name__=='__main__':
    main()