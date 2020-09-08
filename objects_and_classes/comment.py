class Comment:
    def __init__(self, username, content, likes = 0):
        self.username = username
        self.content = content
        self.likes = likes

comment_input = Comment("user", "10", "5")
print(comment_input.username)
print(comment_input.content)
print(comment_input.likes)