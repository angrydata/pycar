# import modules here

def main():
    pass # Placeholder -- remove this

    url = 'https://www.govtrack.us/api/v2/bill?congress=112&order_by=-current_status_date'

    # Read the `requests` documentation for information. I promise it
    # isn't that scary.
    # http://docs.python-requests.org/en/latest/user/quickstart/#json-response-content

    # Get the data using `requests`
    # (Don't forget to import the `requests` module

    # Since we know our data will be JSON, let's automatically convert
    # it to a Python dict. `requests` provides an easy-to-use function to do
    # this for us.

    # -- OR -- If the network is down, we can use a local version of this file.
    # Open the file

    # Convert it into a dict.

    # Print our dict in a human-readable way.

if __name__ == '__main__':
    main()
