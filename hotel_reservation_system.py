"""
Hotel Reservation System
A Python program demonstrating Object-Oriented Programming (OOP) concepts
with exception handling for managing hotel room reservations.
"""


class HotelReservation:
    """
    A class to represent a hotel reservation system.
    
    Attributes:
        reservations (dict): Dictionary to store all reservations with room numbers as keys
        available_rooms (list): List of available room numbers
    """
    
    def __init__(self):
        """Initialize the hotel reservation system with available rooms."""
        self.reservations = {}
        self.available_rooms = list(range(101, 121))  # Rooms 101-120
    
    def make_reservation(self, guest_name, room_number, check_in_date, check_out_date, num_guests):
        """
        Create a new reservation for a guest.
        
        Args:
            guest_name (str): Name of the guest
            room_number (int): Room number to reserve
            check_in_date (str): Check-in date
            check_out_date (str): Check-out date
            num_guests (int): Number of guests
            
        Raises:
            ValueError: If room number is invalid or already reserved
            TypeError: If input types are incorrect
        """
        try:
            # Validate room number
            if not isinstance(room_number, int):
                raise TypeError("Room number must be an integer")
            
            if room_number not in range(101, 121):
                raise ValueError("Invalid room number. Please choose between 101-120")
            
            if room_number not in self.available_rooms:
                raise ValueError(f"Room {room_number} is already reserved")
            
            # Validate number of guests
            if not isinstance(num_guests, int) or num_guests < 1:
                raise ValueError("Number of guests must be a positive integer")
            
            if num_guests > 4:
                raise ValueError("Maximum 4 guests allowed per room")
            
            # Validate guest name
            if not guest_name or not isinstance(guest_name, str):
                raise ValueError("Guest name must be a non-empty string")
            
            # Create reservation
            self.reservations[room_number] = {
                'guest_name': guest_name,
                'check_in_date': check_in_date,
                'check_out_date': check_out_date,
                'num_guests': num_guests
            }
            
            # Remove from available rooms
            self.available_rooms.remove(room_number)
            
            print(f"\n✓ Reservation successful!")
            print(f"Room {room_number} has been reserved for {guest_name}")
            
        except ValueError as ve:
            print(f"\n✗ Error: {ve}")
            raise
        except TypeError as te:
            print(f"\n✗ Error: {te}")
            raise
    
    def display_reservation(self, room_number):
        """
        Display details of a specific reservation.
        
        Args:
            room_number (int): Room number to display
            
        Raises:
            ValueError: If room number is invalid or has no reservation
        """
        try:
            if not isinstance(room_number, int):
                raise TypeError("Room number must be an integer")
            
            if room_number not in self.reservations:
                raise ValueError(f"No reservation found for room {room_number}")
            
            reservation = self.reservations[room_number]
            print("\n" + "="*50)
            print("RESERVATION DETAILS")
            print("="*50)
            print(f"Room Number: {room_number}")
            print(f"Guest Name: {reservation['guest_name']}")
            print(f"Check-in Date: {reservation['check_in_date']}")
            print(f"Check-out Date: {reservation['check_out_date']}")
            print(f"Number of Guests: {reservation['num_guests']}")
            print("="*50)
            
        except (ValueError, TypeError) as e:
            print(f"\n✗ Error: {e}")
            raise
    
    def cancel_reservation(self, room_number):
        """
        Cancel an existing reservation.
        
        Args:
            room_number (int): Room number to cancel
            
        Raises:
            ValueError: If room number is invalid or has no reservation
        """
        try:
            if not isinstance(room_number, int):
                raise TypeError("Room number must be an integer")
            
            if room_number not in self.reservations:
                raise ValueError(f"No reservation found for room {room_number}")
            
            guest_name = self.reservations[room_number]['guest_name']
            del self.reservations[room_number]
            self.available_rooms.append(room_number)
            self.available_rooms.sort()
            
            print(f"\n✓ Reservation cancelled successfully!")
            print(f"Room {room_number} (Guest: {guest_name}) is now available")
            
        except (ValueError, TypeError) as e:
            print(f"\n✗ Error: {e}")
            raise
    
    def display_available_rooms(self):
        """Display all available rooms."""
        if self.available_rooms:
            print(f"\nAvailable Rooms: {', '.join(map(str, self.available_rooms))}")
            print(f"Total Available: {len(self.available_rooms)} rooms")
        else:
            print("\nNo rooms available at the moment")
    
    def display_all_reservations(self):
        """Display all current reservations."""
        if not self.reservations:
            print("\nNo reservations found")
            return
        
        print("\n" + "="*50)
        print("ALL RESERVATIONS")
        print("="*50)
        for room_num, details in sorted(self.reservations.items()):
            print(f"\nRoom {room_num}: {details['guest_name']}")
            print(f"  Check-in: {details['check_in_date']}")
            print(f"  Check-out: {details['check_out_date']}")
            print(f"  Guests: {details['num_guests']}")
        print("="*50)


