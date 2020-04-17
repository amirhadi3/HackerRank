def countingValleys(n, s):
    hiker_level = 0
    sea_level = 0
    valley_counts = 0
    record_first_step = True

    for item in s:
        if record_first_step:
            first_step = item

        if item == 'D':
            hiker_level -= 1
            record_first_step = False

        elif item == 'U':
            hiker_level += 1
            record_first_step = False

        if hiker_level == sea_level:

            record_first_step = True

            if (first_step == 'D') and (item == 'U'):
                valley_counts += 1

    return valley_counts


if __name__ == '__main__':
    n = 8
    s = ['U', 'D', 'D', 'D', 'U', 'D', 'U', 'U']

    result = countingValleys(n, s)

    print(result)
