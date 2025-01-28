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
        {'topic': 'Top upcoming US market earnings this week', 'current_year': str(datetime.now().year), 'date': str(datetime.now().strftime("%Y-%m-%d"))},
        {'topic': 'Fitness News', 'current_year': str(datetime.now().year), 'date': str(datetime.now().strftime("%Y-%m-%d"))},
        {'topic': 'Crypto Updates', 'current_year': str(datetime.now().year), 'date': str(datetime.now().strftime("%Y-%m-%d"))},
        {'topic': 'Top undervalued stocks', 'current_year': str(datetime.now().year), 'date': str(datetime.now().strftime("%Y-%m-%d"))}
    ]

    for inputs in inputs_array:
        Mynews().crew().kickoff_for_each(inputs=inputs_array)

run()