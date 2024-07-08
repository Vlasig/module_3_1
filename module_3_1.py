calls = 0


def count_calls(call):
    global calls
    calls += call
    return calls


def string_info(string):
    k = [len(string), string.upper(), string.lower()]
    count_calls(1)
    return k


def is_contains(string, list_to_search):
    str_n = string.lower()
    list_n = []
    count_calls(1)
    for i in list_to_search:
        i = i.lower()
        list_n.append(i)
    return str_n in list_n

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
