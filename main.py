import json
def load_data(filename):
    with open(filename,"r")as f:
        data=json.load(f)
        return data
data=load_data("data.json")

def extract_users(data):
    for user in data["users"]:
        print(f"user with id {user["id"]} is {user["name"]} and is friends with {user["friends"]} and has interest in {user["liked_pages"]} ")

def extract_pages(data):
    for page in data["pages"]:
        print(f"id {page["id"]} stands for {page["name"]}")
extract_users(data)
extract_pages(data)