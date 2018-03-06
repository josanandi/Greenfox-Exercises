"""Exercise 1"""
def avg_of_odds(numbers):
    total=0
    count=0
    for number in numbers:
        if number%2!=0:
            total+=number
            count+=1
    return float(total/count)



"""Exercise 2"""

def text_encode(text):
    alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']
    new_text=[]
    for letter in text:
        if letter in alphabet:
            counter=text.count(letter)
            break

    for letter in text:
        for index, item in enumerate(alphabet):
            if letter==item:
                new_index=index+counter
                if new_index>=26:
                    new_index-=26
                new_text.append(alphabet[new_index])
                break
        else:
            new_text.append(letter)

    return ("".join(new_text))


""" Exercise 3 """
