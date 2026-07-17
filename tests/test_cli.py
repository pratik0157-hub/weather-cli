#!/usr/bin/env python3
import sys
from cli import parse_arguments

def test_parse_arguments():
    sys.argv = ["main.py", "Pune"]

    city = parse_arguments()

    assert city == "Pune"