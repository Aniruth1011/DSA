from collections import defaultdict ,  deque 

class Twitter:

    def __init__(self):
        self.posts = defaultdict(deque)
        self.follows = defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].appendleft((self.timestamp ,  tweetId))
        self.timestamp+=1

    def getNewsFeed(self, userId: int) -> List[int]: 
        heap = []

        users = self.follows[userId].copy()
        users.add(userId)
        for user in users:
            if user in self.posts:
                for idx , (timestamp , tweetId) in enumerate(list(self.posts[user])[:10] ):
                    heapq.heappush(heap , (timestamp , tweetId))
        
        top_10 = heapq.nlargest(10 , heap)
        res = []
        for ( timestamp , tweetId ) in top_10:
            res.append(tweetId)
        return res 

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId!=followeeId:
            self.follows[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)