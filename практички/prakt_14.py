#Акулов Артём, вариант №4, практичка № 14
import re


input_file_name = "input.txt"
output_file_name = "output.txt"

with open(input_file_name, "r", encoding="utf-8") as file:
    text = file.read()


sentences = re.split(r'(?<=[.!?])\s*', text)


def remove_repeated_words(sentence):
    words = sentence.split()  
    cleaned_words = []  
    previous_word = None  
    for word in words:
        if word != previous_word: 
            cleaned_words.append(word)
            previous_word = word
    return ' '.join(cleaned_words)  


cleaned_sentences = [remove_repeated_words(sentence) for sentence in sentences]


cleaned_text = ' '.join(cleaned_sentences).strip()


with open(output_file_name, "w", encoding="utf-8") as file:
    file.write(cleaned_text)

print("Отредактированный текст успешно записан в файл:", output_file_name)