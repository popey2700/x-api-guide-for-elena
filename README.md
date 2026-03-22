# Elena!! Looking for help?! You should read this!

Hi Elena! T gave me the following brief:

"_So basically what I need help with for my dissertation is my methodology. I’ve decided to use X APIs to extract tweets and use python. I know that there is a free version of the X API where I can get a limited amount of posts and tweets but all the videos I’ve watched about how to do this are outdated and the website has completely changed so I just don’t know where to go from there. X’s developer platform literally says there is the free version but Idk how to use it. Im also gonna use python, but I haven’t even gotten to that point yet_"

I have written the code for this and extracted some simple tweets which will help you get going however it will probably be quite confusing for what to do so I thought I'd give you some pointers about good ways to learn
## If you don't know what Python is and have never ran a single Python file on your laptop read this!

In all truthfulness I have no idea how much you know, if this is your first ever Python project  I would heavily recommend stepping back for a second and covering something simpler. If that is the case there are a lot of good free code bootcamps out there on youtube but if you want something quick to learn from I learnt Python from this website and still commonly refer to it https://www.w3schools.com/python/default.asp - If you use this you don't need to work through everything but I'd try to get familiar with how to run Python files and the following concepts: (Its easy to be overwhelmed with how much stuff there is but the below in my opinion will cover most of your needs)

