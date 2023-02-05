def word_chain(input_list, word=None):
    chains = []
    for w in input_list:
        temp = input_list.copy()
        if not word:
            get_chains(chains, temp, w)
        else:
            if w.startswith(word[-1]):
                get_chains(chains, temp, w)
    if len(chains) > 0:
        return max(chains, key=len)
    return []


def get_chains(chains, word_list, word):
    word_list.remove(word)
    chain = word_chain(word_list, word)
    list = [word]
    if len(chain) > 0:
        list.extend(chain)
    chains.append(list)


words = [
    'why',
    'new',
    'neural',
    'moon',
    'luck',
    'know',
    'yacht',
    'false',
    'true',
]

print(len(word_chain(words)))
print(' - '.join(word_chain(words)))
