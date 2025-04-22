import logging

# Set up logging configuration
logging.basicConfig(filename='app.log', level=logging.INFO)

def main():
    logging.info("Script started.")
    
    try:
        # Example code that could cause an error
        x = 10 / 0  # This will raise ZeroDivisionError
    except ZeroDivisionError as e:
        logging.error(f"Error occurred: {e}")
        # Handle the error gracefully, so it doesn't stop the script
        logging.info("Handled the division by zero error.")
        
    logging.info("Script completed.")

if __name__ == "__main__":
    main()
