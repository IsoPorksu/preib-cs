import json

def import_file():
    """
    Import the co-ordinate file.

    Returns:
        contents of the coordinates.json file as a dictionary (which means we can look things up in it later)
    """
    try: # Try opening the file and loading its contents
        with open('coordinates.json', 'r') as file:
            return json.load(file) # The data is in a JSON file (this is detailed more in README.md), so load it into a dictionary with json.load()
    except Exception as e: # If that doesn't work, print a nice error message; "Exception as e" means that we can print e to get details about the error
        print(f"Oopsie! There was an error opening the JSON file: {e}")
        exit() # We can't load the file, so exit the program (nothing in the program will work if the file can't be loaded)

def get_input():
    """
    Get user input for the place they want to look up.

    Returns:
        The place name as a string.
    """
    place = input("\nEnter the Prisma you want to look for: ")
    # We remove any extra spaces from the input and we make it all lowercase so that it doesn't matter how the user types it
    formatted_input = place.strip().lower()
    return formatted_input

def get_location(coordinates, place):
    """
    Search for the given place in the data.

    Args:
        data: the dictionary containing place names and their coordinates.
        place: the place name to look up (this was given by the user).

    Returns:
        the coordinates as a tuple (latitude, longitude) if found, else None.
    """
    try: # Try searching through the dictionary to find the location
        latitude, longitude = coordinates[place]
        return (latitude, longitude)
    except: # If the search goes wrong, return None
        return None

def display_results(place, location):
    """
    Display the results of the search.

    Args:
        place: the place name that was looked up.
        coordinates: the coordinates tuple (latitude, longitude) or None if not found.
    """
    # If the co-ordinates were found (in other words, they are not None), print them out
    if location is not None:
        latitude, longitude = location # Unpack the tuple into separate latitude and longitude co-ordinates
        print(f"The coordinates of Prisma {place.title()} are ({latitude}, {longitude}).")
    else: # If the co-ordinates were not found, tell the user
        print(f"Sorry, there was no Prisma found at {place}.")

def main():
    """
    Run all the other functions in the right order.
    """
    coordinates = import_file() # Load the coordinates from the file
    while True: # Run continuously until the user decides to stop
        try: # Try to run all the functions in the right order
            place = get_input() # Get the input from the user
            location = get_location(coordinates, place) # Get the location of the place
            display_results(place, location) # Display the results to the user
        except KeyboardInterrupt: # If the user presses Ctrl+C (which causes something called a KeyboardInterrupt), exit the program gracefully
            print("\nThe program will now finish.")
            break # Exit the while True loop, which will effectively end the program
        except Exception as e: # If the program encounters any other error, print a nice error message
            print(f"Oopsie! The program encountered an error: {e}")

# Run the main function to start the program
main()
