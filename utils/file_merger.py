def merge_files(filename_coll, output_filename):
    output_file = open(output_filename, 'a', encoding='UTF-8')
    for filename in filename_coll:
        with open(filename, 'r', encoding='UTF-8') as file:
            for line in file:
                output_file.write(line)
    output_file.flush()
    output_file.close()
