class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        map_email = defaultdict(list) # map email -> account id

        for acc_id, account in enumerate(accounts):
            name = account[0]

            for j in range(1, len(account)):
                email = account[j]
                map_email[email].append(acc_id)
        
        res = []
        seen = set()

        for email in map_email:
            if email not in seen:
                queue = deque()
                queue.append(email)
                seen.add(email)

                acc_id = map_email[email][0]
                account = [accounts[acc_id][0]]
                
                while queue:
                    curr_email = queue.popleft()
                    account.append(curr_email)

                    for idx in map_email[curr_email]:
                        email_list = accounts[idx]

                        for i in range(1, len(email_list)):
                            next_email = email_list[i]

                            if next_email not in seen:
                                seen.add(next_email)
                                queue.append(next_email)
                account.sort()
                res.append(account)
        return res




        