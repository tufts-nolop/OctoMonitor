Requirements:

Python 3.0+ for the python script.\
The credentials file should be plain text with the following format.
```
[BASE_URL_1] [API_KEY_1]
[BASE_URL_2] [API_KEY_2]
```

or

[jq](https://stedolan.github.io/jq/) for the bash script.\
The credentials file should be a json object with the following format.
```json
{
  "user":"",
  "pass":"",
  "urls":[""]
}
```

Todo:
- [ ] Switch bash script to using API-Keys
- [ ] Switch bash script to using same credential file format
