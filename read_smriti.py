import cPickle as pickle
import glob

class Song(object):
    def __init__(self, name, url):
        self.url = base_url + url
        self.name = name
        self.meta_data = {}
        self.read_song()
 
    def read_song(self):
        html = urllib.urlopen(self.url)
        dom = bs4.BeautifulSoup(html, 'lxml')

        pstats = dom.find_all("ul", {"class": "pstats"})[0]
        for li in pstats.find_all("li"):
            data = "" if len(li.contents) < 3 else li.contents[2].contents[0]
            self.meta_data[li.contents[0].contents[0]] = data
 
        songbody = dom.find_all("div", {"class": "songbody"})[0]
        self.lyrics = songbody.getText()

smriti_year = {}
for i in glob.glob('./smriti_songs/*.p'):
    print i
    smriti_year[int(i[-6:-2])] = pickle.load(open(i, 'rb'))

