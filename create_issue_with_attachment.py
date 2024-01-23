import json
import requests
import mimetypes

DOMAIN = "https://frocode.helpshift.com"
API_KEY = "frocode_api_20240120223035136-7718d1a4b2a99f8"
ATTACHMENT_FILE_PATH = "./nkz.jpg"
TEST_PAYLOAD = {
    "email": "test@mail.com",
    "message-body": "Custom Issue Fields Demo.",
    "title": "Issue with random custom issue fields",
    "tags": json.dumps(["foo"]),
    "meta": json.dumps({"test": 1}),
    "author-name": "FroCode",
    "platform-type": "web",
    "app-id": "random_app_20140423095931205-caae76e3be13ef6",
}

def construct_attachment_object(attachment_url):
    file_name = attachment_url.split("/")[-1]
    file_type, encoding = mimetypes.guess_type(attachment_url)
    return {"attachment": (file_name, open(attachment_url, "rb"), file_type)}

def make_api_call(api_endpoint, api_key, payload, attachment={}):
    response = requests.post(api_endpoint, auth=(api_key, ""), data=payload, files=attachment)
    print("API response status {0}".format(response.status_code))
    print("API response {0}".format(response.json()))

if __name__ == "__main__":
    api_endpoint = 'https://api.helpshift.com/v1/issues'  # Remove {0}/{DOMAIN} from the endpoint
    attachment_object = construct_attachment_object(ATTACHMENT_FILE_PATH)
    make_api_call(api_endpoint, API_KEY, TEST_PAYLOAD, attachment_object)
