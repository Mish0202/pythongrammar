def BeNegative(sentence):
    vBforms = ["am", "is", "are", "ARE", "IS", "AM", "WAS", "WERE", "was", "were"]
    negation = "NO" #because in front of a noun phrase
    #sentence = input("Please enter a sentence with THERE IS/ARE:")
    sentence_list = sentence.split()
    #new_sentence = []
    #final_sentence = []
    for word in sentence_list:
        if word in vBforms:
            idx = sentence_list.index(word)
            sentence_list.insert(idx + 1, negation)
            #print(i)
            #print(new_sentence)
        #if word not in vBforms:
            #final_sentence.append(word)
            #print(final_sentence)
    #return sentence_list
    negative_string = " ".join(sentence_list)
    print(negative_string)
    return negative_string

sentence = input("Please enter a sentence with THERE IS/ARE:")
BeNegative(sentence)

#string = "THERE IS SNOW OUTSIDE."
#print(BeNegative(string))
