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

    city = parse_arguments()

    assert city == "Pune"