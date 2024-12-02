def get_input():
    with open("input") as raw:
        return [list(map(int, line.split("   "))) for line in raw.read().split("\n")]


def func_part_i(_input):
    n = len(_input)

    left_registry, right_registry = {}, {}
    for i in range(n):
        left, right = _input[i]

        left_registry[left] = left_registry.get(left, 0) + 1
        right_registry[right] = right_registry.get(right, 0) + 1

    left_ids = sorted(left_registry.keys())
    right_ids = sorted(right_registry.keys())

    tot = 0

    left = 0
    right = 0
    for i in range(n):
        tot += abs(
            left_ids[left]
            - right_ids[right]
        )

        left_registry[left_ids[left]] -= 1
        right_registry[right_ids[right]] -= 1

        if left_registry[left_ids[left]] == 0:
            left += 1

        if right_registry[right_ids[right]] == 0:
            right += 1

    return tot

# def func_part_i(_input):
#     n = len(_input)
#     left_registry, right_registry = {}, {}
#     for i in range(n):
#         left, right = _input[i]
#
#         left_registry[left] = left_registry.get(left, []) + [i]
#         right_registry[right] = right_registry.get(right, []) + [i]
#
#     left_ids = sorted(left_registry.keys())
#     right_ids = sorted(right_registry.keys())
#
#     print(left_registry)
#     print(right_registry)
#     print("-"*20)
#
#     tot = 0
#
#     left = 0
#     right = 0
#     for i in range(n):
#         tot += abs(
#             left_registry[left_ids[left]].pop(0)
#             - right_registry[right_ids[right]].pop(0)
#         )
#
#         if len(left_registry[left_ids[left]]) == 0:
#             left += 1
#
#         if len(right_registry[right_ids[right]]) == 0:
#             right += 1
#
#         print(left_registry)
#         print(right_registry)
#         print("-" * 20)
#
#     return tot


def func_part_ii(_input):
    n = len(_input)

    registry = {}
    existing = []
    for i in range(n):
        left, right = _input[i]

        existing.append(left)
        registry[right] = registry.get(right, 0) + 1

    tot = 0
    for identity in existing:
        tot += identity * registry.get(identity, 0)

    return tot


if __name__ == "__main__":
    data = get_input()
    print(f"{__file__.split('/')[-2]:-^22s}")
    print("Part I - Result: ", func_part_i(data))
    print("Part II - Result: ", func_part_ii(data))
