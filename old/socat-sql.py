def get_ele(ori):
    if ori == 'NaN':
        return 'null'
    else:
        return ori


def append_line(p_str_arr):
    string = ''
    for j in range(5, 32):
        string += ", " + get_ele(p_str_arr[j])
    return string


if __name__ == '__main__':
    # number = 100000
    inputFilename = r'D:\Data\SOCATv2020.tsv'
    outputFilename = r'D:\Data\SOCATv2020.sql'
    print('Running...')
    outputFile = open(outputFilename, 'w')
    new_line = """DROP TABLE IF EXISTS SOCAT_v2020;
CREATE TABLE SOCAT_v2020(
    Expocode VARCHAR(50), 
    version VARCHAR(50), 
    Source_DOI VARCHAR(50), 
    QC_Flag VARCHAR(50), 
    yr INTEGER, 
    mon INTEGER, 
    day INTEGER, 
    hh INTEGER, 
    mm INTEGER, 
    ss INTEGER, 
    longitude DOUBLE, 
    latitude DOUBLE, 
    sample_depth DOUBLE, 
    sal DOUBLE, 
    SST DOUBLE, 
    Tequ DOUBLE, 
    PPPP DOUBLE, 
    Pequ DOUBLE, 
    WOA_SSS DOUBLE, 
    NCEP_SLP DOUBLE, 
    ETOPO2_depth DOUBLE, 
    dist_to_land DOUBLE, 
    GVCO2 DOUBLE, 
    xCO2water_equ_dry DOUBLE, 
    xCO2water_SST_dry DOUBLE, 
    pCO2water_equ_wet DOUBLE, 
    pCO2water_SST_wet DOUBLE, 
    fCO2water_equ_wet DOUBLE, 
    fCO2water_SST_wet DOUBLE, 
    fCO2rec DOUBLE, 
    fCO2rec_src DOUBLE, 
    fCO2rec_flag DOUBLE
);
"""
    flag = False
    outputFile.write(new_line)
    i = 0
    with open(inputFilename, 'r') as inputFile:
        for line in inputFile:
            line = line.replace('\n', '')
            str_arr = line.split('\t')
            if len(str_arr) == 32:
                if flag:
                    i += 1
                    new_line = "INSERT INTO SOCAT_v2020 VALUES"
                    new_line += "('" + get_ele(str_arr[0]) + "', '" + get_ele(str_arr[1]) + "', '" + get_ele(
                        str_arr[2]) + "', '"
                    new_line += get_ele(str_arr[3]) + "', " + get_ele(str_arr[4])
                    new_line += append_line(str_arr)
                    new_line += ");\n"
                    outputFile.write(new_line)
                    # if i == number:
                    #     break
                else:
                    flag = True
    outputFile.close()
    print('All finished!')
