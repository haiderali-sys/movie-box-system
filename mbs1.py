# function to show currect movies
def view_movies():
    print("THESE ARE MOVIES AVAILABLE IN OUR CINEMA")
    for mv in show_movies:
        print(f"Movie:{mv.name}\n Movie_Id:{mv.movie_id}\n Timing :{mv.timing}\n Aavailable seats :{mv.available_seats}")

# functionn to book tickets

def  book_ticket():
    for mv in show_movies:
        print(f"Movie:{mv.name}\n Movie_Id:{mv.movie_id}\n Timing :{mv.timing}\n Aavailable seats :{mv.available_seats}")

    while True:  
        user_inp_id=int(input("Enter movie Id:"))
        print ("Enter 5 to quit")

        if user_inp_id==5:
            return end()
        found=False
        for mv in show_movies:
            
            if  user_inp_id == mv.movie_id:
                found=True
                print(f"Name:{mv.name }\nTiming:{mv.timing}\nAvaiable seats:{mv.available_seats}")
                if mv.available_seats>0:
                    mv.available_seats=mv.available_seats-1
                    return end()
                else:
                    print("Sorry no seats Availabale for this movie")
                    break    
        if not found:
             print("You have entered wrong Movie Id")
       

def cancel_ticket():
    pass
def view_bookings():
    pass
def end():
    print("thank you for using our project")
    exit()
# movie classs for display movies

class movie:
    def __init__(self,movie_id,name,timing,available_seats):
        self.movie_id=movie_id
        self.name=name
        self.timing=timing
        self.available_seats=available_seats
show_movies=[
        movie(101, 'Inception', '6 PM', 0),
        movie(102, 'Interstellar', '9 PM', 50),
        movie(103, 'The Dark Knight', '12 PM', 50)]
    
# main menu for displaying menu

while True :
    print ("==== Welcome to CineMax ====")
    print("1. View Movies")
    print("2. Book Ticket")
    print("3. Cancel Ticket")
    print("4. View Bookings")
    print("5. Exit")
    try:
        user=int(input("Enter the number which option u want to visit:"))
        if user == 1:
            view_movies() 
        elif user == 2:
            book_ticket()
        elif user == 3:
            cancel_ticket()
        elif user == 4:
            view_bookings()
        elif user ==5:
            end()
       
    except ValueError:
        print("Invalid input")