def get_integer_input(prompt, min_value=None, max_value=None):
    """
    Helper function to get integer input with validation.
    
    Args:
        prompt (str): Input prompt message
        min_value (int): Minimum allowed value
        max_value (int): Maximum allowed value
        
    Returns:
        int: Validated integer input
    """
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f"✗ Value must be at least {min_value}")
                continue
            if max_value is not None and value > max_value:
                print(f"✗ Value must be at most {max_value}")
                continue
            return value
        except ValueError:
            print("✗ Invalid input. Please enter a valid number")


def main():
    """Main function to run the Hotel Reservation System."""
    hotel = HotelReservation()
    
    print("\n" + "="*50)
    print("WELCOME TO HOTEL RESERVATION SYSTEM")
    print("="*50)
    
    while True:
        print("\n--- MENU ---")
        print("1. Make a Reservation")
        print("2. View Reservation")
        print("3. Cancel Reservation")
        print("4. View Available Rooms")
        print("5. View All Reservations")
        print("6. Exit")
        
        try:
            choice = get_integer_input("\nEnter your choice (1-6): ", 1, 6)
            
            if choice == 1:
                # Make a reservation
                print("\n--- MAKE A RESERVATION ---")
                hotel.display_available_rooms()
                
                try:
                    guest_name = input("\nEnter guest name: ").strip()
                    room_number = get_integer_input("Enter room number (101-120): ", 101, 120)
                    check_in_date = input("Enter check-in date (e.g., 2024-01-15): ").strip()
                    check_out_date = input("Enter check-out date (e.g., 2024-01-20): ").strip()
                    num_guests = get_integer_input("Enter number of guests (1-4): ", 1, 4)
                    
                    hotel.make_reservation(guest_name, room_number, check_in_date, 
                                         check_out_date, num_guests)
                except (ValueError, TypeError):
                    print("Reservation failed. Please try again.")
            
            elif choice == 2:
                # View reservation
                print("\n--- VIEW RESERVATION ---")
                try:
                    room_number = get_integer_input("Enter room number: ")
                    hotel.display_reservation(room_number)
                except (ValueError, TypeError):
                    print("Could not display reservation.")
            
            elif choice == 3:
                # Cancel reservation
                print("\n--- CANCEL RESERVATION ---")
                try:
                    room_number = get_integer_input("Enter room number to cancel: ")
                    hotel.cancel_reservation(room_number)
                except (ValueError, TypeError):
                    print("Cancellation failed. Please try again.")
            
            elif choice == 4:
                # View available rooms
                hotel.display_available_rooms()
            
            elif choice == 5:
                # View all reservations
                hotel.display_all_reservations()
            
            elif choice == 6:
                # Exit
                print("\nThank you for using Hotel Reservation System!")
                print("Goodbye!")
                break
        
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user.")
            print("Goodbye!")
            break
        except Exception as e:
            print(f"\n✗ An unexpected error occurred: {e}")
            print("Please try again.")


if __name__ == "__main__":
    main()
