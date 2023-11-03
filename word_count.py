#This is a program to find number of occurrences of the word. 

def count_words(file_name):
    word_count = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    word = word.strip('.,!?()[]{}"\'').lower()
                    if word:
                        if word in word_count:
                            word_count[word] += 1
                        else:
                            word_count[word] = 1
        return word_count

    except FileNotFoundError:
        print(f"File is not found with given: {file_name}")
    except Exception as e:
        print(f"You occurred an error: {e}")
    
if __name__=="__main__":
    file_name = "/Users/pavankumar/Documents/Programming/COB/sample.txt"
    word_count = count_words(file_name)
    if word_count:
        for word, count in sorted(word_count.items()):
            print(f"{word}: {count}")
