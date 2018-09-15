from Color import color
import urllib

class Header:

    def __init__(self, path):
        self.path = path
        self.status = True

    def reader(self):
        try:
            opener = urllib.urlopen(self.path)
            if opener.code == 200:
                pass
            elif opener.code == 404:
                raise IOError
        except IOError:
            self.status = False
