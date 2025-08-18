# 🎬 CineMax Ticket Booking System

# Movies list with Movie ID, Name, Time, and Available Seats
movies = [
    {"id": 1, "name": "Avengers: Endgame", "time": "7:00 PM", "seats": 50},
    {"id": 2, "name": "Inception", "time": "9:00 PM", "seats": 40},
    {"id": 3, "name": "Interstellar", "time": "6:30 PM", "seats": 30}
]

# Store bookings
bookings = []

# Function to view all movies
def view_movies():
    print("\n==== Available Movies ====")
    for movie in movies:
        print(f"ID: {movie['id']} | {movie['name']} | Time: {movie['time']} | Seats Available: {movie['seats']}")
    print("==========================\n")

# Function to book a ticket
def book_ticket():
    view_movies()
    try:
        movie_id = int(input("Enter the Movie ID you want to book: "))
        for movie in movies:
            if movie["id"] == movie_id:
                if movie["seats"] > 0:
                    name = input("Enter your name: ")
                    seats = int(input("Enter number of seats: "))
                    if seats <= movie["seats"]:
                        movie["seats"] -= seats
                        booking = {"name": name, "movie": movie["name"], "time": movie["time"], "seats": seats, "id": movie_id}
                        bookings.append(booking)
                        print(f"✅ Booking successful for {name}! {seats} seat(s) for {movie['name']} at {movie['time']}.")
                    else:
                        print("⚠️ Not enough seats available.")
                else:
                    print("⚠️ Sorry, no seats left for this movie.")
                return
        print("⚠️ Invalid Movie ID.")
    except ValueError:
        print("⚠️ Invalid input. Please enter numbers only.")

# Function to cancel a ticket
def cancel_ticket():
    if not bookings:
        print("⚠️ No bookings found to cancel.")
        return

    name = input("Enter your name for cancellation: ")
    found = False
    for booking in bookings:
        if booking["name"].lower() == name.lower():
            # Restore seats
            for movie in movies:
                if movie["id"] == booking["id"]:
                    movie["seats"] += booking["seats"]
                    break
            bookings.remove(booking)
            print(f"❌ Booking for {name} canceled successfully.")
            found = True
            break
    if not found:
        print("⚠️ No booking found under that name.")

# Function to view all bookings
def view_bookings():
    if not bookings:
        print("📭 No bookings yet.")
        return
    print("\n==== Your Bookings ====")
    for booking in bookings:
        print(f"Name: {booking['name']} | Movie: {booking['movie']} | Time: {booking['time']} | Seats: {booking['seats']}")
    print("========================\n")

# Main Menu
while True:
    print("\n==== Welcome to CineMax ====")
    print("1. View Movies 🎬")
    print("2. Book Ticket 🎟️")
    print("3. Cancel Ticket ❌")
    print("4. View Bookings 📖")
    print("5. Exit 🚪")

    choice = input("Enter the number which option you want to visit: ")

    if choice == "1":
        view_movies()
    elif choice == "2":
        book_ticket()
    elif choice == "3":
        cancel_ticket()
    elif choice == "4":
        view_bookings()
    elif choice == "5":
        print("👋 Thank you for using CineMax. Goodbye!")
        break
    else:
        print("⚠️ Invalid choice, please try again.")
