# Data Parsing and Normalization Pipeline for SIEM

## Introduction

This project provides a simple and effective pipeline for parsing and normalizing log data for integration with SIEM systems. It demonstrates the collection, parsing, normalization, and storage of log data, preparing it for effective utilization in SIEM systems.

## Features

- **Data Collection**: Scripts for collecting log data (JSON format).
- **Data Parsing**: Extract relevant information from raw log data.
- **Data Normalization**: Convert data into a standardized format using Pandas.
- **Data Storage**: Store the normalized data in a CSV file for easy ingestion into SIEM systems.

## Prerequisites

- Python 3.x
- Pandas library
- Git (for version control)

## Installation

First, clone this repository to your local machine:

```bash
git clone https://github.com/CyberChrist010/Detection-Pipeline
cd your-repo-name
```
Setup Python and install Pandas

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

pip install pandas

```

## Usage
Data Collection: Place your log files in the logs directory. Ensure they are in JSON format.

Data Parsing: Run the parsing script to extract data from logs.

```bash
python parse_logs.py
```
Data Normalization: The parsing script automatically normalizes the data using Pandas and stores the output in the normalized_logs.csv file.

Data Integration: Manually import normalized_logs.csv into your SIEM system, or adjust the script for automatic integration based on your SIEM's API.

## Configuration
The current setup assumes log files in JSON format. To handle different formats, modify the parse_json_log function in parse_logs.py.

## Contributing
Contributions to this project are welcome! Please fork the repository and submit a pull request with your improvements.
