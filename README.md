# Instagram Most Recent Followers and Following Lists

This project provides a simple way to fetch and display recent followers and following lists of an Instagram user. It leverages internal Instagram GraphQL queries to scrape data without using the official API. The project uses the references the "instagram-crawler" repository to facilitate this process.

## Prerequisites

- Python 3.x
- `followers.json` and `following.json` files containing the JSON data from Instagram (generated using provided GraphQL URLs).

## Setup

1. **Determine UserID:**
   - Navigate to the Instagram profile page of the target user.
   - View the page source (`Ctrl + U` or right-click and select "View page source").
   - Search for `profilePage_` and copy the number immediately following it. This is the user ID.

2. **Generate JSON Data:**
   - Use the provided GraphQL URLs to fetch follower and following data:
     - Followers URL: `https://www.instagram.com/graphql/query/?query_hash=c76146de99bb02f6415203be841dd25a&variables={"id":"<UserID>","first":50}`
     - Following URL: `https://www.instagram.com/graphql/query/?query_hash=d04b0a864b4b54837c0d870b0e77e076&variables={"id":"<UserID>","first":50}`
   - Replace `<UserID>` in the URLs with the actual user ID.
   - Paste these URLs into your browser to obtain the JSON data.
   - Save the data from these URLs into `followers.json` and `following.json` files, respectively.

3. **Run the Script:** Run the `main.py` script to display the recent followers and following lists.
