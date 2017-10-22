# Worth-It
Visualize the price of a product in terms of products you already know using the Amazon Echo

![Logo](https://github.com/sunny8751/Worth-It/blob/master/logo%20copy.png?raw=true)
[Example Demonstration](https://youtu.be/0AM2WQz2kiU)

## What inspired us
When I say that I pay ~$50,000/year for college, what does that actually mean? To some, that's just a really big number, but to me, that number is equivalent to 7,692 Chipotle bowls.
We realized that in a world that is rapidly moving away from physical currency and even physically shopping, the worth of goods and products is becoming harder to quantify.  
We understand the food, technology, and entertainment that we purchase in terms of dollar signs, but what do they actually mean to us?  We developed _Worth It_ to define value in terms of something familiar to us all: other goods and products.

## What it does
_Worth It_ allows the user to compare the worth of one product in terms of another more familiar product. With the Alexa and just a simple voice command, we can describe how much a Nintendo Switch costs in terms of Chipotle bowls, or how much a new laptop costs in ramen noodle packages.  _Worth It_ can respond instantaneously via Alexa voice response, show what is being said via a slick web interface, and even create cards on the Amazon Alexa app for both Android and iOS. 

## How we built it
We developed _Worth It_ by using the Flask-Ask framework to integrate Alexa skills in Python and create the cards. Each product is identified by comparing it to the entire Amazon product database using the Amazon Product Advertising API. Also, we created a backend MongoDB server which contains unique items not found on Amazon, such as a Vanderbilt tuition or Chipotle bowl. The web interface was made using Flask, Socket.io, HTML, AJAX, JQuery, and Python.

## Challenges we ran into
* One of the bigger challenges that we ran into was the problem of updating the web interface UI asynchronously in relation to the response that was returned by the Alexa.  Because we realized that Flask was not built for asynchronous calls, we had to switch to Socket.io at the last minute, which was super stressful.
* Another challenge we ran into was that the Amazon API only allows a maximum of one query per second. This was an obstacle that we did not think could be solved as it was a limitation from Amazon itself. However we managed to fix this problem in true hackathon fashion by creating a second AWS account that could also access the Amazon API. Thus, between our API lookups we alternated between the two.

## What we learned
We learned how to create an Alexa Skill, use Flask to create a web interface, and store information on a MongoDB database. All of these technologies were fairly new to us, so it was great being exposed to new skills.

## Related Links

* [Devpost](https://devpost.com/software/worth-it) - The hackathon Devpost
* [Presentation](https://docs.google.com/presentation/d/1JSu8Pt7rGgZYWuYxLTpD-pBapFxYYHOrN8s1bCJ_XYo/edit?usp=sharing) - Presentation


