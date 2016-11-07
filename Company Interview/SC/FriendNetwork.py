class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.friends = []

    def add_friend(self, user_obj):
        self.friends.append(user_obj)

    def get_friend_count(self, level_num):
        if level_num == 0:
        	return 0

        friend_count_in_level = 0
        level = 1
        friends = [self]
        while level <= level_num:
            level_friends = []
            friend_count_in_level = 0
            for friend in friends:
                level_friends.extend(friend.friends)
                friend_count_in_level += len(friend.friends)
            friends = level_friends
            level += 1
        return friend_count_in_level
