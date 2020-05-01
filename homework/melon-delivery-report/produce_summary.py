def melon_count(day_num,path):
    print(f"Day {day_num}")
    file=open(path)

    for line in file:
        line=line.rstrip()
        words= line.split("|")

        melon = words[0]
        count = words[1]
        amount = words[2]

        print("Delivered {} {}s for total of ${}".format(
        count, melon, amount))

    file.close()
melon_count(1, "um-deliveries-20140519.txt")
melon_count(2, "um-deliveries-20140520.txt")
melon_count(3, "um-deliveries-20140521.txt")

# the_file = open("um-deliveries-20140519.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


# print("Day 2")
# the_file = open("um-deliveries-20140520.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-20140521.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()
