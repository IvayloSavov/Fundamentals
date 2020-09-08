def count_candles_blown_away(array: list):
    height_candle = max(array)
    count_candles = array.count(height_candle)
    return print(count_candles)


number_of_candles = int(input())
height_of_candles = list(map(int, input().split()))
count_candles_blown_away(height_of_candles)