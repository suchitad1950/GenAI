#The zip() function in Python is used to combine multiple iterables (like lists, tuples) into an iterator of tuples
# Pairing items from two lists
names = ["Hema","Riya","Nita"]
scores = [85, 90, 88]
paired = list(zip(names,scores))
print(paired)

#  Zipping two lists of different lengths
names = ["Hema", "Riya","Nita"]
scores =[85 ,90]
paired = list(zip(names,scores))
print(paired)


# Unzipping with zip()
# You can unzip a list of tuples back into individual lists using the zip() function with the unpacking operator *.

paired = [('Hema',85),( 'Riya',90), ('Nita', 88)]
names, scores = zip(*paired)
print(names)
print(scores)

