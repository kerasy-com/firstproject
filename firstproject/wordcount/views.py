from django.shortcuts import render
import re

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    text = re.sub('[-=+,#/\?:^$.@*\"~&%!]', '', text)
    text = text.split()
    total_words = len(text)

    word_dictionary = {}
    for word in text:
        if word in word_dictionary:
            #increase
            word_dictionary[word] += 1
        else:
            #add to dictionary
            word_dictionary[word] = 1

    return render(request, 'result.html', {'full': text, 'total': total_words, "dictionary": word_dictionary.items()})