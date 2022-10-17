Requirements:

Python 3.0+ for the python script.

or

[jq](https://stedolan.github.io/jq/) for the bash script.

The credentials file should have the following format.
```
[BASE_URL_1] [API_KEY_1]
[BASE_URL_2] [API_KEY_2]
```

```
git clone git@github.com:tufts-nolop/OctoMonitor.git
sudo apt install python3-flask
cd OctoMonitor
(need to install credentials.txt file)
flask run
```
