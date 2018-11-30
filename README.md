# Price-Watcher
Use the data science pipeline to see how accurately  amateure investors can predict stock prices.
### Project Description
Using sentiment analysis for the posts that the tickers for specific stocks occur in and market data, analyze the rise and fall of stock prices in tandem with growing stock popularity and positive sentiment.  Focus on stocks that are fast growing, bubble prone, and popular in day trading communities.
## Data Pipeline
### Gathering Data
To choose the stocks to use for this project, I picked stocks that were very volatile, so I could get some days of high increases and decreases in price.  I also decided to pick stocks that were favored by the day trading community, so there would be more data to get from on StockTwits.  I found eight stocks to fit this criteria: $TLRY, $AMD, $MU, $BABA, $IQ, $JD, $TCEHY and $APRN

To collect the amature data, I decided to use the website [Stocktwits](https://stocktwits.com/), because it provides opinions from investors about the stocks, who are the ones who directly cause changes in stock prices.  Stocktwits also has a free API that can be used to get posts about certain stocks, which users can make and tag with how they feel about the stock.  Users can tag a stock 'Bearish' if they feel it will go down of 'Bullish' if they feel it will go up.

One issue that I ran into with Stocktwits is their API does not allow for collecting historical data.  This meant that whenever the API call was made, I would only receive the last 10 posts made tagging that ticker.  To get around this, I ran the script I wrote every day on the [Google Cloud Console](https://cloud.google.com/cloud-console/).

To gather the information about historical stock prices, I used the website [eoddata](http://eoddata.com/).  Because I was using only a few different stocks, I just went to the page of each stocks and downloaded the historical data for the time frame that I needed.  I chose to do this over using an API because I was only grabbing the data for eight different stocks, and this seemed like the simpler solution. 

### Cleaning and Summarizing the Data
To clean and summarize the data, I added all of the StockTwits data to a VM with PySpark on it.  Here, I loaded all the csv's into a dataframe.  I looped through all of the days in the dataframe and found the sum of all bearish and bullish sentiments for each stock, for each day.  This drastically reduced the amount of raw data.  The results were loaded into a json file so it would be easy to import them into Python for analysis.

### Analyzing Data
I needed to get a metric of the ratio of bear and bull posts that was not affected by the size of the data set, as some days more data was gathered than others.  I decided to take the average of the bearish sentiment using the formula: (-bearish posts)/(bullish + bearish).  This data was graphed with the percent change of a stock every day.  

This can be interpreted easily: if the sentiment of a stock is higher (relative to the other heights) than investors are more positive about the stock, and it should go up.  There seems to be no discernible correlation between large changes in stock prices and sentiment the day before.

The AMD stock is fairly indicative of this.  In all of these charts, any large changes in stock price are mirrored by corresponding increases and decreases in sentiment, showing most of the data on StockTwits is reactive instead of predictive.  This can be seen in the AMD chart on the 14th, 19th and 20th.  There is an increase in sentiment on the 14th, when the stock rises higher, a decrease when the stock falls, then an increased the next day.     

![alt text](/finalGraphs/AMD.png?raw=true)

The APRN stock shows more of the same trends.  Except for two points (the 8th and 21st), the sentiment more or less follows the current stock price.

![alt text](/finalGraphs/APRN.png?raw=true)

I picked the BABA chart to show a time when a “prediction” was correct.  It seems like the sentiment on the 7th "predicted" better performance on the 8th.  However, this trend is not continued for the rest of the time the stock was recorded and is likely a coincidence.   

![alt text](/finalGraphs/BABA.png?raw=true)

## Future Additions

**Different Time:**  I would like to try collecting all of this data at a different time in the market.  November has been one of the poorest performing months in the past few years and this made finding accurate predictions difficult because most of the stocks I was watching lost value every day.

**More Knowledge of Statistics:** I did not originally think that the sentiment would be so reactive to the stocks daily performance because the Bearish and Bullish tags are supposed to be a prediction of how the stock will do in the future, not about how the stock is currently doing.  I would like to learn a little more about Statistics so I could better interpret these graphs and perhaps make a function that could remove this variable.

**Different Sources for Data:** I would like to try getting data from different sources.  I originally decided to go with StockTwits because the sentiment was given.  I was first looking at using investing communities on Reddit, but because of the profanity, almost every post is assigned a negative sentiment when using most available LSTM's on the internet.  In the future, a stock trading specific LSTM could be trained using the data from Stocktwits.  I would also like to try this with data from non-investors.  A paper that showed success with using Twitter to predict stock prices is in the GitHub repository.




