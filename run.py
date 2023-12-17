import requests
from bs4 import BeautifulSoup as bs
from listhtml import h0, diffs, prompts
from subprocess import Popen, PIPE

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

# print(prompt)

url = "https://api.perplexity.ai/chat/completions"


headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "Bearer API_KEY"
}

def takeinput(t):
    print(t)
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    return ''.join(contents)

def inputdiff():
    html1 = takeinput('html1')
    html2 = takeinput('html2')
    # html1, html2 = h0[0]
    html1, html2 = beautify(html1), beautify(html2)

    with open('html1.html', 'w') as f:
        f.write(html1)
    with open('html2.html', 'w') as f:
        f.write(html2)

    html1, html2 = h0[1]
    # html1, html2 = beautify(html1), beautify(html2)
    cmd = 'git diff -U999999 --no-index html1.html html2.html' 
    process = Popen(cmd, stdout=PIPE, shell=True)
    diff, error = process.communicate()
    diff = diff.decode()

    with open('diff.html', 'w') as f:
        f.write(diff)

    print(diff)
    return diff

def moddiff(diff):
    lines = diff.split('\n')
    for i, l in enumerate(lines):
        if l and l[0]=='-':
            lines[i] = '(del)' + l[1:]
        elif l and l[0] == '+':
            lines[i] = '(ins)' + l[1:]
    return '\n'.join(lines)
    
def main():
    # diff = inputdiff()
    with open('diff.html', 'r') as f:
        diff = f.readlines()
        diff = ''.join(diff)

    diff = moddiff(diff)
    print(diff)
    # exit(0)
    try:
        prompt = prompts[1]
        prompt = f"""
        {prompt}

        diff:
        {diff}
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
        response = requests.post(url, json=payload, headers=headers)
        print(response.text)
        print("-----------------")
        print()
        content = response.json()['choices'][0]['message']['content']
        print(content)
        print("="*10)

        # prompt2 = "Summarise these changes and ONLY the changes/diff. Omit things you are not sure about, and insignificant things. Be breif and high-level. Use logic and reason to correct any mistakes made by you earlier. Write like you are describing the changes to a non-technical person. Dont describe what events took place, simply mention the differences. Use points."

        # payload['messages'].extend([
        #     {'role': 'assistant', 'content': content}, 
        #     {'role': 'user', 'content': prompt2}])
        
        # print('payload', payload)

        # response = requests.post(url, json=payload, headers=headers)
        # print(response.text)
        # print("-----------------")
        # print()
        # content = response.json()['choices'][0]['message']['content']
        # print(content)

    except Exception as e:
        print(f'excpetion occured: {e}')

main()