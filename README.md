# Data Parsing and Normalization Pipeline for SIEM

## Introduction

This project provides a simple and effective pipeline for parsing and normalizing log data for integration with SIEM systems. It demonstrates the collection, parsing, normalization, and storage of log data, preparing it for effective utilization in SIEM systems. 

## Please Note: You will need to update the file names (depending on your use case) and paths to the logs in each script as all enviornments are built differently! This Repo and pipeline is built as an example and is pulled from my scripts and notes from over the years working in Linux, Windows and with different vendors for Cloud, Firewalls, IDSs and SIEMs and as such, I have made my notes and scripts public as was requested for job interview(s) and I welcome any comments or suggestions!

## Features

- **Data Collection**: Scripts for collecting log data (JSON format).
- **Data Parsing**: Extract relevant information from raw log data.
- **Data Normalization**: Convert data into a standardized format using Pandas.
- **Data Storage**: Store the normalized data in a CSV file for easy ingestion into SIEM systems.
- **Easily Adptable for Automated Pipeline**: Use Jenkins or other pipeline tools to automate the parsing and normalization steps to be imported into SIEM.

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
pip install pandas python-dateutil

```

## Usage
Data Collection: Place your log files in the logs directory. Ensure they are in JSON format.

Data Parsing: Run the parsing script to extract data from logs. Update the name/scripts needed for each type of use case.

```bash
python parse_logs.py
```
Data Normalization: The parsing script automatically normalizes the data using Pandas and stores the output in the normalized_logs.csv file.

Data Integration: Manually import normalized_logs.csv into your SIEM system, or adjust the script for automatic integration based on your SIEM's API.

## Configuration
The current setup assumes log files in JSON format. To handle different formats, modify the parse_json_log function in parse_logs.py.

## Contributing and Thanks!
Contributions to this project are welcome! Please fork the repository and submit a pull request with your improvements.

I sourced (but did not directly copy) information from the following Repo to help with creating scripts for parsing and normalizing different log files: https://github.com/OTRF/OSSEM-DD. Many Thanks for their hardwork!
