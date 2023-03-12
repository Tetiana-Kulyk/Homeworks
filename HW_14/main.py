from txt_proxy_writer_reader import TxtProxyWriterReader

if __name__ == '__main__':
    proxy_reader = TxtProxyWriterReader('my_file.txt')

    print(proxy_reader.read_file())
    print('\n')
    print(proxy_reader.write_to_file())
