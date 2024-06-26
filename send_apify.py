from apify_client import ApifyClient
import os

# Initialize the ApifyClient with your API token
# Eventually hide API key
client = ApifyClient(os.environ.get('APIFY_KEY'))

with open('urls.txt', 'r') as f:
    urls = f.read().splitlines()
    start_urls = [{"url": url} for url in urls]

# Prepare the Actor input
run_input = {
    "startUrls": start_urls,
    "instructions": """Create 2 quiz based questions on the article, with 4 multiple choice answers. Provide the correct answer too""",
    "schema": {
        "type": "object",
        "properties": {
            "Question": {
                "type": "string",
                "description": "Question to be asked",
            },
            "Answers": {
                "type": "string",
                "description": "4 multiple choice answers",
            },
            "Correct_Answer": {
                "type": "string",
                "description": "The correct answer from the 4 multiple choice answers",
            },
        },
}}

# Run the Actor and wait for it to finish
run = client.actor("paOtbjvyUiNsr1Qms").call(run_input=run_input)

with open('urls.txt', 'a') as f:
    # Assuming client.dataset().iterate_items() returns iterable items you want to write to a file
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        # Convert the item to a string and write it to the file, followed by a newline
        f.write(str(item) + '\n')

#I want to only show URL, question, answer, correct answer cleanly
#I want to set all these to their own unique variable