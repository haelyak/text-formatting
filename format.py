

def splitfile(filename):
    file = open(filename, 'r')
    words = file.read()
    wordList = words.split()
    return wordList

def format(filename, columns, k, value):
  # Input: the name of the input text file, a positive integer indicating        
  # the number of columns in the output, and a penalty value
  # Output: the optimal total penalty
    filename = splitfile(filename)

    DP = [0]*(len(filename)+1) # Create a 1D DP table with n+1 cells (where n is the number of words in the file)
    breadcrumbs = [0]*(len(filename)+1) # Create a similarily sized breadcrumb table

    for i in range(0, len(filename)+1):
        if i == 0: # if there are no words in the file, return zero
            DP[i] = 0 
            breadcrumbs[i] = 0
        else:
            lineLength = len(filename[i-1]) #Place the i-1 word on the line becuase of zero-indexing
            DP[i] = pow(columns - len(filename[i-1]), k) + DP[i-1] #Store the sum of the penalty for this word and the previous cell's value 
            breadcrumbs[i] = i-1 #The breadcrumb points to the previous cell 

            for j in range(i-1, 0, -1): #Loop through the rest of the words in the file
                lineLength += len(filename[j-1]) + 1 # we need +1 for the extra space between words
                if lineLength <= columns: # if there is space left on the line 
                    penalty = pow((columns - lineLength), k)
                    stayOnLine = penalty + DP[j-1] #Calculate the penalty for adding this word onto the same line as the previous one
                    DP[i] = min(DP[i], stayOnLine) #If stayonLine is better, update the DP cell
                    if DP[i] == stayOnLine:
                        breadcrumbs[i] = j-1 #If stayoneLine is better, also update the breadcrumbs
    # print(DP)
    # print(breadcrumbs)
    # print(len(filename))
    if value == True:
        text = ""
        i = len(breadcrumbs)-1 #Start at the back of the breadcrumbs table
        while i > 0:
            for j in range(i, breadcrumbs[i], -1): #Start at i and go backwards until the breadcrumb value
                text = filename[j-1] + " " + text  #This range of text needs to be added to the final output
            i = breadcrumbs[i] #Start at the next range that needs to be printed
            text = "\n" +  text #Add line breaks after chunks of words are printed
        print(text)
    return DP[len(filename)]


# print(splitfile("C:/Users/tsaik/Desktop/CS Homework/CS140/sample1.txt"))
#print(format(["You", "don't", "know","about", "me", "without", "you", "have", "read", "a", "book", "by", "the", "name"], 50, 3, True))

#print(format("C:/Users/tsaik/Desktop/CS Homework/CS140/huckleberry.txt", 50, 3, True))
