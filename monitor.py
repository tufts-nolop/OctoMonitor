import datetime
import json
import requests

printers: dict = {}
credentials: list[str]
with open('credentials') as file:
    credentials = file.readlines()

for credential in credentials:
    if credential == "": continue
    [base_url, api_key] = credential.split()
    url = f'https://{base_url.strip()}/api/job'
    printers[url] = api_key.strip()

for url, api_key in printers.items():
    print(f'Printer: {url}')
    try:
        req = requests.get(url, headers={"X-Api-Key": api_key})
    except requests.exceptions.ConnectionError:
        print('Unable to connect')
        print()
        continue
    except Exception as ex:
        print(f'Unexpected Error: {ex}')
        print()
        continue
    
    response = json.loads(req.text)

    if "state" not in response:
        print(f'Unexpected Response: {response}')
        print()
        continue

    print(response["state"])
    progress = response["progress"]
    print(f'Progress: {progress["completion"]:.2f}%')
    print(f'Time left: {datetime.timedelta(seconds=progress["printTimeLeft"])}')
    print()