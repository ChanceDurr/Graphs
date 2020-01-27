import random
from util import Queue
class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        self.friendships_called = 0

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            # print("WARNING: You cannot be friends with yourself")
            pass
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            # print("WARNING: Friendship already exists")
            pass
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            self.friendships_called += 1

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Get names from txt files
        with open('first_names.txt', 'r') as f:
            first_names = f.read().split(', ')

        with open('last_names.txt', 'r') as f:
            last_names = f.read().split(', ')
        # Add users
        for i in range(num_users):
            name = f'{random.choice(first_names)} {random.choice(last_names)}'
            self.add_user(name)

        # Create friendships
        for user in self.users:
            for i in range(random.randint(1, avg_friendships)):
                self.add_friendship(user, random.randint(1, len(self.users)))



    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        if user_id not in self.users:
            print('WARNING: User id does not exist')
            return
        
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        queue = Queue()

        queue.enqueue([user_id])

        while queue.size() > 0:

            path = queue.dequeue()

            user = path[-1]

            if user not in visited:

                visited[user] = path

                for next_vert in self.friendships[user]:

                    new_path = list(path)
                    new_path.append(next_vert)
                    queue.enqueue(new_path)
        
        return visited


if __name__ == '__main__':
    print('Creating social graph with 10 users with 2 friends avg \n')
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections, '\n')
    
    print('Creating social graph with 100 users with 10 friends avg \n')
    sg = SocialGraph()
    sg.populate_graph(100, 10)
    friends = 0
    for i in range(1, 100):
        friends += len(sg.friendships[i])

    print('Average Number of friends: ', friends / 100)
    print('Number of times add_friendship() was called', sg.friendships_called, '\n')
    
    print('Creating social graph with 1000 users with 5 friends avg \n')
    sg = SocialGraph()
    sg.populate_graph(1000, 5)

    total_of_ext = 0
    for i in sg.get_all_social_paths(random.randint(1, 1000)).items():
        if len(i[1]) > 2:
            total_of_ext += 1

    print("Percent of users in extend social group", total_of_ext / 1000)
    # for i in sg.users:
    #     print(sg.users[i].name)