# The student needs to get on a train that leaves from the station D kilometres away in T minutes.
# She can get a taxi that drives at V1 km/h for the price of R €/km or she can walk at V2 km/h for free.
# A correct solution will be a function that returns the minimum price she needs to pay the taxi driver
#  or the string "Won't make it!".
# All the inputs will be positive integers, the output has to be a string containing a number with two
#  decimal places - or "Won't make it!" if that is the case.
# It won't take her any time to get on the taxi or the train.
# In non-trivial cases you need to combine walking and riding the taxi so that she makes it, 
# but pays as little as possible.

# t1 + t2 <= t
# v1*t1 + v2*t2 = d
# To solve for t2
# t1 = (d-v2*t2)/v1
# so t2 = (v1*t-d)/(v1-v2)

def calculate_optimal_fare(d, t, v1, r, v2):
  # TODO: return minimal taxi fare (e.g. "3.14") or "Won't make it!"
    t = t/60.0
    if d/v2 <= t:
        return "0.00" 
    elif d/v1 > t:
        return "Won't make it!"
    else:
        t2 = (v1*t-d)/(v1-v2)
        d2 = v2 * t2
        d1 = d - d2
        fare = r*d1
        return f"{fare:.2f}"