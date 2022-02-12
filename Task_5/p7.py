# Method to find the maximum topics and the number of teams that know that many topics
def acmTeam(topic):
    list = []
    for i in range(len(topic)):
        for j in range((i + 1) , len(topic)):
            x = int(topic[i]) + int(topic[j])
            list.append(len(str(x)) - str(x).count("0"))
    return [max(list) , list.count(max(list))]

# Program Test
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

topic = []
for i in range(n):
    topic_item = input()
    topic.append(topic_item)

print(*acmTeam(topic))