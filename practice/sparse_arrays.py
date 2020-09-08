def match_queries(arr_strings: list, arr_queries):
    count_queries_matches = []

    for index, query_word in enumerate(arr_queries):
        count_matches = arr_strings.count(query_word)
        count_queries_matches.insert(index, count_matches)

    return list(map(str, count_queries_matches))


size_of_strings = int(input())
all_strings = []

for _ in range(size_of_strings):
    string = input()
    all_strings.append(string)

size_of_queries = int(input())
all_queries = []

for _ in range(size_of_queries):
    query = input()
    all_queries.append(query)

print("\n".join(match_queries(all_strings, all_queries)))