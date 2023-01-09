import json
with open("following.json", "r") as following_file:
    following_data = json.load(following_file)
with open("followers.json", "r") as followers_file:
    followers_data = json.load(followers_file)
def parse(json_, str_):
    sets = set()
    for user in json_[str_]:
        sets.add(user["string_list_data"][0]["value"])
    return sets
not_following = parse(following_data, "relationships_following")-parse(followers_data, "relationships_followers")
for users in not_following:
    print(users)