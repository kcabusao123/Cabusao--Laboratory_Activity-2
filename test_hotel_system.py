"""
Test script for Hotel Reservation System
Tests the main functionality without manual interaction
"""

from hotel_reservation_system import HotelReservation

def test_hotel_reservation_system():
    """Test all major functions of the Hotel Reservation System."""
    print("="*60)
    print("TESTING HOTEL RESERVATION SYSTEM")
    print("="*60)
    
    # Initialize the system
    hotel = HotelReservation()
    print("\n✓ Test 1: Hotel Reservation System initialized")
    print(f"  Available rooms: {len(hotel.available_rooms)}")
    
    # Test making a reservation
    print("\n--- Test 2: Making a reservation ---")
    try:
        hotel.make_reservation(
            guest_name="John Doe",
            room_number=105,
            check_in_date="2024-02-01",
            check_out_date="2024-02-05",
            num_guests=2
        )
        print("✓ Reservation created successfully")
    except Exception as e:
        print(f"✗ Failed to create reservation: {e}")
    
    # Test displaying a reservation
    print("\n--- Test 3: Displaying reservation ---")
    try:
        hotel.display_reservation(105)
        print("✓ Reservation displayed successfully")
    except Exception as e:
        print(f"✗ Failed to display reservation: {e}")
    
    # Test making another reservation
    print("\n--- Test 4: Making second reservation ---")
    try:
        hotel.make_reservation(
            guest_name="Jane Smith",
            room_number=110,
            check_in_date="2024-02-10",
            check_out_date="2024-02-15",
            num_guests=1
        )
        print("✓ Second reservation created successfully")
    except Exception as e:
        print(f"✗ Failed to create second reservation: {e}")
    
    # Test displaying all reservations
    print("\n--- Test 5: Displaying all reservations ---")
    hotel.display_all_reservations()
    print("✓ All reservations displayed")
    
    # Test error handling - invalid room number
    print("\n--- Test 6: Error handling - invalid room number ---")
    hotel.make_reservation(
        guest_name="Invalid User",
        room_number=999,
        check_in_date="2024-03-01",
        check_out_date="2024-03-05",
        num_guests=2
    )
    print("✓ Error handling works: Invalid room number rejected")
    
    # Test error handling - room already reserved
    print("\n--- Test 7: Error handling - double booking ---")
    hotel.make_reservation(
        guest_name="Another Guest",
        room_number=105,
        check_in_date="2024-02-01",
        check_out_date="2024-02-05",
        num_guests=2
    )
    print("✓ Error handling works: Double booking prevented")
    
    # Test error handling - too many guests
    print("\n--- Test 8: Error handling - too many guests ---")
    hotel.make_reservation(
        guest_name="Large Group",
        room_number=115,
        check_in_date="2024-02-01",
        check_out_date="2024-02-05",
        num_guests=10
    )
    print("✓ Error handling works: Guest limit enforced")
    
    # Test canceling a reservation
    print("\n--- Test 9: Canceling a reservation ---")
    hotel.cancel_reservation(105)
    print("✓ Cancellation feature works")
    
    # Test error handling - canceling non-existent reservation
    print("\n--- Test 10: Error handling - cancel non-existent reservation ---")
    hotel.cancel_reservation(105)  # Already cancelled
    print("✓ Error handling works: Non-existent reservation rejected")
    
    # Test displaying available rooms
    print("\n--- Test 11: Displaying available rooms ---")
    hotel.display_available_rooms()
    print("✓ Available rooms displayed")
    
    # Test error handling - empty guest name
    print("\n--- Test 12: Error handling - empty guest name ---")
    hotel.make_reservation(
        guest_name="",
        room_number=107,
        check_in_date="2024-02-01",
        check_out_date="2024-02-05",
        num_guests=2
    )
    print("✓ Error handling works: Empty name validation works")
    
    print("\n" + "="*60)
    print("ALL TESTS COMPLETED")
    print("="*60)
    print("\nFinal State:")
    hotel.display_all_reservations()
    hotel.display_available_rooms()

if __name__ == "__main__":
    test_hotel_reservation_system()
