#modify batches
import glob

files = filter(lambda i: i != "./binaca_songs.tsv", glob.glob('./*.tsv'))
for b_file in files:
    f = open(b_file, 'r+b')
    print b_file
    content = f.read()
    f.seek(0,0)
    l = '{}\t{}\t{}\n'.format('Song lyrics', 'Mood', 'Offensive')
    f.write(l)
    for line in content.split('\n'):
        f.write('{}\t{}\t{}\n'.format(line, '0', '0'))

    f.close()
