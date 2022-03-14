from nltk.tokenize import regexp_tokenize
from collections import Counter
import random


def token_division_to_list(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        list_of_tokens = regexp_tokenize(file.read(), r'[\S]+')
        # Сейчас он должен разбивать на токены по одному слову
        file.close()
    return list_of_tokens


def bigram_division_to_list(list_of_tokens):
    list_of_bigrams = []
    for i in range(0, len(list_of_tokens) - 2):
        list_of_bigrams.append(list_of_tokens[i] + ' ' + list_of_tokens[i + 1])
    # Сейчас он должен разбивать на токены по два слова
    return list_of_bigrams


def trigram_division_to_list(list_of_tokens):
    list_of_trigrams = []
    for i in range(0, len(list_of_tokens) - 2):
        list_of_trigrams.append(list_of_tokens[i] + ' ' + list_of_tokens[i + 1] + ' ' +
                                list_of_tokens[i+2])
        # Сейчас он должен разбивать на токены по три слова
    return list_of_trigrams


# def corpus_statistics(list_of_smth):
#     # print('Corpus statistics')
#     # print('All tokens:', len(list_of_smth))
#     # print('Unique tokens:', len(set(list_of_smth)))
#     print('Number of bigrams:', len(list_of_smth))
#     print()


# def creation_of_prob_tail_list(head, list_of_bigrams):
#     list_of_tails = [bigram.split()[1] for bigram in list_of_bigrams
#                      if bigram.split()[0] == head]
#     if not list_of_tails:
#         assert KeyError
#     prob_list_of_tails = Counter(list_of_tails).most_common()
#     return prob_list_of_tails


def creation_of_prob_tail_list_for_trigrams(head, list_of_trigrams):
    list_of_tails = []
    for trigram in list_of_trigrams:
        temp = trigram.split()
        if temp[0] + ' ' + temp[1] == head:
            list_of_tails.append(temp[2])
    # # print(list_of_tails)
    # if not list_of_tails:
    #     assert KeyError
    prob_list_of_tails = Counter(list_of_tails).most_common()
    return prob_list_of_tails


def creation_of_tail_or_prob_list(prob_list_of_tails, n=0):  # by default list of tails (if n=1: probs)will be created
    out_list = []
    for pair in prob_list_of_tails:
        # print(pair)
        out_list.append(pair[n])
    return out_list


# def word_selection(head, bigram_list):
#     temp = creation_of_prob_tail_list(head, bigram_list)
#     tail_list = creation_of_tail_or_prob_list(temp, 0)
#     prob_list = creation_of_tail_or_prob_list(temp, 1)
#     tail = random.choices(population=tail_list, weights=prob_list)
#     return tail


# def main_2_stage():
#     file_name = input()
#     list_of_bigrams = bigram_division_to_list(file_name)
#     # print(list_of_bigrams[-1])
#     # corpus_statistics(list_of_bigrams)
#     while True:
#         input_string = input()
#         if input_string == 'exit':
#             break
#         try:
#             number = int(input_string)
#             try:
#                 output = list_of_bigrams[number].split()
#                 print(f'Head: {output[0]} Tail: {output[1]}')
#             except IndexError:
#                 print('Index Error. Please input an integer that is in the range of the corpus.')
#         except ValueError:
#
#             print('Type Error. Please input an integer.')


# def main_3_stage():
#     file_name = input()
#     list_of_bigrams = bigram_division_to_list(file_name)
#     while True:
#         input_string = input()
#         if input_string == 'exit':
#             break
#         try:
#             list_of_input = [bigram.split()[1] for bigram in list_of_bigrams if bigram.split()[0] == input_string]
#             if not list_of_input:
#                 assert KeyError
#             counter_list = Counter(list_of_input).most_common()
#             print('Head:', input_string)
#             for pair in counter_list:
#                 print(f'Tail: {pair[0]} Count: {pair[1]}')
#         except KeyError:
#             print('Key Error. The requested word is not in the model. Please input another word.')
#
#
# def main_4_stage():
#     file_name = input()
#     token_list = token_division_to_list(file_name)
#     bigram_list = bigram_division_to_list(token_list)
#     head_word = random.choice(token_list)
#     output_list = [head_word]
#     for i in range(100):
#         tail = word_selection(head_word, bigram_list)[0]
#         output_list.append(tail)
#         head_word = tail
#     for i in range(10):
#         output = output_list[i * 10: (i + 1) * 10]
#         print(*output)


def tail_selection(head, trigram_list):
    temp = creation_of_prob_tail_list_for_trigrams(head, trigram_list)
    # print(temp)
    tail_list = creation_of_tail_or_prob_list(temp, 0)
    prob_list = creation_of_tail_or_prob_list(temp, 1)
    tail = random.choices(tail_list, weights=prob_list)
    return tail[0]


def only_capital_head(list_of_trigrams):
    list_of_head = []
    for trigram in list_of_trigrams:
        temp = trigram.split()
        # print(temp[0])
        if temp[0][0].isupper() and temp[0][-1] not in ['!', '?', '.']:
            # print(temp)
            list_of_head.append(temp[0] + ' ' + temp[1])
    return list_of_head


# def only_capital_letters(file_name):
#     with open(file_name, 'r', encoding='utf-8') as file:
#         list_of_tokens = regexp_tokenize(file.read(), r'[A-Z][a-z]+[^.!?\s]')
#         # Сейчас он должен разбивать на токены по одному слову, все слова с большой буквы
#         file.close()
#     return list_of_tokens


# def main_5_stage():
#     file_name = input()
#     token_list = token_division_to_list(file_name)
#     bigram_list = bigram_division_to_list(token_list)
#     capital_token_list = only_capital_letters(file_name)
#     head_word = random.choice(capital_token_list)
#     output_list = [head_word]
#     for i in range(10):
#         while True:
#             reserved_head = head_word
#             tail = word_selection(head_word, bigram_list)[0]
#             if not output_list:
#                 flag = True
#                 while flag:
#                     if tail[-1] in ['.', '?', '!']:
#                         tail = word_selection(reserved_head, bigram_list)[0]
#                     else:
#                         flag = False
#             output_list.append(tail)
#             head_word = tail
#             last_char = head_word[-1]
#             if len(output_list) >= 5 and (last_char in ['.', '?', '!']):
#                 print(*output_list)
#                 output_list = []
#                 break


def main_6_stage():
    file_name = input()
    token_list = token_division_to_list(file_name)
    all_head_list = bigram_division_to_list(token_list)
    trigram_list = trigram_division_to_list(token_list)
    # print(trigram_list)
    capital_head_list = only_capital_head(all_head_list)
    head = random.choice(capital_head_list)
    output_list = head.split()
    # print(head)
    for i in range(10):
        while True:
            reserved_head = head
            tail = tail_selection(head, trigram_list)
            # print(tail)
            if not output_list:
                flag = True
                while flag:
                    if tail[-1] in ['.', '?', '!']:
                        tail = tail_selection(reserved_head, trigram_list)
                    else:
                        flag = False
            output_list.append(tail)
            head = head.split()[1] + ' ' + tail
            last_char = head[-1]
            # print(output_list)
            # print(head)
            if len(output_list) >= 5 and last_char in ['.', '?', '!']:
                # print(output_list)
                print(' '.join(output_list))
                output_list = []
                break


if __name__ == '__main__':
    main_6_stage()
