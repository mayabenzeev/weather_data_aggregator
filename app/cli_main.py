import argparse
import os
import requests

import app.services.weather_service as weather_service

def run_cli():
    """
    Run the weather app from CLI arguments
    """

    # handle cli arguments
    parser = argparse.ArgumentParser(description="Weather CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # add subparser for fetch command
    fetch_subparser = subparsers.add_parser("fetch", help="Fetch the weather of a city")
    fetch_subparser.add_argument("--cities", nargs="+",  help="List of cities", required=True)

    # add subparser for analyze command
    analyze_subparser = subparsers.add_parser("analyze", help="Analyze the weather of a city")
    analyze_subparser.add_argument("--city", help="The city to analyze", required=True)

    args = parser.parse_args()
    
    if args.command == "fetch":
        for city in args.cities:
            print(weather_service.fetch_weather(city))
    elif args.command == "analyze":
        print(weather_service.analyze_weather(args.city))




