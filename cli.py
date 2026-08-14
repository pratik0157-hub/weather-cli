#!/usr/bin/env python3

import argparse

def parse_arguments():
    # Create an argument parser for command-line input
    parser = argparse.ArgumentParser()

    # Add a required argument to accept the city name
    parser.add_argument("-c","--city", required=True, help="Enter the name of the city")
    parser.add_argument("--json", action="store_true", help="Gives out data in json form")
    parser.add_argument("--forecast", action="store_true", help="Gives weather forecast for the next five days")

    # Parse the arguments entered by the user
    args = parser.parse_args()

    # Return all values of the arguments
    return args