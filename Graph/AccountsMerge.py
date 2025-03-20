

"""
Merging the accounts using the disjoint set
Mapping each mail to same person if another list is having the same mail, that mail should also point to original person. 
where we will update the parent rest all things will be same as we do in disjoint set.
"""


class AccountsMerge:
    def __init__(self, accounts):
        self.accounts = accounts
        self.mail_dict = {}        
        self.parent = [i for i in range(len(self.accounts))]
        self.merged_accounts = [[] for i in range(len(self.accounts))]
    
    def find_parent(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]

        
    def accounts_merge(self):
        for i in range(len(self.accounts)):
            for j in range(len(self.accounts[i])):
                if j == 0:
                    self.merged_accounts[i].append(self.accounts[i][j])
                else:
                    if self.accounts[i][j] not in self.mail_dict.keys():
                        self.mail_dict[self.accounts[i][j]] = i
                    else:
                        self.parent[i] = self.mail_dict[self.accounts[i][j]]

        for k, v in self.mail_dict.items():
            parent = self.find_parent(v)
            self.merged_accounts[parent].append(k)
        
        for account in self.merged_accounts.copy():
            if len(account) == 1:
                self.merged_accounts.remove(account)
        
        result = []
        for account in self.merged_accounts:
            temp = sorted(account[1:])
            temp.insert(0, account[0])
            result.append(temp)
        return result


def test_set1_account_merge():
    Accounts = [
        ["John", "j2@com", "j1@com", "j8@com"], 
        ["John","j4@com"],
        ["Raj", "r1@com","r2@com"],
        ["John", "j1@com", "j0@com"],
        ["Raj","r2@com", "r3@com"],
        ["Mary", "m1@com"]
    ]

    account_merge = AccountsMerge(Accounts)
    account_merge_result = account_merge.accounts_merge()
    for account in account_merge_result:
        print(account)


test_set1_account_merge()







