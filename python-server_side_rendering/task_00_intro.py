"""
task_00_intro.py

Function: generate_invitations(template, attendees)
Creates sequential output_X.txt invitation files from a template and a list
of attendee dictionaries. Implements the error handling described in the
exercise instructions.

Usage:
    from task_00_intro import generate_invitations
    with open('template.txt', 'r') as f:
        template_content = f.read()
    generate_invitations(template_content, attendees)
"""

import os
from typing import List, Dict, Any


def generate_invitations(template: str, attendees: List[Dict[str, Any]]):
    """
    Generate invitation files from a template string and a list of attendee dicts.

    Rules and behavior implemented:
    - Validate that `template` is a string and `attendees` is a list of dicts.
    - If the template is empty -> print error and return without creating files.
    - If attendees list is empty -> print message and return without creating files.
    - For each attendee, missing or None values for placeholders are replaced with "N/A".
    - Output files are named output_1.txt, output_2.txt, ... and written to the
      current working directory. If a write error occurs it is logged but the
      function continues processing remaining attendees.
    """

    # Validate types
    if not isinstance(template, str):
        print(f"Invalid input type: template must be a string, got {type(template).__name__}.")
        return

    if not isinstance(attendees, list):
        print(f"Invalid input type: attendees must be a list of dictionaries, got {type(attendees).__name__}.")
        return

    # Check empty template
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Check empty attendees list
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Expected placeholders (based on the provided template)
    expected_keys = ["name", "event_title", "event_date", "event_location"]

    # Validate each item in attendees is a dict
    for idx, item in enumerate(attendees, start=1):
        if not isinstance(item, dict):
            print(f"Invalid input type: attendee at index {idx} is not a dictionary (got {type(item).__name__}).")
            return

    # Process attendees
    for i, person in enumerate(attendees, start=1):
        # Build a safe mapping where missing or None values become 'N/A'
        mapping = {}
        for k in expected_keys:
            val = person.get(k) if isinstance(person, dict) else None
            if val is None:
                mapping[k] = "N/A"
            else:
                # Convert other types to string as needed
                mapping[k] = str(val)

        # Use str.format to substitute placeholders
        try:
            invitation_text = template.format(**mapping)
        except Exception as e:
            # If template formatting fails for any reason, log and use a simple
            # replace fallback: replace known placeholders manually.
            print(f"Warning: formatting template for attendee #{i} failed with: {e}. Falling back to manual replacement.")
            invitation_text = template
            for k, v in mapping.items():
                invitation_text = invitation_text.replace('{' + k + '}', v)

        filename = f"output_{i}.txt"

        # If file exists, we overwrite it but notify the user
        if os.path.exists(filename):
            print(f"Note: {filename} already exists and will be overwritten.")

        try:
            with open(filename, 'w', encoding='utf-8') as out:
                out.write(invitation_text)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
            # continue to next attendee instead of terminating
            continue

    print(f"Generated {len(attendees)} invitation file(s).")


# If run as a script, demonstrate usage with the example data
if __name__ == '__main__':
    example_template = (
        "Hello {name},\n\n"
        "You are invited to the {event_title} on {event_date} at {event_location}.\n\n"
        "We look forward to your presence.\n\n"
        "Best regards,\n"
        "Event Team\n"
    )

    example_attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    generate_invitations(example_template, example_attendees)
