import string

file_name = 'oxford.txt'
with open(file_name, 'r') as f:
  for line in f:
    #print(line)
    sentence = line.strip()
    sentence = sentence.strip(string.punctuation)
    print(sentence)
    sentence = sentence.lower()
    #print(sentence)
    word_list = sentence.strip()

    word_list = word_list.split(' ')

    for i in range(len(word_list)):
        word_list[i] = word_list[i].strip(string.punctuation)
    print(word_list)

    wordset = {}
    if word_list[i] in wordset:
        wordset[word_list[i]] += 1
    else:
        wordset[word_list[i]] = 0
    print(wordset)

#
# #word_set = {'the':567, 'a':675, 'them':474}
