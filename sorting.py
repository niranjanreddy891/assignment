
# Input given in the question-3

data = {'hello': ['doc1'], 'my': ['doc1'], 'name': ['doc1'], 'is': ['doc1', 'doc2'], 'james': ['doc1', 'doc2'],
'a': ['doc2'], 'developer': ['doc2']}


# To print input data
print("Input is : " + str(data))

# To sort the data
res = {key: sorted(data[key]) for key in sorted(data)}

# To print output
print("Output is : " + str(res))