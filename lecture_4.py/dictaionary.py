dict = {
    "name" : "zohaib",
    "subject" : "python",
    "topics" : ("dict" , "set"),
    19.45 : [10 , 12],
    39 : "oil",
    "is_adult" : True
}
dict["name"] = "hafsa"
print(type(dict))
print(dict)
info = {
    "name" : "zohaib",
    "subjects": {
        "sub" : "python",
        "phy": {
           "lecture1" : True,
           "lecture2" : True,
           "lecture3" : True,
           "lecture4" : "see",
           "lecture5" : False,
           "lecture6" : False,
           "lecture7" : False,
        }
    }
}
print(info.keys())
print(info)

