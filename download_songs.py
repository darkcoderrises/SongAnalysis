import bs4
import urllib
import cPickle as pickle

base_url = "https://www.hindigeetmala.net"
year_url = base_url + "/binaca_geetmala_{}.htm"
meta_data = ["Song Heading", "Singer(s)", "Music Director", "Lyricist", "Movie/Album"]

def get_data_from_track_cell(cell):
    data = cell.findAll("span", {"itemprop": "name"})
    if len(data) == 0:
        return ""
    return next(data[0].children).strip()

class Song:
    """
    Stores the metadata and lyrics of a song
    """

    def __init__(self, track):
        names = track.findAll("td")[1:-1]
        
        self.song_link = track.findAll("a", {"itemprop": "url"})[0].attrs["href"]
        self.meta_info = {meta_data[i] : get_data_from_track_cell(names[i])
                for i in range(len(meta_data))}
        self.download_lyrics()

    def download_lyrics(self):
        html = urllib.urlopen(base_url + self.song_link).read()
        tags = bs4.BeautifulSoup(html, "lxml")
        self.lyrics = next(tags.findAll("pre")[0].children)
        

class BinacaYear:
    """
    Stores all the songs in a perticular year
    """

    def __init__(self, year):
        self.year = year
        self.songs = []

        html = urllib.urlopen(year_url.format(year)).read()
        tags = bs4.BeautifulSoup(html, "lxml")
        tracks = tags.findAll("tr", {"itemprop": "track"})

        for track in tracks:
            song = Song(track)
            self.songs.append(song)

if __name__ == "__main__":
    for year in range(1953, 1984):
        print year
        by = BinacaYear(year)
        pickle.dump(by, open("songs/{}.p".format(year), "wb"))

