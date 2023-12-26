def canCross(stones):
    target = stones[-1]
    stones_set = set(stones)
    memo = {}

    def dfs(pos, jump):
        if (pos, jump) in memo:
            return memo[(pos, jump)]

        if pos == target:
            memo[(pos, jump)] = True
            return True

        for next_jump in [jump - 1, jump, jump + 1]:
            if next_jump <= 0:
                continue

            next_pos = pos + next_jump
            if next_pos != pos and next_pos in stones_set:
                if dfs(next_pos, next_jump):
                    memo[(pos, jump)] = True
                    return True

        memo[(pos, jump)] = False
        return False

    return dfs(0, 0)

n = int(input())
stones = [int(x) for x in input().split()]
result = canCross(stones)
print(result)