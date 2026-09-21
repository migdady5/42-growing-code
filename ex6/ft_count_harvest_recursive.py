def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def helper(current, end):
        if current > end:
            print("Harvest time!")
            return
        print("Day", current)
        helper(current + 1, end)

    helper(1, days)
