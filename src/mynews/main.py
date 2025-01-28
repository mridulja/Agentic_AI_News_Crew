#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from crew import Mynews

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Top news in Telecom',
        'current_year': str(datetime.now().year),
        'date': str(datetime.now().strftime("%Y-%m-%d"))
    }

    inputs_array = [
        {'topic': 'Upcoming US market earnings reports', 'current_year': str(datetime.now().year), 'date': str(datetime.now().strftime("%Y-%m-%d"))},
        {'topic': 'AI news and updates', 'current_year': str(datetime.now().year), 'date': str(datetime.now().strftime("%Y-%m-%d"))},
        {'topic': 'Nonprofit news', 'current_year': str(datetime.now().year), 'date': str(datetime.now().strftime("%Y-%m-%d"))},
        {'topic': 'Best stocks opportunities', 'current_year': str(datetime.now().year), 'date': str(datetime.now().strftime("%Y-%m-%d"))}
    ]

    for inputs in inputs_array:
        Mynews().crew().kickoff_for_each(inputs=inputs_array)

run()