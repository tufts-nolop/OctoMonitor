from flask import Flask, render_template
import datetime
import json
import requests

app = Flask(__name__)

printers = {}
credentials = []
responses = {}
with open('credentials.txt') as file:
    credentials = file.readlines()

for credential in credentials:
    if credential == '': continue
    [hostname, api_key] = credential.split()
    url = f'https://{hostname.strip()}.nolop.org/api/job'
    printers[hostname] = (url, api_key.strip())
print(printers)

@app.route('/')
def check_status():
    print(printers)
    for (url, api_key) in printers.values():
        print(url)
        try:
            req = requests.get(url, headers={"X-Api-Key": api_key}, timeout=10)
        except requests.exceptions.ConnectionError:
            print('Unable to connect to ' + url)
            print()
            continue
        except Exception as ex:
            print(f'Unexpected Error: {ex}')
            print()
            continue

        response = json.loads(req.text)
        print(response)

        if "state" not in response:
            print(f'Unexpected Response: {response}')
            print()
            continue
        responses['p' + ''.join(filter( lambda x: x in '0123456789', url ))] = response
    return render_template('index.html', printers = printers, responses = responses)
