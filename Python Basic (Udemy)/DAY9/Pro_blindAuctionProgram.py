import blindAuctionArt

print(blindAuctionArt.logo)
print("Welcome to the secret auction program.")

bidsRecord = []
shouldContinue = "yes"

def findHighestBid(biddingRecord) :
    highestBidAmount = 0
    highestBidderName = ""
    for  bidder in biddingRecord :
        bidderAmount = bidder["amount"]
        if highestBidAmount < bidderAmount :
            highestBidAmount = bidderAmount
            highestBidderName = bidder["name"]

    print(f'The Winner is {highestBidderName} with a bid of {highestBidAmount}.')

while shouldContinue == "yes" :
    bidderName = input("What's your name?:\n").lower()
    bidAmount = int(input("What's your bid? $:\n"))

    newBidder = {}
    newBidder["name"] = bidderName
    newBidder["amount"] = bidAmount 
    bidsRecord.append(newBidder)

    shouldContinue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

findHighestBid(bidsRecord)