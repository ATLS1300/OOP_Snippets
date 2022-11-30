""" 
Reading & Writing Hi Score Files

Note, to make smaller files, this script uses the csv library, not the pandas library.

To use (3 ways):
A. copy the functions and use them in classes (editing required)
B. download this file, save it to the same foldr as your script, import & use dot notation:
    import hiScore
    hiScore.get()
    hiScore.set(1000)
"""
import csv

def get(file="score.txt"):
    '''Gets hiScore from file, if it exists. Returns all data in single string variable.
    Use string methods (split()) to separate values.
    Arguments:
        score (int/float,str) - value to save 
        file (str) - name of file to save to. Must have .txt extension. Saves file to working folder.
        To save to a specific location, add filepath to file name:
            "user/Documents/filename.txt"
    '''
    # Try to read the high score from a file
    try:
        f = open(file, "r")
        high_score = f.read()
        f.close()
        return high_score
    except IOError:
        # Error reading file, no high score; return default score
        print("There is no high score yet.")
        return 0

def set(hi_score, file='score.txt',add=False):
    '''Creates new hi score file if there is none in folder.
    Arguments:
        hi_score (any) - data to save. Can be any data type (except dicts)
        file (str) - name of file. Must include .txt extensinon
        add (bool) - toggles appending to file. Seleect False to overwrite files.
    '''
    if add:
        mode = "a+"
    else:
        mode = "w"
    
    try:
        # Write the file to disk
        f = open(file, mode)
        if type(hi_score) in [list,tuple]:
            for row in hi_score:
                f.write(str(row)+" ")
        else:
            f.write(str(hi_score))
        f.close()
        print('New high score saved.')
    except IOError:
        # Hm, can't write it.
        print("Unable to save the high score.")

if __name__=="__main__":
    
    # get a high score
    hi_score = get() # if file is absent, default score will be produced (int)
    
    # if output is a string, a file has been read
    if type(hi_score) == str: 
        # change hi_score from string to ints
        scoreName,hi_score = hi_score.split() # separates at space
        hi_score = int(hi_score) # convert to int for use
        print(scoreName,hi_score)
    
    # create hi score mock data (this would be generated from your game)
    score = 5000
    name = "Ngozi" 
    
    # replace high score
    if score>=hi_score:
        set((name,score))
    