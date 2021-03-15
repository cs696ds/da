import pickle

f = 'part-19100_0.pkl'

# open a file, where you stored the pickled data
file = open(f, 'rb')

# dump information to that file
data = pickle.load(file)

# close the file
file.close()

print('Showing the pickled data:')

cnt = 0
for item in data:
    print('The data ', cnt, ' is : ', item)
    cnt += 1


print("Embedding Dimension: %d" % len(data[1][1]))
