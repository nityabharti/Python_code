from random import randint
def pick_random_word():
    word_list=["hello","nitu","rain","animal","rat","egg","ear","train","summer","winter","sunday","march","cat","water","tea","tomato","peak","dibu","january","sohan"]
    selected_index=randint(0,len(word_list))
    return word_list[selected_index]

print(pick_random_word())   