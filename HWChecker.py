import difflib
import time

try:
    q = int(input("Instructions\n\tThe filenames should be the roll no of the student\n\tThe file format must be text or with extension .txt \n\tThe program and all the files of students must be in same folder\n\t""Press an integer digit to continue!"))
except ValueError:
    print("Thank You!")
    time.sleep(2)
try:
    # no of students in the class
    n = int(input("Enter the Number of students in the class : "))
except ValueError:
    print("You must give in a integer value")
    time.sleep(2)
    exit()

try:
    # Percentage of similarity that can be tolerated
    p = int(input("Enter the percentage of similarity that can be tolerated : "))
except ValueError:
    print("You must give in a integer value")
    time.sleep(2)
    exit()

# array for storing roll no of people who not submitted the home work
nosubmission = []
# array for storing roll no of people who submitted the home work
submission = []
# array for keeping the count of keywords present in submitted file
kwords = []
# Function for adding keywords to be searched
keywords = []
# array for similar submissions
copy = []
# flag is used for checking whether keyword searching is added
flag = 0


# add keywords to array so that program searches them in the file and confirms whether student has written about it
def addkeywords():
    x = input("Enter the Keyword you want to add followed by Enter key : ")
    x.lower()  # converted to lower case for easy searching
    keywords.append(x)
    y = input("To add more press 1 \n To continue to Home work Checker press 0 : ")
    if y == str(1):
        addkeywords()


choice = input("Do you want to add keywords to be searched in the home work file \n To add press 1 else press 0 : ")
if choice == str(1):
    flag = 1
    addkeywords()
i = 1
while i <= n:
    file1 = str(i) + ".txt"
    try:
        f1 = open(file1, "r")
        if not (i in submission):
            submission.append(i)
        word1 = f1.read().lower()
        li = list(word1.split(" "))
        count = 0
        for c in range(len(keywords)):
            for d in range(len(li)):
                if keywords[c] == li[d]:
                    count += 1
                    break
        kwords.append(count)
        j = i + 1
        group = []
        while j <= n: # and j not in submission:
            file2 = str(j) + ".txt"
            try:
                f2 = open(file2, "r")
                # if not (j in submission):
                    # submission.append(j)
                word2 = f2.read().lower()
                m = difflib.SequenceMatcher(None, word1, word2)
                if (m.ratio()) * 100 > p:
                    group.append(j)
                f2.close()
            except FileNotFoundError:
                if not (j in nosubmission):
                    nosubmission.append(j)
            j += 1
        group.insert(0, i)
        copy.append(group)
        f1.close()
    except FileNotFoundError:
        if not (i in nosubmission):
            nosubmission.append(i)
    i += 1

f1 = open("report.txt","w")
# The output portion
print("\n\nSubmissions")
f1.write("\n\t\t\tReport\n\nSubmissions\n")
for i in range(len(submission)):
    print(submission[i], end=" ")
    f1.write(str(submission[i]) + " ")
print("\n")
if flag == 1:
    print("\n\nKeywords Search")
    f1.write("\n\nKeywords Search\n")
    print("\tRoll No\tFound keywords\tTotal keywords\tPercentage")
    f1.write("\tRoll No\tFound keywords\tTotal keywords\tPercentage\n")
    for i in range(len(submission)):
        print("\t\t" + str(i+1) + "\t\t\t" + str(kwords[i]) + "\t\t\t" + str(len(keywords)) + "\t\t\t" + str((kwords[i] / len(keywords)) * 100))
        data = "\t\t" + str(i+1) + "\t\t\t" + str(kwords[i]) + "\t\t\t" + str(len(keywords)) + "\t\t\t" + str((kwords[i] / len(keywords)) * 100) + " \n"
        f1.write(data)
    print("\n")
    f1.write("\n")
print("\n\nSimilar submissions")
f1.write("\n\nSimilar submissions\n")
for i in range(len(copy)):
    if not(len(copy[i]) == 1):
        for j in range(len(copy[i])):
            print(copy[i][j], end=" ")
            f1.write(str(copy[i][j]) + " ")
        print("\n")
        f1.write("\n")
print("\n\nNot submitted")
f1.write("\n\nNot submitted\n")
for i in range(len(nosubmission)):
    print(nosubmission[i], end=" ")
    f1.write(str(nosubmission[i]) + " ")
print("\n\n")
f1.write("\n\n")
f1.close()