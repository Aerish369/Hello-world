def check_for_harry(post):
    return "Harry " in post

post = input("Enter your post: ")

if check_for_harry(post):
    print("This post is talking about Harry.")
else:
    print("This post is not talking about Harry.")