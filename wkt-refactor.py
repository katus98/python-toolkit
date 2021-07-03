"""
@:description WKT文件格式重构
@:author Keran Sun (katus)
@:version 1.0
"""

if __name__ == '__main__':
    inputFilename = r'D:\Data\polygon4test.csv'
    outputFilename = r'D:\Data\part.csv'
    print('Running...')
    outputFile = open(outputFilename, 'w')
    with open(inputFilename, 'r') as inputFile:
        for line in inputFile:
            line = line.replace('"', '')
            line = line.replace('\n', '')
            line = line.replace('\r', '')
            lst = line.split('\t')
            newLine = ''
            for i in range(1, len(lst)):
                newLine += lst[i] + '\t'
            newLine += lst[0] + '\n'
            outputFile.write(newLine)
    outputFile.close()
    print('All finished!')
