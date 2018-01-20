def display_message():
    print "I am learning alot about functions!!!"

display_message()

def Favorite_book():
    print "One of my favorite books is Omerta by Mario Puzo ".title() + "!"

Favorite_book()

def make_shirt(shirt_size = "small", text_message = "our shirts Rule".title()):
    print "The font size on my shirt is " + shirt_size, "and the message is: " + text_message

make_shirt()
make_shirt("XXL", "Tech's Run the World".title())
make_shirt("Large", "I love Python".title())

