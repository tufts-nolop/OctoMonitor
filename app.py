from flask import Flask, render_template
import datetime
import json
import requests

app = Flask(__name__)

printers = {}
credentials = []
responses = {}
with open('credentials') as file:
    credentials = file.readlines()

for credential in credentials:
    if credential == "": continue
    [base_url, api_key] = credential.split()
    url = f'https://{base_url.strip()}/api/job'
    printers[url] = api_key.strip()
print(printers)

@app.route('/')
def check_status():
    msg = ''
    print(printers)
    for url, api_key in printers.items():
        print(f'Printer: P' + "".join(filter( lambda x: x in '0123456789', url )))
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

        #print(f'Progress: {progress[url]["completion"]:.2f}%')
        #print(f'Time left: {datetime.timedelta(seconds=progress[url]["printTimeLeft"])}')
    return render_template('index.html', response1=responses['p1'], response2 = responses['p4'])
