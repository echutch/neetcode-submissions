class Twitter:

    def __init__(self):
        self.count = 0
        self.tweet_map = defaultdict(list)
        self.follow_map = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append((self.count, tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        build_feed = []

        # add self
        self.follow_map[userId].add(userId)

        # add followees
        for followeeId in self.follow_map[userId]:
            if followeeId in self.tweet_map:
                index = len(self.tweet_map[followeeId]) - 1
                count, id = self.tweet_map[followeeId][index]
                build_feed.append((-count, id, followeeId, index - 1))

        heapq.heapify(build_feed)

        res = []
        while build_feed and len(res) < 10:
            recent_count, recent_id, followeeId, index = heapq.heappop(build_feed)
            res.append(recent_id)

            if index >= 0:
                new_count, new_id = self.tweet_map[followeeId][index]
                heapq.heappush(build_feed, (-new_count, new_id, followeeId, index - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
        
