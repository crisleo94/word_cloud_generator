from ast import Not
from http.client import FOUND
import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import io
import sys
from collections import Counter
from itertools import chain

def calculate_frequencies(file_contents):
    result = count_words(file_contents)
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(dict(result[0]))
    return cloud.to_array()
  
def count_words(file_contents):
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "so", "in", "an", "as", "i", "me", "my", \
      "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
      "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
      "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
      "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    new_contents = []
    no_punctuation_contents = []
    result = []
    
    for content in file_contents:
      clean_value = content.replace("\n", " ")
      new_contents = clean_value.split(" ")
      for nc in new_contents:
        if nc.isalpha() and (nc != "" or nc != " "):
          no_punctuation_contents.append(nc.lower())
          
    for uw in uninteresting_words:
      result = remove_items(no_punctuation_contents, uw)
    
    return [Counter(chain.from_iterable(map(str.split, result))), result]
  
def remove_items(test_list, item):
  c = test_list.count(item)
  for i in range(c):
    test_list.remove(item)
  return test_list
  
f = open('input.txt', 'r', encoding='utf-8')
file_contents = f.readlines()
f.close()

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
