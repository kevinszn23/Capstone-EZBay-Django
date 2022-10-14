import os
import datetime
import sys
from ebaysdk.finding import Connection
from ebaysdk.exception import ConnectionError

from dotenv import load_dotenv
load_dotenv()
API_KEY=os.getenv("api_key")

class ebay_api(object):
    def __init__(self, API_KEY, st):
        self.api_key = API_KEY
        self.st = st

    def fetch(self):
        try:
            api = Connection(appid=self.api_key, config_file=None, siteid="EBAY-US")
            response = api.execute('findItemsAdvanced', {'keywords': st})
            # print(response.reply)
            print(f"Total items: {response.reply.paginationOutput.totalEntries}\n")

            for item in response.reply.searchResult.item:
                print(f"Title: {item.title}, Price: {item.sellingStatus.currentPrice.value}")
                # print(f"Condition: {item.condition.conditionDisplayName}")
                print(f"Buy it now: {item.listingInfo.buyItNowAvailable}")
                print(f"Country: {item.country}")
                print(f"End time: {item.listingInfo.endTime}")
                print(f"URL: {item.viewItemURL}")
                try:
                    print(f"Watchers: {item.listingInfo.watchCount}\n")
                except:
                    pass
                
            return response.reply.searchResult.item

        except ConnectionError as e:
            print(e)
            print(e.response.dict())

    def parse(self):
        pass

if __name__ == "__main__":
    st = sys.argv[1]
    e = ebay_api(API_KEY, st)
    print("testing stuff out", e.fetch())
    e.parse()