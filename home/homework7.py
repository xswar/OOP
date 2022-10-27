
def get_list() -> list:
    return list(range(0, 1_000, 2))


class Solution:

    def __init__(self):
        pass

    def find_target(self, lst, target):
        if target not in lst:
            return f'такого числа нет'
        l = 0
        r = len(lst) - 1
        m = (l + r) // 2
        while target != lst[m]:
            if target > lst[m]:
                l = m
            elif target < lst[m]:
                r = m
            m = (l + r) // 2
        return m


lst = get_list()
solution = Solution()
print(solution.find_target(lst, 100))










