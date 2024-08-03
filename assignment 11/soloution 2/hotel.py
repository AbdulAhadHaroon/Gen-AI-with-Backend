# hotel.py
from datetime import datetime, timedelta

class Hotel:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.rooms = []
        self.bookings = []
    
    def add_room(self, name, num_of_beds, fare_per_day):
        room = Room(name, num_of_beds, fare_per_day)
        self.rooms.append(room)
    
    def book_room(self, room_name, start_date, end_date):
        room = self._find_room_by_name(room_name)
        if room:
            if self.is_room_available(room_name, start_date, end_date):
                booking = Booking(room, start_date, end_date)
                self.bookings.append(booking)
                print(f"Room '{room_name}' booked from {start_date} to {end_date}.")
            else:
                print(f"Room '{room_name}' is not available from {start_date} to {end_date}.")
        else:
            print(f"Room '{room_name}' does not exist.")
    
    def _find_room_by_name(self, name):
        for room in self.rooms:
            if room.name == name:
                return room
        return None
    
    def is_room_available(self, room_name, start_date, end_date):
        room = self._find_room_by_name(room_name)
        if room:
            for booking in self.bookings:
                if booking.room == room and not (end_date <= booking.start_date or start_date >= booking.end_date):
                    return False
            return True
        return False
    
    def view_stats(self):
        today = datetime.now().date()
        total_rooms = len(self.rooms)
        rooms_occupied_today = len([b for b in self.bookings if b.start_date <= today <= b.end_date])
        rooms_available_today = total_rooms - rooms_occupied_today
        
        print(f"Total rooms: {total_rooms}")
        print(f"Rooms occupied today: {rooms_occupied_today}")
        print(f"Rooms available today: {rooms_available_today}")

class Room:
    def __init__(self, name, num_of_beds, fare_per_day):
        self.name = name
        self.num_of_beds = num_of_beds
        self.fare_per_day = fare_per_day

class Booking:
    def __init__(self, room, start_date, end_date):
        self.room = room
        self.start_date = start_date
        self.end_date = end_date

# Example usage
if __name__ == "__main__":
    hotel = Hotel("Grand Hotel", "123 Main St, Anytown")
    
    # Add rooms
    hotel.add_room("Deluxe Suite", 2, 200)
    hotel.add_room("Standard Room", 1, 100)
    
    # Book rooms
    hotel.book_room("Deluxe Suite", datetime.now().date(), datetime.now().date() + timedelta(days=2))
    
    # View stats
    hotel.view_stats()
    
    # Check availability
    future_date = datetime.now().date() + timedelta(days=3)
    print(f"Is 'Standard Room' available on {future_date}? {hotel.is_room_available('Standard Room', future_date, future_date + timedelta(days=1))}")