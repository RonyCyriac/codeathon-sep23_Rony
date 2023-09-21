def max_profit(prices):
    if len(prices) < 2:
        return -1
    
    min_price = prices[0]
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    
    if max_profit == 0:
        return -1
    else:
        return max_profit

 def test_max_profit():
    assert max_profit([7,1,5,3,6,4]) == 5
    assert max_profit([7,6,4,3,1]) == -1
    assert max_profit([1,2,3,4,5]) == 4
    assert max_profit([2,4,1]) == 2
    assert max_profit([2,1,2,1,0,1,2]) == 2

test_max_profit()       
