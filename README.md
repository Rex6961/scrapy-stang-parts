Вот пример README.md для вашего проекта на GitHub:

# Web Scraper Project

This is a web scraping project built with Python 3.12.2, Scrapy, python-dotenv, and openpyxl. It extracts data (name, part number, price, and availability) from a website.

## Prerequisites

- Python 3.12.2
- Virtual Environment (venv)
- Scrapy
- python-dotenv
- openpyxl

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/your-repo.git
```

2. Navigate to the project directory:

```
cd your-repo
```

3. Create and activate a virtual environment:

```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

4. Install the required packages:

```
pip install scrapy python-dotenv openpyxl
```

## Usage

1. Set up your environment variables by creating a `.env` file in the project root directory with the following structure:

```
WEBSITE_URL=https://example.com
```

2. Run the Scrapy spider:

```
scrapy crawl your_spider_name -o data.xlsx
```

This will scrape the data from the specified website and save it to an Excel file named `data.xlsx`.

## Project Structure

- `scrapy.cfg`: Scrapy configuration file
- `your_project/`: Your Scrapy project directory
  - `spiders/`: Directory for your spider files
  - `items.py`: Definition of the data model
  - `pipelines.py`: Pipeline for processing scraped data
  - `settings.py`: Project settings

## Contributing

Contributions are welcome! Please follow the standard GitHub workflow:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Commit your changes
4. Push your changes to your fork
5. Create a pull request

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Scrapy](https://scrapy.org/)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/)