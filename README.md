# Website Auto Refresher

This Python script automates the process of refreshing a website for a specified number of times. It sends a GET request to the specified URL and waits for a random duration between 1 and 8 seconds before each refresh.

## Requirements

- Python 3.x
- requests library (`pip install requests`)

## Usage

1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the script using the following command:

    ```
    python auto_refresh.py
    ```

5. Provide the URL of the website you want to refresh when prompted.
6. Sit back and watch as the script refreshes the website for the specified number of times!

## Parameters

- `refresh_count`: Number of times to refresh the page (default: 20)
- `url`: URL of the website to refresh

## Example

Refresh the Google homepage 20 times:

```bash
python auto_refresh.py
