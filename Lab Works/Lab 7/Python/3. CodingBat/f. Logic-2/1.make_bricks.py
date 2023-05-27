def make_bricks(small, big, goal):
    if big*5 == goal:
        return True
    elif big*5 > goal:
        return goal % 5 <= small
    else:
        max_big = min(goal//5, big)
        remaining_length = goal - max_big*5
        return remaining_length <= small
