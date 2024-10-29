# Persian Calendar Holiday Events Web Scraping Project

This Python project performs web scraping to retrieve Persian holiday and event data from the `time.ir` website. It processes the data and saves it in a structured CSV format. The output CSV includes holidays and important events across various calendar types (Gregorian, Jalali, and Hijri).

## Features

- Scrapes event data for each month across years 1395 to 1403.
- Extracts information such as event title, holiday status, and dates in multiple calendar formats.
- Outputs results to `Holidays.csv` in UTF-8 format for easy use with Persian text.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/hkhajei/Persian-Calendar-Holiday-Events-Web-Scraping-Project.git
    ```
2. Install required dependencies:
    ```bash
    pip install requests pandas
    ```

## Usage

1. Run the script:
    ```bash
    python holiday_events.py
    ```
2. The output file `Holidays.csv` will be generated in the project directory.

## Example Output

The output CSV file includes columns such as:

| id  | title                    | gregorian_year | gregorian_month | gregorian_day | jalali_year | jalali_month | jalali_day | hijri_year | hijri_month | hijri_day | is_holiday | event_type |
| --- | ------------------------- | -------------- | --------------- | ------------- | ----------- | ------------ | ---------- | ---------- | ----------- | --------- | ---------- | ---------- |
| 1   | نوروز (New Year)         | 2016          | 3               | 20            | 1395        | 1            | 1          | 1437       | 6           | 10        | TRUE       | Holiday    |

## Notes

- **Web Scraping**: This project scrapes data from a website, which may be subject to the site's terms of service.
- **Error Handling**: The script includes basic error handling for failed requests.

## License

This project is licensed under the MIT License.

## Educational Purpose

This project and the data it retrieves are shared solely for educational purposes. Please use the information responsibly and adhere to the relevant copyright and licensing agreements.

