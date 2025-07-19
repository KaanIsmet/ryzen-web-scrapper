# Ryzen Web Scraper

A Python-based web scraping tool designed to extract and analyze AMD Ryzen processor data from web sources. This project provides automated data collection capabilities with robust HTML parsing and data processing features.

## Features

- **Web Data Extraction**: Efficiently scrapes Ryzen processor information from various web sources
- **HTML Parsing**: Utilizes BeautifulSoup with html5lib parser for reliable HTML processing
- **Data Processing**: Leverages pandas for structured data manipulation and analysis
- **HTTP Handling**: Built on the requests library for robust web communication

## Dependencies

- **requests**: HTTP library for making web requests
- **html5lib**: Standards-compliant HTML parser
- **pandas**: Data analysis and manipulation toolkit
- **beautifulsoup4**: HTML/XML parsing library

## Project Structure

This project uses `pyproject.toml` for modern Python project configuration and dependency management, following current Python packaging standards.

## Use Cases

- Market research and price comparison for AMD Ryzen processors
- Technical specification aggregation across multiple retailers
- Performance benchmarking data collection
- Inventory tracking and availability monitoring

## Installation

The project can be installed using pip with the `pyproject.toml` configuration:

```bash
pip install -e .
```

This will automatically install all required dependencies and set up the scraper for use.
