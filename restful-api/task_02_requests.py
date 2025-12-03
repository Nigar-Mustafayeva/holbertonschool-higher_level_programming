import requests
import csv

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts_json = response.json()
        
        # Step 4: Prepare data for CSV
        posts_data = []
        for post in posts_json:
            posts_data.append({
                "id": post['id'],
                "title": post['title'],
                "body": post['body']
            })
        
        # Step 5: Write to CSV
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts_data)
        
        print("Data saved to posts.csv successfully!")
    else:
        print(f"Failed to fetch posts. Status code: {response.status_code}")

# Run the function
fetch_and_save_posts()
