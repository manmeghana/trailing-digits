def maxTrailing(price_of_each, desired_trail_number, overall_price):
    maxMultiplier =  overall_price // price_of_each 
    maxcount = 0
    iterator1 = 1#k=Temperory variable 
    while iterator1 <= maxMultiplier:
        result = price_of_each * iterator1
        if str(desired_trail_number) in str(result):
            count = trail(desired_trail_number, result)
            if maxcount < count:
                    maxcount = count
        iterator1 += 1
    return maxcount

def trail(desired_trail_number, result):
    count = 0  
    for ch in str(result):
        if ch == str(desired_trail_number):
            count += 1
        else:
            count = 0
    return count if count >= 2 else 0

print(maxTrailing(57, 9, 1000))
print(maxTrailing(57, 4, 40000))
print(maxTrailing(57, 4, 39000))