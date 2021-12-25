from instapy import InstaPy,smart_run
def automate(session,blacklist,tags,amount:int=50):
    with smart_run(session):
        session.set_relationship_bounds(enabled=True,delimit_by_numbers=True,max_followers=500,min_followers=50,min_following=30)
        session.set_do_follow(True,percentage=100)
        session.set_dont_like(blacklist)
        session.like_by_tags(tags,amount=amount)
def main():
    username = input("Username:  ")
    password = input("Password:  ")
    amount = int(input("People to follow Per Tag:  "))
    session = InstaPy(username=username,password=password,headless_browser=False)
    blacklist = []
    tags = []
    for bad in open("blacklist.txt","r").read().splitlines():
        blacklist.append(bad)
    for follow in open("tags.txt","r").read().splitlines():
        tags.append(follow)
    automate(session,blacklist,tags,amount)
if __name__ == "__main__":
    main()