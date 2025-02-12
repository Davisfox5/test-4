import pytest
from app import main

def test_main():
    assert main() == "Hello from minimal app.py"