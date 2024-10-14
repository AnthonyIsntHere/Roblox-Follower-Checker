import requests
import os
import json

os.system("title Anthony's Follower Checker")

os.system("cls")
os.system("color")

while True:
    UserId = input("\x1b[35;49m[+] \x1b[31;49m{$int64} User Id: \x1b[32;49m")
    
    if UserId.isdigit():
        break
    else:
        print("\x1b[31;49m[+] \x1b[33;49minput is not int64. please try again")

FirstPageCount = 0
FriendApi = f"https://friends.roblox.com/v1/users/{UserId}/followers"
UserApi = f"https://users.roblox.com/v1/users/{UserId}"
Parameters = {
    "limit": "100",
    "cursor": "",
    "sortOrder": "Asc"
}

Response = requests.get(FriendApi, params=Parameters)
body = Response.json()
Data = body["data"]
NextPageCursor = body["nextPageCursor"]
for x in Data:
    FirstPageCount += 1

FollowCounter = 0

User_Response = requests.get(UserApi)
User_body = User_Response.json()
CurrentUsername = User_body["name"]

print(f"\x1b[35;49m[+] \x1b[32;49mChecking followers for the user: \x1b[35;49m{CurrentUsername}")

def CheckFriends():
    global NextPageCursor
    global FollowCounter
    
    if NextPageCursor:
        Parameters = {
            "limit": "100",
            "cursor": f"{NextPageCursor}",
            "sortOrder": "Asc"
        }
    else:
        return False

    r = requests.get(FriendApi, params=Parameters)
    body = r.json()
    NextPageCursor = body["nextPageCursor"]
    Data = body["data"]
    for x in Data:
        UserInfo = {
            "name": x["name"],
            "displayName": x["displayName"],
            "id": x["id"],
            "isBanned": x["isBanned"],
            "hasVerifiedBadge": x["hasVerifiedBadge"],
        }
        with open(f"{CurrentUsername}.txt", "a") as file:
            file.write(json.dumps(UserInfo) + "\n")
        FollowCounter += 1
    print(f"\x1b[35;49m[+] \x1b[32;49m{FollowCounter}")

while True:
    if CheckFriends() == False:
        break

FollowCounter += FirstPageCount

os.system("cls")
print("\x1b[35;49m[+] \x1b[35;49mFinished counting!")
print(f"\x1b[35;49m[+] \x1b[36;49m{CurrentUsername} \x1b[32;49mhas \x1b[35;49m{FollowCounter} \x1b[32;49mfollowers.")
os.system("pause")
