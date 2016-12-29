## 3. Optional Arguments ##

# Default code
def tokenize(text_string, special_characters, clean=False):
    if clean == True:
        cleaned_story = clean_text(text_string, special_characters)
        story_tokens = cleaned_story.split(" ")
    else:
        story_tokens = text_string.split(" ")
    return(story_tokens)
clean_chars = [",", ".", "'", ";", "\n"]
tokenized_story = []
tokenized_vocabulary = []
misspelled_words = []
tokenized_story = tokenize(story_string, clean_chars, clean=True)
tokenized_vocabulary = tokenize(vocabulary, clean_chars, clean=False)
for item in tokenized_story:
    if item not in tokenized_vocabulary:
        misspelled_words.append(item)

## 5. Practice: Creating a More Compact Spell Checker ##

def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for string in special_characters:
        cleaned_string = cleaned_string.replace(string, "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)

def tokenize(text_string, special_characters, clean=False):
    cleaned_text = text_string
    if clean:
        cleaned_text = clean_text(text_string, special_characters)
    tokens = cleaned_text.split(" ")
    return(tokens)

def spell_check(vocabulary_file,text_file,special_characters=[",",".","'",";","\n"]):
    misspelled_words = []
    voca = open(vocabulary_file).read()
    txt = open(text_file).read()
    tokenized_vocabulary = tokenize(voca,special_characters,clean=False)
    tokenized_text = tokenize(txt,special_characters,clean=True)
    for item in tokenized_text:
        if item not in tokenized_vocabulary and item != '':
            misspelled_words.append(item)
    return(misspelled_words)
    
final_misspelled_words = []
final_misspelled_words = spell_check('dictionary.txt','story.txt')
print(final_misspelled_words)

## 7. Syntax Errors ##

def spell_check(vocabulary_file, text_file, special_characters=[",",".","'",";","\n"]):
    misspelled_words = []
    vocabulary = open(vocabulary_file).read()
    text = open(text_file.read()
    
    tokenized_vocabulary = tokenize(vocabulary, special_characters= special_characters,clean = False)
    tokenized_text = tokenize(text, special_characters, True)
    
    for ts in tokenized_text:
        if ts not in tokenized_vocabulary and ts != '':
            misspelled_words.append(ts)
    return(misspelled_words)

final_misspelled_words = spell_check(vocabulary_file="dictionary.txt", text_file="story.txt")
print(final_misspelled_words)

## 9. TypeError and ValueError ##

forty_two = 42
forty_two + float("42")

str("guardians")

## 11. Traceback ##

def spell_check(vocabulary_file, text_file, special_characters=[",",".","'",";","\n"]):
    misspelled_words = []
    vocabulary = open(vocabulary_file).read()
    # Add ending parentheses.
    text = open(text_file).read()
    
    # Fix indentation.
    tokenized_vocabulary = tokenize(vocabulary, special_characters)
    tokenized_text = tokenize(text, special_characters, True)
    
    for ts in tokenized_text:
        if ts not in tokenized_vocabulary and ts != '':
            misspelled_words.append(ts)
    return(misspelled_words)

final_misspelled_words = spell_check(vocabulary_file="dictionary.txt", text_file="story.txt")
print(final_misspelled_words)