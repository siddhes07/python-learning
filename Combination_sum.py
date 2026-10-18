
def combinationSum(candidates, target):
    result = []

    def backtrack(start, current, total):
        if total == target:
            result.append(current[:])
            return

        if total > target:
            return

        for i in range(start, len(candidates)):
            current.append(candidates[i])

            backtrack(i, current, total + candidates[i])

            current.pop()

    backtrack(0, [], 0)
    return result


candidates = list(map(int, input("Enter candidates separated by spaces: ").split()))
target = int(input("Enter target: "))

print(combinationSum(candidates, target))
