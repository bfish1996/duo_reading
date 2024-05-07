from apify_client import ApifyClient
import url_add

# Initialize the ApifyClient with your API token
# Eventually hide API key
client = ApifyClient("apify_api_CgXY8zpHkOgO0JSu5bDD85wdVQlbNI2HNKht")

# Prepare the Actor input
run_input = {
    "startUrls": [{ "url": "https://news.ycombinator.com/" }],
    "instructions": """Gets the post with the most points from the page and returns it as JSON in this format: 
postTitle
postUrl
pointsCount""",
}

# Run the Actor and wait for it to finish
run = client.actor("paOtbjvyUiNsr1Qms").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)