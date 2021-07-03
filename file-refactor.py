"""
@:filename file-refactor.py
@:description
@:author Keran Sun (katus)
@:version 1.0, 2020-10-16
"""

if __name__ == '__main__':
    inputFilename = r'D:\Data\3S\3S-Test\Extent3.tsv'
    outputFilename = r'D:\Data\3S\3S-Test\Extent4.tsv'
    print('Running...')
    outputFile = open(outputFilename, 'w')
    with open(inputFilename, 'r') as inputFile:
        for line in inputFile:
            line = line.replace('"', '')
            line = line.replace('\n', '')
            line = line.replace('\r', '')
            lst = line.split('\t')
            newLine = ''
            for i in range(0, len(lst)-1):
                newLine += lst[i] + '\t'
            newLine += lst[len(lst)-1] + '\n'
            outputFile.write(newLine)
    outputFile.close()
    print('All finished!')
