class Restauraunt():
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
    
    def describe_restaurant(self):
        print "The name of the restaurant is " , self.name,  "and they serve", self.cuisine,  "food"
        return self

    def open_restaurant(self):
        print self.name , "is open for business"
        return self

restauraunt1 = Restauraunt("Danny's", "Chinese")
restauraunt2 = Restauraunt("Mickey d's", "American" )
restauraunt3 = Restauraunt("Checkers", "fast food")

print restauraunt1.name
print restauraunt1.cuisine

restauraunt1.describe_restaurant()
restauraunt1.open_restaurant()
restauraunt2.describe_restaurant()
restauraunt3.describe_restaurant()

class  User():
    def __init__(self, first_name, last_name, email, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password

    def describe_user(self):
        print self.first_name
        print self.last_name 
        print self.email
        print self.username 
        print self.password

    