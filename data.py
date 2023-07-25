import requests

# 10 questions max

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
# And to keep only the list of questions, we keep results
question_data = data["results"]
