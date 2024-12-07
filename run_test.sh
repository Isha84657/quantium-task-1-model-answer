#!/bin/bash

# Activate the project virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Check if activation was successful
if [ $? -ne 0 ]; then
    echo "Failed to activate virtual environment."
    exit 1
fi

# Execute the test suite using pytest
echo "Running the test suite..."
pytest test_app.py

# Check if pytest was successful
if [ $? -eq 0 ]; then
    echo "All tests passed!"
    exit 0
else
    echo "Some tests failed."
    exit 1
fi
