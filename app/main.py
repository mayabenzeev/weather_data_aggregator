import argparse
import os
import sys
import json
from typing import Dict, Any

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import services.weather_service as weather_service

def format_response(success: bool, message: str, data: Dict[str, Any] = None) -> str:
    """Format the response as a JSON string"""
    response = {
        "status": "success" if success else "error",
        "message": message,
    }
    if data:
        response["data"] = data
    return json.dumps(response, indent=2)

class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        print(format_response(False, f"Command line error: {message}"))
        sys.exit(2)

def run_cli():
    """
    Run the weather app from CLI arguments
    """
    try:
        # handle cli arguments
        parser = CustomArgumentParser(description="Weather CLI")
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
                try:
                    city_json = weather_service.fetch_city_json(city, return_json=True)
                    if city_json:
                        print(format_response(True, f"Fetched weather data for {city}, saved in data/{city}.json"))
                except Exception as e:
                    print(format_response(False, str(e)))
        elif args.command == "analyze":
            try:
                analysis = weather_service.get_weather_info(args.city)
                print(format_response(True, f"Analysis for {args.city}", analysis))
            except Exception as e:
                print(format_response(False, str(e)))

    except Exception as e:
        print(format_response(False, str(e)))

if __name__ == "__main__":
    run_cli()

