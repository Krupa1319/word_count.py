def count_words(text):
    words=text.strip().split()
    return len(words)

#Function to check if input contains numbers
def check_numbers(text):
    return any(char.isdigit() for char in text)

#main program
def main():
    #prompt user for input
    text=input("Enter a sentence or paragraph:")
    
    #Error handling:check for empty input
    while not text.strip():
        text=input("Input can not be empty.\nplease enter a sentence or paragraph:")
    #check for numbers in input
    if check_numbers(text):
        #if input contains only numbers ask user to enter a sentence or paragraph
        while check_numbers(text):
            text=input("Input contains numbers.\nplease enter a sentence or a Paragraph:")
            
    #counts words
    word_count=count_words(text)
    
    #Displays output
    print(f"\nWord count is: {word_count}\n")
    
if __name__=="__main__":
    main()