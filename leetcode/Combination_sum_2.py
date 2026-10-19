
def combinationSum2(candidates, target):
    candidates.sort()
    result = []

    def backtrack(start, current, total):
        if total == target:
            result.append(current[:])
            return

        if total > target:
            return

        for i in range(start, len(candidates)):
            # Skip duplicate numbers at the same level
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            current.append(candidates[i])

            # Move to i + 1 because each number is used once
            backtrack(i + 1, current, total + candidates[i])

            current.pop()

    backtrack(0, [], 0)
    return result


candidates = list(map(int, input("Enter candidates separated by spaces: ").split()))
target = int(input("Enter target: "))

answer = combinationSum2(candidates, target)
print("Unique combinations:", answer)
