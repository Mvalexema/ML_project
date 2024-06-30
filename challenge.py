# 1. Add a prefix to a word

def add_prefix_un(word):
    new_word = 'un' + word
    return (new_word)

print(add_prefix_un("happy"))

# 2. Add prefixes to word groups
new_vocab_words = []

def make_word_groups(vocab_words):
    prefix=vocab_words[0]
    new_vocab_words.append(prefix)
    for i in range(1,len(vocab_words)):
        new_word = prefix + vocab_words[i]
        new_vocab_words.append(new_word)
    return new_vocab_words


print('::'.join(make_word_groups(['en','close','joy','lighten']) ))



# 3. Removal a suffix from a word

def remove_suffix_ness(word):
      
    new_word = word[:-4]
    # print(new_word)
    if new_word[-1] == 'i':
        word_ness = new_word[:-1]+'y'
        print(word_ness)
    else:
        print(new_word)


word = "heaviness"
remove_suffix_ness(word)


# 4. Extract and transform a word

def adjective_to_verb(sentence: str,index: int):
    sentence = sentence[:-1]  # Deteling the dot at the end
    list=sentence.split()
    adj=list[index]
    verb=adj+'en'
    
    return(verb)

sentence = 'I need to make that bright.'
index=-1

print(adjective_to_verb(sentence,index))