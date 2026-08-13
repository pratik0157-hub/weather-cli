#!/usr/bin/env python3

import argparse

def parse_arguments():
    # Create an argument parser for command-line input
    parser = argparse.ArgumentParser()

    # Add a required argument to accept the city name
    parser.add_argument("-c","--city", required=True, help="Enter the name of the city")
    parser.add_argument("--json", action="store_true", help="Gives out data in json form")

    # Parse the arguments entered by the user
    args = parser.parse_args()

    # Return only the city name instead of the whole Namespace object
    return args