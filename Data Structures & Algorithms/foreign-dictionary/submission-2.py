class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(list)
        indeg = defaultdict(int)

        for w in words:
            for c in w:
                indeg[c] = 0


        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            minLen = min(len(w1), len(w2))
            # check prefix
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    # if w2[j] not in adj[w1[j]]:
                    adj[w1[j]].append(w2[j])
                    indeg[w2[j]] += 1
                    break

        queue = deque()
        for c in indeg:
            if indeg[c] == 0:
                queue.append(c)
        res = []
        while queue:
            curr = queue.popleft()
            res.append(curr)

            for next in adj[curr]:
                indeg[next] -= 1
                if indeg[next] == 0:
                    queue.append(next)
        print(res, indeg)
        if len(res) == len(indeg):
            return "".join(res)
        else:
            return ""
        