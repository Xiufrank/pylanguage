def writeFile():
    str = 'This is a test of the emergency text system'
    fileName = '/Users/frank/Documents/Ex/test1'
    file = open(fileName, 'wt')
    file.write(str)
    file.close()

    file = open(fileName, 'rt')
    str1 = file.read()
    if str == str1:
        print("相同")
    else:
        print("不同")

def writeCsv():
    fileName = '/Users/frank/Documents/Ex/books.csv'
    file = open(fileName, 'wt')
    file.write("author,book\n")
    file.write("J R R Tolkien,The Hobbit\n")
    file.write('Lynne Truss,"Eats, Shoots & Leaves"\n')
    file.flush()
    file.close()


if __name__ == "__main__":
    # writeFile()
    writeCsv()
