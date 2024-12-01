__author__ = ''

"""This program counts the number of times each unique word appears in
a text file. The results are output to the command line, and the user
is given the option of printing the results to a new text file."""

import os

COMMON_WORDS = {"the", "be", "are", "is", "were", "was", "am",
                "been", "being", "to", "of", "and", "a", "in",
                "that", "have", "had", "has", "having", "for",
                "not", "on", "with", "as", "do", "does", "did",
                "doing", "done", "at", "but", "by", "from"}


class WordProcess:
    """This class returns the number of times each word appers in a text file."""

    def __init__(self, file):
        """Construct class instance with file attribute."""
        self.file = file

    def sort_by_value(item):
        """Create a key to be used to sort wordlist later."""
        return item[-1]

    def words_dict(self):
        """Compare user input text file to English wordlist and return matches."""
        read_input = self.file.split() #Split a string into a list where each word is a list item:eg['welcome', 'to', 'the', 'jungle']
        read_wordlist = ["this", "is", "a", "test"]  #List declared using brackets [].

        count = 0

        for word in read_input: #List in line 29
            word = word.lower()
            # Removes common punctuation so it's not part of the word.
            read_input[count] = word.strip(".,?!\"\';:()") #line 29, strip() -Remove spaces at the beginning and at the end of the string:
            count += 1

        word_count = {} #Set is defined by values separated by a comma inside braces { }.

        for word in read_input: #read_input List line 29 & Line 37
            word = word.lower() #lower() method returns the lowercased string from the given string. 
            if word in read_wordlist: #List at line 30
                if word not in word_count: #Set in line 40
                    word_count[word] = 1
                else:
                    word_count[word] += 1
            else:
                continue

        return word_count

    def print_top_words(self, choice):
        """
        Sort and print each unique word with its frequency to the console.
        Return the results as a list to use in file output.
        """ 
        word_count = self.words_dict()  #method words_dict()- line 27

        # Uses reverse order to sort (most frequent first).
        items = sorted(word_count.items(), key=WordProcess.sort_by_value, reverse=True) #sorted() function returns a sorted list of the specified iterable object
                #sorted(see line 40-set, key=line 23 function to decide the order, True=sort descending)
        results_list = [] #List declared using brackets []

        # Truncates output if user wants to suppress common words.to prevent from being published
        for word in items[:50]: #line 62
            if choice == "y" and word[0] not in COMMON_WORDS: #Set in line 9
                result = word[0] + ": " + str(word[1]) + " times"
                results_list.append(result)
                print(result)
            elif choice == "n":
                result = word[0] + ": " + str(word[1]) + " times"
                results_list.append(result)
                print(result)

        return results_list

while True:
    user_input = input("Please enter the path and name of the text file you want"
                       " to analyze. (E.g.: C:/Users/Monty/Desktop/file.txt):"
                       "\n")

    class_init = WordProcess(user_input)

    if user_input is False:
        print("The file you specified does not exist.\n")
        continue
    else:
        common_word = ""

        while common_word != "y" or common_word != "n":
            common_word = input("Would you like to strip common words from the results? "
                                "(Y/N) ").lower()

            if common_word == "y" or common_word == "n":
                break

        new_result = WordProcess.print_top_words(class_init, common_word)

        user_output = ""

        while user_output != "y" and user_output != "n":
            user_output = input("\nWould you like to output these results to a file? "
                                "(Y/N) ").lower()

            if user_output == "y":
                # Relative path to current user's desktop.
                user_desktop = os.path.expanduser("~/Desktop")
                output_folder = "/Wordcound Output"

                #Removes path from file name.
                file_name = user_input.split("/")[-1]
                #Remove file extension from name.
                no_ext = file_name.rsplit(".",1)[0]
                #open a new file for writing and assigning to write_file
                write_file = open(no_ext + "_result.txt", "w")   # no_ext variable remove the file extension, _result.txt will be the new file's name. try change no_ext to file_name
                write_file.write("My Result from {}: \n\n".format(file_name)) 
                #write the result to the output file
                for line in new_result:  
                    write_file.write(line + "\n")
                #close write_file
                write_file.close()
                
                print("Success!")
                break
            elif user_output == "n":
                print("Exiting...")
                break

        break
