import argparse
import os
import requests

# @app.post("/fetc_h")
# def fetch_citiesweather():
    
# handle cli arguments
parser = argparse.ArgumentParser(description="Weather CLI")
subparsers = parser.add_subparsers(dest="command", required=True)

# add subparser for fetch command
fetch_subparser = subparsers.add_parser("fetch", help="Fetch the weather of a city")
fetch_subparser.add_argument("--cities", nargs="+",  help="List of cities", required=True)

# add subparser for analyze command
analyze_parser = subparsers.add_parser("analyze", help="Analyze the weather of a city")
analyze_parser.add_argument("--city", help="The city to analyze", required=True)


parser.add_argument("--city",
                     type=str,
                       help="The city to analyze",
                         required=True, default="Tel Aviv")
args = parser.parse_args()

# analyze the weather of the city
print(analyze_city_weather(args.city))


# HANDLE RESTAPI REQUESTS

if __name__ == "__main__":

