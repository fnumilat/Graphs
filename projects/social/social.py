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

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

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

        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i+1}")

        # Create friendships
        # Generate ALL possible friendships
        # Avoid duplicate friendships 
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                # user_id == user_id_2 cannot happen
                # if friendship between user_id and user_id_2 already exists
                #   dont add friendship between user_id_2 and user_id
                possible_friendships.append( (user_id, friend_id) )
            
        # Randomly select X friendships
        # the formula for X is  num_users * avg_friendships  // 2 
        # shuffle the array and pick X elements from the front of it
        random.shuffle(possible_friendships)
        num_friendships = num_users * avg_friendships // 2
        for i in range(0, num_friendships):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # Call the Queue method from the Queue class
        queue = Queue()

        # Add the user id to the queue
        queue.enqueue([user_id])

        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        # While the queue's lenght is not zero
        while queue.size() > 0:
            # Create a var called path to dequeue
            path = queue.dequeue()
            # Create a var called vertex to get the last 
             # node in the path
            vertex = path[-1]

            # Check and see if vertex isn't checked as visited
            if vertex is not visited:
                # and see if vertex is not the user id
                if vertex is not user_id:
                    # then set the visited vertex to path
                    visited[vertex] = path

                # Check for the neighbors of the vertex,
                # see if the neighbor is not checked as visited
                # then copy the path,
                # add the neighbor to the path
                # and add the path to the queue 
                for neighbor in self.friendships[vertex]:
                    if neighbor not in visited:
                        new_path = path.copy()
                        new_path.append(neighbor)
                        queue.enqueue(new_path)
                        

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    # sg.populate_graph(100, 10)
    print(f'Friendships:{sg.friendships}')
    connections = sg.get_all_social_paths(1)
    print(f'Connections: {connections}')

    ## Questions:

    # 1. To create 100 users with an average of 10 friends each, how many times would you need to call `add_friendship()`? Why?

    ## Answer:

    # 100 * 10 = 1000 // 2 = 500
    # It would be 500 times because each friendship is a pair


    # 2. If you create 1000 users with an average of 5 random friends each, what percentage of other users will be in a 
    # particular user's extended social network? What is the average degree of separation between a user and those in his/her 
    # extended network?
