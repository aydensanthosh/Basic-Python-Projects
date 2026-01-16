with open("story.txt","r") as f:
    story=f.read()
    
words=[]
answerkeypair={}
start_of_word=-1
target_start="{"
target_end="}"
for i,char in enumerate(story):
    if char==target_start:
        start_of_word=i

    if char==target_end and start_of_word!=-1:
        word=story[start_of_word:i+1]
        words.append(word)
        start_of_word=-1
print(words)
for i in words:
    answer=input(f"Enter a {i} word:")
    answerkeypair[i]=answer
print(answerkeypair)
for word in words:
    story=story.replace(word,answerkeypair[word])
print("Here is your story:")
print(story)
print(dir(story))