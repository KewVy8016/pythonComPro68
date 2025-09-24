import requests

# Make a GET request to a public API (GitHub API)
response = requests.get('https://api.github.com/users/octocat')

# Check if the request was successful
if response.status_code == 200:
    user_data = response.json()

    # Display some information from the response
    print(f"Username: {user_data['login']}")
    print(f"Name: {user_data['name']}")
    print(f"Bio: {user_data['bio']}")
    print(f"Public Repos: {user_data['public_repos']}")
    print(f"Followers: {user_data['followers']}")
    print(f"Following: {user_data['following']}")
else:
    print("Failed to retrieve data.")
