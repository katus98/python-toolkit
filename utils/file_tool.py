def merge_files(filename_coll, output_filename):
    output_file = open(output_filename, 'a', encoding='UTF-8')
    for filename in filename_coll:
        with open(filename, 'r', encoding='UTF-8') as file:
            for line in file:
                output_file.write(line)
    output_file.flush()
    output_file.close()


def split_file(filename, count):
    file = open(filename, 'r', encoding='UTF-8')
    output = filename[0:filename.rindex('\\') + 1]
    out_file = open(output + 'temp0.csv', 'w', encoding='UTF-8')
    c, f = 0, 0
    for line in file:
        out_file.write(line)
        c += 1
        if c >= count:
            out_file.close()
            f += 1
            out_file = open(output + 'temp' + str(f) + '.csv', 'w', encoding='UTF-8')
            c = 0
    out_file.close()
    file.close()
