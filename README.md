# TelmexComplainer
A simple Python program that monitors your internet speed and tweets a complaint to your ISP when it gets slow. 

## Installation
Once you've downloaded/cloned the project to your machine, install the dependencies with:


```
pip3 install -r requirements.txt
```

You will also need a [Twitter developer account](https://developer.twitter.com/en). Once you have it, just put
the API keys they give you in the `config.json` file.


## Usage
```
python3 telmexcomplainer.py
```
Or you can also run it in the background with

```
python3 telmexcomplainer.py &
```
In order to run this as a service you will have to manually setup the daemon, however. 

You can configure this program through the `config.json` file:
* {atISP}: This is the username (@) of the ISP account that will be mentioned in your tweets
* {internetSpeedThreshold}: The internet speed (download speed in this case) that you are paying for 
* {twitterAuth}: This is just where your API keys will go
* {tweetSelection}: This is where you will get your tweets from, depending on how bad your internet speed is (my messages are in Spanish, so change them if you need to)
  * bad: Slightly angry tweets
  * horrible: Really angry tweets

## Notes
Now, you might be thinking, "Wait, how does this account for the bandwidth used up by the speedtest itself?". The answer is it doesn't. As much
as I hate my ISP, it's a little unfair to spam them with tweets everytime my internet speed is 1 Mbps slower than what it's supposed to.
Because of this, this program decides if your speed is 'bad' or 'horrible' depending on what percentage of the advertised speed you actually have.
So if you are paying for 30 Mbps, for instance, then this program will only tweet if your current speed dips below 60% (bad) or 50% (horrible) of those
30 Mbps. 




You can change that by the way. Go to lines 43 and 45 of the `telmexcomplainer.py` file.


And that's pretty much it. This program doesn't do anything beyond tweeting. I will probably add more stuff later on but this will do for now. You could
also just pay a kid on the street a few bucks to manually harass your ISP.
