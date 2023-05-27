def make_chocolate(small, big, goal):
    # 计算可以用 big bars 的数量
    big_bars_needed = goal // 5
    if big_bars_needed <= big:
        # 如果 big bars 的数量足够，用 big bars 填满目标重量
        goal -= big_bars_needed * 5
    else:
        # 否则用所有 big bars 填满，剩余部分由 small bars 填补
        goal -= big * 5
    
    # 计算剩余所需的 small bars 数量
    if goal <= small:
        return goal
    else:
        return -1
