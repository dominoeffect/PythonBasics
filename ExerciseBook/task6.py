headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

# TODO: set news_ticker to a string that contains no more than 140 characters long.
# HINT: modify the headlines list to verify your loop works with different inputs
def news(headlines):
    news_ticker = ""
    for index in range(len(headlines)):
        news_ticker += headlines[index] + " "
        while len(news_ticker) >= 140:
            news_ticker = news_ticker[:140]
            break
    return news_ticker

news_ticker = news(headlines)
print (news_ticker)





for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break