def get_wkt(m_x, m_y, m_w):
    str1 = str(m_x) + ' ' + str(m_y)
    str2 = str(m_x + m_w) + ' ' + str(m_y)
    str3 = str(m_x + m_w) + ' ' + str(m_y + m_w)
    str4 = str(m_x) + ' ' + str(m_y + m_w)
    return 'POLYGON ((' + str1 + ', ' + str2 + ', ' + str3 + ', ' + str4 + ', ' + str1 + '))'


def get_cc(cc):
    lcc = cc % 9 + 1
    return '0' + str(lcc)


if __name__ == '__main__':
    filename = r'D:\Data\WKT\TEST.tsv'
    startPoint = {'x': 13550255, 'y': 3490255}
    width = 500
    number = {'row': 181, 'col': 181}
    print('Running...')
    file = open(filename, 'w')
    count = 0
    for r in range(number.get('row')):
        y = startPoint.get('y') + r * width
        for c in range(number.get('col')):
            x = startPoint.get('x') + c * width
            line = str(count + 1) + '\t' + get_cc(count) + '\t' + get_wkt(x, y, width) + '\n'
            file.write(line)
            count += 1
    file.close()
    print('All finished!')
