#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    """Fetch posts and print the status code + titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Print status code
    print(f"Status Code: {response.status_code}")

    # Process only if successful
    if response.status_code == 200:
        posts = response.json()

        # Print each title
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Fetch posts, structure data, and save to posts.csv."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts_json = response.json()

        # Create list of dictionaries with selected fields
        formatted_posts = [
            {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            for post in posts_json
        ]

        # Write to CSV
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(formatted_posts)
