"""
@:filename wkt-sql.py
@:description
@:author Keran Sun (katus)
@:version 1.0, 2020-09-23
"""

if __name__ == '__main__':
    number = 10000
    inputFilename = r'D:\Data\polygon4test.csv'
    outputFilename = r'D:\Data\polygon4test_part.sql'
    print('Running...')
    outputFile = open(outputFilename, 'w')
    new_line = """DROP TABLE IF EXISTS polygon4test_part;
CREATE TABLE polygon4test_part(
    id bigint PRIMARY KEY,
    object_id bigint,
    wkt text
);
INSERT INTO polygon4test_part(id, object_id, wkt) VALUES
"""
    outputFile.write(new_line)
    i = -1
    with open(inputFilename, 'r') as inputFile:
        for line in inputFile:
            i += 1
            if i == 0:
                continue
            str_arr = line.split('"')
            new_line = "\t(" + str_arr[5] + ", " + str_arr[3] + ", '" + str_arr[1] + "')"
            if i == number:
                new_line += ";"
                outputFile.write(new_line)
                break
            else:
                new_line += ", \n"
                outputFile.write(new_line)
    outputFile.close()
    print('All finished!')
