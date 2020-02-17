#Allows to store information in (key,value) pairs
#Create (key,value) pairs and call them from the Dictionary using the "key" in the (key,value)
#Key - word or what uniquely identifies the pair in the dictionary
#Value - is the definion
#All keys have to be unique
#Program to convert 3 digit month name to full name Jan -> January

month_conversations = {
    1: "January",
    2: "February",
    3: "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "July": "July",
    "Aug": "August",
    "Sep": "September",
    10: "October",
    11: "November",
    12: "December",
}

#to print a key from the dictionary
print(month_conversations[2])
print(month_conversations.get("Sep"))

#default value for a key that is not in the dictionary
print(month_conversations.get("luv", "===NOT A VALID KEY==="))