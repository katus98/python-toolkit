def process_bar(percent, start_str='', end_str='', total_length=0):
    bar = ''.join(['#'] * int(percent * total_length)) + ''
    bar = '\r' + start_str + bar.ljust(total_length) + ' {:0>4.1f}%|'.format(percent * 100) + end_str
    print(bar, end='', flush=True)
