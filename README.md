# Cabusao--Laboratory_Activity-2

HOTEL RESERVATION SYSTEM - DESIGN EXPLANATIONS
===============================================

QUESTION 1: Explain the overall design of your program and justify why you chose this particular class structure and set of user-defined methods.

ANSWER:

Overall Design:
The program is designed around a single class called "HotelReservation" that encapsulates all the functionality needed to manage hotel room reservations. This follows the Object-Oriented Programming principle of encapsulation, where related data and methods are grouped together in a cohesive unit.

Class Structure Justification:
I chose a single-class design because:
1. Simplicity: A hotel reservation system at its core manages a collection of reservations, which can be effectively handled by one class.
2. Cohesion: All methods (make_reservation, display_reservation, cancel_reservation) directly relate to managing reservations and belong together.
3. Data Encapsulation: The class encapsulates two main attributes:
   - reservations (dict): Stores all active reservations with room numbers as keys
   - available_rooms (list): Tracks which rooms are currently available
   This keeps the data organized and prevents external code from directly manipulating the reservation data.

User-Defined Methods:
I implemented five primary methods, each serving a distinct purpose:

1. make_reservation(guest_name, room_number, check_in_date, check_out_date, num_guests):
   - Purpose: Creates new reservations
   - Justification: This is the core functionality of any reservation system
   - Validates all inputs (room availability, guest count limits, valid room numbers)

2. display_reservation(room_number):
   - Purpose: Shows details of a specific reservation
   - Justification: Users need to view their booking information
   - Provides formatted output for easy reading

3. cancel_reservation(room_number):
   - Purpose: Removes a reservation and frees up the room
   - Justification: Cancellations are a necessary business function
   - Properly updates both the reservations dictionary and available_rooms list

4. display_available_rooms():
   - Purpose: Shows which rooms can be booked
   - Justification: Helps users make informed decisions when booking

5. display_all_reservations():
   - Purpose: Shows all current reservations
   - Justification: Useful for hotel management to see occupancy status

This method structure covers the complete CRUD (Create, Read, Update, Delete) operations needed for a reservation system, though Update is simplified to cancel-and-recreate in this implementation.


QUESTION 2: Describe how user input is handled in your program and discuss the role of exception handling (try–except) in preventing incorrect or unexpected behavior.

ANSWER:

User Input Handling:
The program handles user input at two levels:

1. Menu Selection:
   - Uses a helper function get_integer_input() that validates integer inputs
   - Ensures users enter valid menu choices (1-6)
   - Loops until valid input is received

2. Reservation Data:
   - Collects guest name (string), room number (integer), dates (strings), and number of guests (integer)
   - Each input is validated before being processed

Exception Handling Strategy:
The program uses try-except blocks extensively to handle various error scenarios:

1. Type Validation:
   - TypeError is raised when inputs are of incorrect types
   - Example: If room_number is not an integer, the system catches it
   
2. Value Validation:
   - ValueError is raised for logically incorrect values
   - Examples:
     * Room number outside valid range (101-120)
     * Room already reserved
     * More than 4 guests per room
     * Empty guest name

3. Specific Exception Handling in Methods:
   - make_reservation(): Catches ValueError and TypeError, displays user-friendly messages
   - display_reservation(): Handles cases where room number doesn't exist
   - cancel_reservation(): Prevents canceling non-existent reservations

4. Input Conversion Protection:
   - get_integer_input() wraps int() conversion in try-except
   - Catches ValueError when user enters non-numeric input
   - Prompts user to try again instead of crashing

5. Graceful Degradation:
   - Main menu loop has a broad Exception handler as a safety net
   - KeyboardInterrupt is caught to handle Ctrl+C gracefully
   - Program never crashes unexpectedly; always provides feedback

Role of Exception Handling:
Exception handling prevents:
- Program crashes from invalid input
- Data corruption (e.g., double-booking rooms)
- Confusing error messages for end users
- Silent failures that leave the system in an inconsistent state

It ensures the program is robust and user-friendly, guiding users to correct their mistakes rather than terminating abruptly.


QUESTION 3: Identify one limitation of your current implementation and explain how it could be improved using additional OOP concepts or better error handling.

ANSWER:

Limitation: Single Reservation Per Room Without Date Management

Current Issue:
The current implementation only tracks whether a room is reserved or available, but doesn't handle overlapping dates. Once a room is booked, it remains unavailable until the reservation is cancelled, even if someone wants to book it for dates after the current guest checks out. This is unrealistic for a real hotel system.

For example:
- Guest A books room 101 for Jan 1-5
- Guest B wants to book room 101 for Jan 10-15
- Current system: Rejects Guest B because room 101 is "reserved"
- Real system should: Allow booking since dates don't overlap

How to Improve Using OOP Concepts:

1. Create Additional Classes (Composition):
   - Create a separate "Reservation" class to represent individual bookings
   - Create a "Guest" class to store guest information
   - Create a "Room" class to represent room properties
   
   Example structure:
   class Guest:
       def __init__(self, name, contact_info):
           self.name = name
           self.contact_info = contact_info
   
   class Room:
       def __init__(self, room_number, room_type, capacity):
           self.room_number = room_number
           self.room_type = room_type
           self.capacity = capacity
   
   class Reservation:
       def __init__(self, guest, room, check_in, check_out):
           self.guest = guest
           self.room = room
           self.check_in = check_in
           self.check_out = check_out
       
       def overlaps_with(self, other_reservation):
           # Check if dates overlap
           pass

2. Implement Date Validation (Better Error Handling):
   - Use Python's datetime module to validate dates
   - Check that check_out_date is after check_in_date
   - Prevent booking dates in the past
   - Calculate stay duration and pricing
   
   Example:
   from datetime import datetime
   
   def validate_dates(self, check_in, check_out):
       try:
           check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
           check_out_date = datetime.strptime(check_out, "%Y-%m-%d")
           
           if check_out_date <= check_in_date:
               raise ValueError("Check-out must be after check-in")
           
           if check_in_date < datetime.now():
               raise ValueError("Cannot book dates in the past")
               
       except ValueError as e:
           raise ValueError(f"Invalid date: {e}")

3. Implement Inheritance (OOP Enhancement):
   - Create a base "RoomReservation" class
   - Derive specialized classes like "StandardReservation", "SuiteReservation"
   - Each can have different pricing, amenities, or cancellation policies

4. Add Data Persistence:
   - Currently, all data is lost when program exits
   - Could implement file I/O or database connection to save reservations
   - Add load/save methods with proper exception handling for file operations

These improvements would make the system more realistic and production-ready while demonstrating advanced OOP concepts like composition, inheritance, and polymorphism, plus more sophisticated error handling for date validation and data persistence.
