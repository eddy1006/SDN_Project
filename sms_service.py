# SMS service
import requests
import base64
import os
from dotenv import load_dotenv

if(pred[0][1] > 0):  # >1 - attack     0 - benign
  load_dotenv()
  appId = os.getenv('APPID')
  accessKey = os.getenv('ACCESSKEY')
  accessSecret = os.getenv('ACCESSSECRET')
  projectId = os.getenv('PROJECTID')
  channel = "SMS"
  identity = "+918792884722"
  url = "https://us.conversation.api.sinch.com/v1/projects/" + projectId + "/messages:send"

  data = accessKey + ":" + accessSecret
  encodedBytes = base64.b64encode(data.encode("utf-8"))
  accessToken = str(encodedBytes, "utf-8")

  payload = {
    "app_id": appId,
    "recipient": {
        "identified_by": {
            "channel_identities": [
              {
                  "channel": channel,
                  "identity": identity
              }  
              ]
        }
    },
    "message": {
        "text_message": {
            "text": "Ddos Attack Detected. Kindly take necessary action."
        }
    }  
  }

  headers = {
    "Content-Type": "application/json",
    "Authorization": "Basic " + accessToken
  }

  response = requests.post(url, json=payload, headers=headers)

  data = response.json()
  print(data)