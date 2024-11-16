import pickle

hello_str = "Hello World!"

print(type(hello_str))

hello_byte = pickle.dumps(hello_str)

print(hello_byte)

with open('hello.pkl', 'wb') as pkl_file:
    pickle.dump(hello_str, pkl_file)


deserialized_bytes = pickle.loads(hello_byte)
print(deserialized_bytes)


with open('hello.pkl', 'rb') as pkl_file:
    data = pickle.load(pkl_file)
    print(data)