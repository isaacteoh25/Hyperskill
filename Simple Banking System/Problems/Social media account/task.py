class Account:
    def __init__(self, media, username, n_followers):
        self.media = media
        self.username = username
        self.n_followers = n_followers
        print("Account")


# create the class here
class InstagramAccount(Account):
    def __init__(self, username, n_followers, n_following):
        # super().__init__(n_following)
        super().__init__( "Instagram", username, n_followers)
        # self.media =
        self.n_following = n_following

# class InstagramAccount(Account):
#     def __init__(self, username, n_followers, n_following):
#         self.n_following = n_following
#         Account.__init__(self, 'Instagram', username, n_followers)