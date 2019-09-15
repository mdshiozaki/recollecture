import requests

endpoint = "https://recollecture.cognitiveservices.azure.com"
url = endpoint + "/text/analytics/v2.1/keyPhrases"

transcript_text = "Those trying to have good careers are going to fail, because, really, good jobs are now disappearing. There are great jobs and great careers, and then there are the high-workload, high-stress, bloodsucking, soul-destroying kinds of jobs, and practically nothing in-between. So people looking for good jobs are going to fail. I want to talk about those looking for great jobs, great careers, and why you're going to fail. First reason is that no matter how many times people tell you, 'If you want a great career, you have to pursue your passion, you have to pursue your dreams, you have to pursue the greatest fascination in your life,' you hear it again and again, and then you decide not to do it. It doesn't matter how many times you download Steven J.'s Stanford commencement address, you still look at it and decide not to do it. "

documents = {"documents": [
    {"id": "1", "text": transcript_text}
]}

headers = {"Ocp-Apim-Subscription-Key": ""}
response = requests.post(url, headers=headers, json=documents)
key_phrases = response.json()
print(key_phrases)
