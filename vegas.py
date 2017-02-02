import cs50
import sys

dates = ["THURSDAY 2/2", "FRIDAY 2/3", "SATURDAY 2/4"]

print ("Please enter the number of males and females to search all Las Vegas guest lists:")
females = int(input("Number of females: "))
males = int(input("Number of males: "))

def ratio(males, females):
    if females >= 1 and males == 0: #condition for girl only groups
        return 1 
    elif females >= males and males != 0: #condition for even ratio groups, or groups with more females then males
        return 2 
    elif females < males and females >= 0: #condition for groups with more males than females
        return 3 
        
guestlist_rule = ratio(males, females)
print (guestlist_rule)

#Returns guest list rule #1: Free for girls only
#Returns guest list rule #2: Free for even female/male ratio groups
#Returns guest list rule #3: Free for everyone

thursday_venues ={
    'Omnia' : 1,
    'Hakkasan' : 2,
    'Intrigue' : 1
}

friday_venues ={
    'Omnia' : 1,
    'Hakkasan' : 2,
    'Jewel' : 1,
    'XS' : 1,
    'Surrender' : 2,
    'Intrigue' : 1,
    'Light' : 1,
    'Marquee' : 2,
}

saturday_venues ={
    'Omnia' : 1,
    'Hakkasan' : 1,
    'Jewel' : 2,
    'XS' : 1,
    'Surrender' : 1,
    'Intrigue' : 3,
    'Light' : 1,
    'Marquee' : 1,
}

def thursday():
    key = 0
    if guestlist_rule == 1:
        for key in thursday_venues:
            if thursday_venues.get(key) == 1 or thursday_venues.get(key) == 2 or thursday_venues.get(key) == 3:
                print (key)
    elif guestlist_rule == 2:
        for key in thursday_venues:
            if thursday_venues.get(key) == 2 or thursday_venues.get(key) == 3:
                print (key)
    elif guestlist_rule == 3:
        for key in thursday_venues:
            if thursday_venues.get(key) == 3:
                print (key)
    print ("\n")


def friday():
    key = 0
    if guestlist_rule == 1:
        for key in friday_venues:
            if friday_venues.get(key) == 1 or friday_venues.get(key) == 2 or friday_venues.get(key) == 3:
                print (key)
    elif guestlist_rule == 2:
        for key in friday_venues:
            if friday_venues.get(key) == 2 or friday_venues.get(key) == 3:
                print (key)
    elif guestlist_rule == 3:
        for key in friday_venues:
            if friday_venues.get(key) == 3:
                print (key)
    print ("\n")
    
def saturday():
    key = 0
    if guestlist_rule == 1:
        for key in saturday_venues:
            print (key)
    elif guestlist_rule == 2:
        for key in saturday_venues:
            if saturday_venues.get(key) == 2:
                print (key)
    elif guestlist_rule == 3:
        for key in saturday_venues:
            if saturday_venues.get(key) == 3:
                print (key)
    print ("\n")

print ("For %s females and %s males, the following Vegas guest lists are free for this group:\n" % (females, males))
print (dates[0])
thursday()
print (dates[1])
friday()
print (dates[2])
saturday()