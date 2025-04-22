import logging

# Set up logging to capture output for the HTML file
logging.basicConfig(filename='app.log', level=logging.INFO)

def main():
    logging.info("Script started.")
    
    try:
        x = 10 / 0  # This will raise ZeroDivisionError
    except ZeroDivisionError as e:
        logging.error(f"Error occurred: {e}")
    
    logging.info("Script completed.")

    # Generate HTML content based on the log
    with open('output.html', 'w') as f:
        f.write('<html><body>')
        f.write('<h1>Python Script Output</h1>')
        f.write('<h2>Logs:</h2>')
        with open('app.log', 'r') as log_file:
            logs = log_file.readlines()
            for log in logs:
                f.write(f'<p>{log}</p>')
        f.write('</body></html>')

if __name__ == "__main__":
    main()
