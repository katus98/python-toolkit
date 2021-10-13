if __name__ == '__main__':
    number = 10000
    inputFilename = r'D:\Data\polygon4test.csv'
    outputFilename = r'D:\Data\polygon4test.sql'
    print('Running...')
    outputFile = open(outputFilename, 'w')
    new_line = """DROP TABLE IF EXISTS polygon4test;
CREATE TABLE polygon4test(
    id bigint PRIMARY KEY,
    object_id bigint,
    geom geometry
);
"""
    outputFile.write(new_line)
    i = -1
    with open(inputFilename, 'r') as inputFile:
        for line in inputFile:
            i += 1
            if i == 0:
                continue
            str_arr = line.split('"')
            new_line = "INSERT INTO polygon4test(id, object_id, geom) VALUES"
            new_line += "(" + str_arr[5] + ", " + str_arr[3] + ", ST_GeomFromText('" + str_arr[1] + "', 4326));\n"
            outputFile.write(new_line)
            # if i == number:
            #     break
    outputFile.close()
    print('All finished!')
