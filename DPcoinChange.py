def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
   for cents in range(change+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minCoins[change]

def printCoins(coinsUsed,change):
   coin = change
   while coin > 0:
      thisCoin = coinsUsed[coin]
      print(thisCoin)
      coin = coin - thisCoin

def main():
    a = [int(x) for x in input().split(" ")]
    amnt = a[0]
    clist = [int(x) for x in input().split(" ")]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)

    #print("Making change for",amnt,"requires")
    #print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"coins")
    print(dpMakeChange(clist,amnt,coinCount,coinsUsed))
    #print("They are:")
    #printCoins(coinsUsed,amnt)
    #print("The used list is as follows:")
    #print(coinsUsed)

main()