- What a Variable is
- Different Python data types (you'll see that there are more than I have listed below but honestly these will cover you for 90% of coding)
	- Strings
	- Integers
	- Lists
	- Dictionaries
	- Booleans
	- Tuples
- Different Python Operators
	- Arithmetic
		- Addition
		- Subtraction
		- Multiplication
		- Division
	- Comparison
		- Equal
		- Not Equal
		- Greater Than
		- Less Than
		- Greater than or equal
		- Less than or equal
	- Logical
		- and
		- or
		- not
- If and If else statements
- For loops
- Functions

### How do I even "get" Python?

There are quite a few ways to install Python if you google how to do it, I would recommend using Homebrew:

1. Open the terminal
2. run this command: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
3. run this command once the above has finished: `brew install python`
4. Verify this worked by running the command: `python3 --version` . If this returns a message like: `Python <version-number>` then it worked! If it doesn't then google the error and see what people say! (AI is very good for this). If you're really stuck ping T and we can work out how to figure it out.

### Where do I write Python?!

You need an IDE. This is a place for you to edit code and have other useful tools. There are hundreds of IDE's out there I'd recommend using VsCode when you're learning. For getting setup use their documentation https://code.visualstudio.com/docs/languages/python. If you're getting along well with VsCode you could consider trying Cursor which is VsCode but with AI support.

## I have written some Python and I understand the basics now what?

With the basics out of the way you're able to start thinking about your project! There is some learning I would recommend doing before the next steps that is learning about Git, Python Virtual Environment and API's. 

## Git & Github (Optional — but highly recommended!)

**You do not need Git to get your project working**, so if you're in a rush to get to the code feel free to skip this for now and come back later. That said, it's really really really really helpful and if you think you might ever code again it will be one of the most valuable things you can learn, so I'd encourage you to come back to it.

Git is a version control system — it lets you save snapshots of your code as you go. When you inevitably break something beyond repair you can just roll back to a version that worked. It's a safety net, and a very good one.

Github is a popular cloud storage for your git versions. (You're reading this in a Github Repository right now!)

This guide will teach you both: https://docs.github.com/en/get-started/start-your-journey - there are a lot of good youtube videos out there as well!

## Python Venv's

Virtual environments in Python are a place to manage packages. Packages are code other people have written which you can use to do things to save yourself reinventing the wheel. For your project you're likely to need a few but a minimum you will need the requests package. More on that later. This is worth learning. https://www.w3schools.com/python/python_virtualenv.asp

## REST API's

REST API's let different things communicate. In your case you need to communicate with X in order to get information from them. API's are quite a big topic so this is worth getting a rough understanding of before you dive in and start working with them! This is quite a good video https://www.youtube.com/watch?v=lsMQRaeKNDk.

When you call an API it sends back data in a format called **JSON**. You are going to be working with JSON a lot in this project since every tweet X sends back will be in that format. The good news is that JSON looks and behaves almost identically to Python dictionaries — so if you got comfortable with dictionaries during the basics section you're already most of the way there. It's worth giving this a quick read so it doesn't catch you off guard: https://www.w3schools.com/python/python_json.asp


## A note on X API costs

Unfortunately X's API is no longer free to read from — this catches a lot of people out since many tutorials online are outdated and were made before this changed. The good news is it's pay-as-you-go and reasonably affordable for a small project. Reading posts costs $0.005 per post, so $5 of credits gets you 1,000 posts which should be plenty to get started and experiment. Just be mindful that if you're pulling large amounts of data for your dissertation it will add up, so keep an eye on your usage in the developer console.

## Getting started with X's API

1. You need access to use X's API and also to see their documentation on how to interact with it. You'll find this here: https://docs.x.com/x-api/introduction then for getting access here: https://docs.x.com/x-api/getting-started/getting-access. Follow the guide laid out here which involves signing up to X if you haven't before and then visiting the Developer Console https://console.x.com/onboarding. Submit your application and be honest about your anticipated usecase.
2. Continue following the guide in https://docs.x.com/x-api/getting-started/getting-access moving onto step 2. This will be creating a New App and you will eventually get some credentials. You will want to here create a new file in the project root called `.env` You will see I have made an example file called .env.example you can copy. Paste your credentials in appropriatley. These are sensitive, you do not want other people to be able to see them hence you cannot see my .env file in Github! The Bearer Token is the most relevant one for you, you will send it with your API requests when accessing data. 

## Understanding the code — `make_x_health_api_call()`

Open up `main.py` and you'll see the following function. This is a "health check" — it calls X's API to fetch a user's basic info, just to confirm everything is connected and working. Here's what each line does:

```python
def make_x_health_api_call():
    bearer_token = os.getenv("BEARER_TOKEN")
    url = "https://api.x.com/2/users/by/username/xdevelopers"
    headers = {"Authorization": f"Bearer {bearer_token}"}
    response = requests.get(url, headers=headers)

    print(response.json())
```

**`def make_x_health_api_call():`**
This defines a function called `make_x_health_api_call`. Nothing inside it runs until the function is called. You saw how functions work in the basics section — this is one!

**`bearer_token = os.getenv("BEARER_TOKEN")`**
This reads your Bearer Token from your `.env` file and stores it in a variable called `bearer_token`. Remember those sensitive credentials you pasted in earlier? This is where we use them. `os.getenv` is how Python safely reads values from environment files without you having to paste the actual secret into your code.

**`url = "https://api.x.com/2/users/by/username/xdevelopers"`**
This is the URL of the X API endpoint we want to talk to. Think of an endpoint like a specific page on a website — this particular one returns information about a user by their username. Here it's fetching the `xdevelopers` account, just as a test.

**`headers = {"Authorization": f"Bearer {bearer_token}"}`**
Headers are extra information you send alongside an API request. This one is telling X "here is my Bearer Token, I am allowed to be here." The `f"Bearer {bearer_token}"` part is an f-string — it's how Python slots a variable into the middle of a string. So if your token was `abc123`, this would produce the string `"Bearer abc123"`. X checks this token on every request to verify it's you.

**`response = requests.get(url, headers=headers)`**
This is the line that actually makes the request! `requests.get` sends a GET request (i.e. "please give me some data") to the URL, passing the headers along with it. X processes the request and sends back a response, which we store in a variable called `response`.

**`print(response.json())`**
The response from X contains data in JSON format. `.json()` converts that into a Python dictionary so Python can work with it. `print` then outputs it to your terminal so you can see what came back. If everything is set up correctly you should see information about the xdevelopers account printed out!

## A simple X API example — fetching and analysing NASA's tweets

Now that you understand the basics of making an API call, let's look at something a bit more interesting. In `main.py` you'll find a set of functions that fetch NASA's 100 most recent tweets and run some simple analysis on them.

### Navigating the X API docs

Before diving into the code, it's worth understanding how the X API docs are structured because they aren't the most obvious to navigate. You can find them at `docs.x.com` and they are organised by resource type — **Posts**, **Users**, **Lists** etc. The two sections relevant to this example are:

- **Users → Lookup** (`docs.x.com/x-api/users/lookup/introduction`) — for finding information about a user
- **Posts → Timelines** (`docs.x.com/x-api/posts/timelines`) — for fetching a user's tweets

One thing that catches people out: X's tweet endpoints don't accept a username directly, they require a numeric **user ID**. So to get someone's tweets you always have to do it in two steps — first look up the user by username to get their ID, then use that ID to fetch their tweets. You'll see this pattern reflected in the code below.

### The code

```python
def get_nasa_tweets():
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
```

**Step 1 — Look up NASA's user ID**
The first request goes to `/2/users/by/username/NASA` which is the Users → Lookup endpoint. It returns a JSON response and we dig into it with `["data"]["id"]` to pull out just the numeric ID. Think of this like opening a dictionary and looking up a key — `"data"` is the outer key, `"id"` is nested inside it.

**Step 2 — Fetch the tweets**
The second request uses that ID in the URL (`/2/users/{nasa_id}/tweets`) to fetch their timeline. Notice `params={"max_results": 100}` — params are optional extra instructions you can send with a request. Here we're telling X we want 100 tweets back. Without this it would just return a default amount.

**Pulling out the tweet text**
`tweets = [tweet["text"] for tweet in nasa_tweets_response.json()["data"]]` — this is a **list comprehension**, a compact way of building a list in Python. It's doing the same thing as writing a for loop that goes through every tweet in the response and picks out just the `"text"` field. The result is a plain list of strings, one per tweet, which is much easier to work with than the full JSON.

**`print_tweet_analysis(tweets)`**
Rather than doing everything in one big function, the analysis is broken out into separate helper functions and this line calls the one that ties it all together. Splitting code into small focused functions like this is good practice — each one does one thing and is easier to understand and fix if something goes wrong.

---

```python
def average_tweet_length(tweets):
    total_characters = 0
    for tweet in tweets:
        total_characters += len(tweet)
    return total_characters / len(tweets)
```

This loops through every tweet, uses `len()` to count its characters, and adds that to a running total. Once the loop is done it divides the total by the number of tweets to get the average. `+=` is shorthand for "add this to what's already there" — `total_characters += len(tweet)` is the same as writing `total_characters = total_characters + len(tweet)`.

---

```python
def space_mention_count(tweets):
    count = 0
    for tweet in tweets:
        words = tweet.lower().split()
        for word in words:
            if word == "space":
                count += 1
    return count
```

This uses a **nested loop** — a loop inside a loop. The outer loop goes through each tweet, the inner loop goes through each word in that tweet. `.lower()` converts the tweet to lowercase first so that "Space" and "SPACE" and "space" all count the same. `.split()` breaks the string into a list of individual words by splitting on spaces.

---

```python
def print_tweet_analysis(tweets):
    print(f"Average tweet length: {average_tweet_length(tweets):.1f} characters")
    print(f"Times 'space' was mentioned: {space_mention_count(tweets)}")
```

This calls the two helper functions above and prints the results. The `:.1f` inside the f-string is a formatting instruction that rounds the number to 1 decimal place — without it you'd get a long float like `187.3481927...`.

## What next?

You've now got a working setup that can fetch tweets and run basic analysis on them — nice work! But for your dissertation you're probably less interested in one specific user's tweets and more interested in tweets about a **topic or keyword**. For that you'll want the **search endpoint**.

Rather than fetching a user's timeline, the search endpoint lets you pass in a query (like `"climate change"` or `"NHS"`) and get back tweets matching that term. The relevant docs are under **Posts → Search** at `docs.x.com/x-api/posts/search/introduction`.

The structure of the code would be very similar to what you've already seen — same headers, same `requests.get`, same JSON response — but with a different URL and query parameters. Give it a read and see how far you get, you might surprise yourself!
