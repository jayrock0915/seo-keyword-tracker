
from pytrends.request import TrendReq

# Connect to Google Trends
pytrends = TrendReq(hl='en-US', tz=360)

def get_keyword_interest(keywords):
    pytrends.build_payload(keywords, timeframe='now 1-d', geo='US')
    data = pytrends.interest_over_time()
    return data

if __name__ == '__main__':
    keywords = ["AI", "NBA", "Taylor Swift", "Bitcoin", "Job Interview"]
    interest_data = get_keyword_interest(keywords)

    print("📊 Keyword Interest Over Time (Past Day):")
    print(interest_data)
# Save to CSV
interest_data.to_csv("keyword_trends.csv")
print("✅ Data saved to keyword_trends.csv")




