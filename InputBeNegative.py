def BeNegative(sentence):
    vBforms = ["am", "is", "are", "ARE", "IS", "AM", "WAS", "WERE", "was", "were"]
    negation = "NO" #because in front of a noun phrase
    sentence_list = sentence.split()
    
    for word in sentence_list:
        if word in vBforms:
            idx = sentence_list.index(word)
            sentence_list.insert(idx + 1, negation)
           
    negative_string = " ".join(sentence_list)
    print("Отрицательная форма:", negative_string)
    return negative_string

sentence = input("Напишите предложение с THERE IS/ARE:   ")
BeNegative(sentence)


