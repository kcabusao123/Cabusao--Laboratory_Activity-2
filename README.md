# Cabusao--Laboratory_Activity-2

## Hotel Reservation System - OOP Implementation

This repository contains a **Hotel Reservation System** implemented in Python using Object-Oriented Programming (OOP) principles with comprehensive exception handling.

### 📋 Project Overview

This project demonstrates:
- ✅ Object-Oriented Programming (OOP) concepts
- ✅ Class design with user-defined attributes and methods
- ✅ Exception handling (try-except) for robust error management
- ✅ User input validation and processing
- ✅ Interactive menu-driven interface

### 📁 Repository Structure

```
.
├── hotel_reservation_system.py  # Main program with OOP implementation
├── answers.txt                  # Detailed explanations for design decisions
├── test_hotel_system.py        # Automated test suite
├── .gitignore                  # Git ignore file
└── README.md                   # This file
```

### 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/kcabusao123/Cabusao--Laboratory_Activity-2.git
   cd Cabusao--Laboratory_Activity-2
   ```

2. **Run the program:**
   ```bash
   python3 hotel_reservation_system.py
   ```

3. **Run the test suite:**
   ```bash
   python3 test_hotel_system.py
   ```

### 🎯 Features

#### HotelReservation Class
- **Attributes:**
  - `reservations` (dict): Stores all active reservations
  - `available_rooms` (list): Tracks available room numbers (101-120)

- **Methods:**
  - `make_reservation()`: Create new reservations with validation
  - `display_reservation()`: View details of specific reservations
  - `cancel_reservation()`: Cancel existing reservations
  - `display_available_rooms()`: Show all available rooms
  - `display_all_reservations()`: View all current bookings

#### User Input & Validation
- Room number validation (101-120)
- Guest count limit (1-4 guests per room)
- Guest name validation
- Double-booking prevention
- Integer input validation with error recovery

#### Exception Handling
- **ValueError**: For invalid values (room numbers, guest counts, etc.)
- **TypeError**: For incorrect data types
- **KeyboardInterrupt**: Graceful program exit on Ctrl+C
- Generic exception handler as safety net

### 📖 Menu Options

1. **Make a Reservation** - Book a room with guest details
2. **View Reservation** - Display details of a specific booking
3. **Cancel Reservation** - Remove an existing reservation
4. **View Available Rooms** - See all bookable rooms
5. **View All Reservations** - List all current bookings
6. **Exit** - Close the program

### 🧪 Testing

The test suite (`test_hotel_system.py`) includes 12 comprehensive tests:
- ✓ System initialization
- ✓ Making reservations
- ✓ Displaying reservations
- ✓ Canceling reservations
- ✓ Error handling for invalid inputs
- ✓ Double-booking prevention
- ✓ Guest limit enforcement
- ✓ Empty name validation

All tests pass successfully! ✅

### 📝 Documentation

See `answers.txt` for detailed explanations of:
1. Overall design and class structure justification
2. User input handling and exception handling role
3. Current limitations and potential improvements

### 🔒 Security

- No security vulnerabilities found (CodeQL verified)
- Input validation prevents common errors
- No hardcoded credentials or sensitive data

### 💡 Key OOP Concepts Demonstrated

- **Encapsulation**: Data and methods grouped in HotelReservation class
- **Abstraction**: Complex operations hidden behind simple method calls
- **Data Validation**: Robust input checking at multiple levels
- **Error Handling**: Comprehensive try-except blocks throughout

### 🎓 Academic Requirements Met

✅ At least one class with user-defined attributes  
✅ Minimum of two user-defined methods (implemented 5)  
✅ Accepts user input with validation  
✅ Demonstrates proper exception handling (try-except)  
✅ Answers all required questions in answers.txt

---

**Author:** kcabusao123  
**Course:** Laboratory Activity 2 - OOP Implementation  
**Language:** Python 3.12+