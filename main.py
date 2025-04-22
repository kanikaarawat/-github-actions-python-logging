import logging

# Configure logging to save logs to app.log
logging.basicConfig(filename='app.log', level=logging.INFO)

def main():
    logging.info("Script started.")
    try:
        x = 10 / 0  # This will raise ZeroDivisionError
    except ZeroDivisionError as e:
        logging.error(f"Error occurred: {e}")
        raise  # Re-raise to fail the CI build

if __name__ == "__main__":
    main()
