def strip_punc(string):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for x in string:
        if x in punctuations:
            string = string.replace(x, "")
    return string

def word_count(string):
    word_count = {}
    words = string.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

if __name__ == '__main__':
    print(word_count(strip_punc(input("Enter a string: "))))