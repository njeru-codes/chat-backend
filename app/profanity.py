import json,os
from googleapiclient import discovery
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get('GOOGLE_API_KEY')

def is_toxic(text):
    client = discovery.build(
        "commentanalyzer",
        "v1alpha1",
        developerKey=API_KEY,
        discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
        static_discovery=False,
    )

    analyze_request = {
        'comment': {'text': text},
        'requestedAttributes': {'TOXICITY': {}}
    }

    response = client.comments().analyze(body=analyze_request).execute()
    toxicity = response['attributeScores']['TOXICITY']['summaryScore']['value']
    return toxicity > 0.5

