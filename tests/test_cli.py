#!/usr/bin/env python3
import sys
from cli import parse_arguments
import pytest

def test_city_is_required():
    sys.argv = ["main.py"]

    with pytest.raises(SystemExit):
        parse_arguments()

def test_parse_arguments():
    sys.argv = ["main.py","--city", "Pune"]

    args = parse_arguments()

    assert args.city == "Pune"
    assert args.json is False

def test_json_argument():
    sys.argv = ["main.py", "--city", "Pune", "--json"]

    args = parse_arguments()

    assert args.city == "Pune"
    assert args.json is True