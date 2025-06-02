import argparse
from app.fetcher import fetch_and_store
from app.analytics import analyze_city

def main():
    parser = argparse.ArgumentParser(description="Weather Data Aggregator")
    subparsers = parser.add_subparsers(dest="command")

    fetch_parser = subparsers.add_parser("fetch")
    fetch_parser.add_argument("--cities", nargs="+", required=True)

    analyze_parser = subparsers.add_parser("analyze")
    analyze_parser.add_argument("--city", required=True)

    args = parser.parse_args()

    if args.command == "fetch":
        fetch_and_store(args.cities)
    elif args.command == "analyze":
        analyze_city(args.city)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
