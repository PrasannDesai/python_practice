# File objects

# f = open('sample.txt', 'r')

# print(f.name)

# print(f.mode)

# f.close()

# Handling files using context manager

with open('sample.txt', 'r') as rf:
    with open('sample2_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

    # f_content = f.read()
    # f_content = f.read(100)
    # f_contents = f.readline()
    # print(f_contents, end='')
    # f_contents = f.readline()
    # print(f_contents, end='')
    # size_to_read = 10
    # f_contents = f.read(size_to_read)
    # print(f_contents)
    # f_contents = f.read(size_to_read)
    # print(f_contents)

    # f.seek(0)

    # f_contents = f.read(size_to_read)
    # print(f_contents)

    # f.write('Test')

    # print(f.tell())
    # while len(f_contents) > 0:
    #     print(f_contents, end='')
    #     f_contents = f.read(size_to_read)


# print(f.name)
# print(f.mode)
# print(f.closed)
