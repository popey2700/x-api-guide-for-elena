import os
import requests
from dotenv import load_dotenv

load_dotenv()


def make_x_health_api_call():
    try:
        bearer_token = os.getenv("BEARER_TOKEN")
        url = "https://api.x.com/2/users/by/username/xdevelopers"
        headers = {"Authorization": f"Bearer {bearer_token}"}
        response = requests.get(url, headers=headers)
        print(response.json())
    except Exception as e:
        print(f"Something went wrong: {e}")


def get_nasa_tweets():
    try:
        bearer_token = os.getenv("BEARER_TOKEN")
        headers = {"Authorization": f"Bearer {bearer_token}"}

        nasa_lookup_response = requests.get(
            "https://api.x.com/2/users/by/username/NASA",
            headers=headers
        )
        nasa_id = nasa_lookup_response.json()["data"]["id"]

        nasa_tweets_response = requests.get(
            f"https://api.x.com/2/users/{nasa_id}/tweets",
            headers=headers,
            params={"max_results": 100}
        )

        tweets = [tweet["text"] for tweet in nasa_tweets_response.json()["data"]]

        print_tweet_analysis(tweets)
    except Exception as e:
        print(f"Something went wrong: {e}")


def average_tweet_length(tweets):
    total_characters = 0
    for tweet in tweets:
        total_characters += len(tweet)
    return total_characters / len(tweets)


def space_mention_count(tweets):
    count = 0
    for tweet in tweets:
        words = tweet.lower().split()
        for word in words:
            if word == "space":
                count += 1
    return count


def print_tweet_analysis(tweets):
    print(f"Average tweet length: {average_tweet_length(tweets):.1f} characters")
    print(f"Times 'space' was mentioned: {space_mention_count(tweets)}")


if __name__ == "__main__":
    # make_x_health_api_call() 
    get_nasa_tweets()
