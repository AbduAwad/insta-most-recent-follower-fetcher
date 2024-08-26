# "instagram-crawler" uses internal Instagram queries (identified by query_hash values) to scrape follower, 
# following, and story viewer data directly from Instagram, without using the official API.
# Github REPO: https://github.com/yc5/instagram-crawler

# Step 1: Determine UserID:
# view-source:https://www.instagram.com/<username>/
# crtl+f: "profilePage_" and copy the number after it

USERNAME = '<username>'

# URL for followers.json: user your own id in the {id} field
followers_url = 'https://www.instagram.com/graphql/query/?query_hash=c76146de99bb02f6415203be841dd25a&variables={"id":"<UserID>","first":50}'

# URL for following.json:
following_url = 'https://www.instagram.com/graphql/query/?query_hash=d04b0a864b4b54837c0d870b0e77e076&variables={"id":"<UserID>","first":50}'


# STEP 2: 
# past the URL in the browser to get the json data
# copy the json data to followers.json and following.json files respectively.

import json 

def get_most_recent_followers() -> list:
    with open('followers.json', 'r', encoding='utf-8') as f:
        followers = json.load(f)
    
    followers_list = []

    print("--------------------------------- @" + USERNAME + " Most Recent Followers ---------------------------------")

    for follower in followers['data']['user']['edge_followed_by']['edges']:
        print(follower['node']['username'])

    return followers_list

def get_most_recent_following() -> list:
    with open('following.json', 'r', encoding='utf-8') as f:
        following = json.load(f)

    following_list = []
    print("--------------------------------- @" + USERNAME + ' Most Recent Following ---------------------------------')
    for follower in following['data']['user']['edge_follow']['edges']:
        following_list.append(follower['node']['username'])
        print(follower['node']['username'])
    
    return following_list

def main():
    get_most_recent_followers()
    get_most_recent_following()


if __name__ == '__main__':
    main()