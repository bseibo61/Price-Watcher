# Price-Watcher
Use the data science pipeline to see how accurately analysts and amateurs can predict stock prices.

### Project Description
Using sentiment analysis for the posts that the tickers for specific stocks occur in and market data, analyze the rise and fall of stock prices in tandem with growing stock popularity and positive sentiment.  Focus on stocks that are fast growing, bubble prone, and popular in day trading communities.
### Gathering Data
To collect the amature data, I decided to use the website [Stocktwits](https://stocktwits.com/), because it provides opinions from investors about the stocks, who are the ones who directly cause changes in stock prices.  Stocktwits also has a free API that can be used to get posts about certain stocks, which users can tag with how they feel about the stock.  Users can tag a stock 'Bearish' if they feel it will go down of 'Bullish' if they feel it will go up.
One issue that I ran into with Stocktwits is their API does not allow for collecting historical data.  This meant that whenever the API call was made, I would only receive the last 10 posts.  To get around this, I ran the script I wrote every day on the [Google Cloud Console](https://cloud.google.com/cloud-console/).
To gather the information about historical stock prices, I used the website [eoddata](http://eoddata.com/).  Because I was using only a few different stocks, I just went to the page of each stocks and downloaded the historical data for the time frame that I needed.




![alt text](/finalGraphs/AMD.png?raw=true)
