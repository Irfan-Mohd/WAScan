import Header, urllib, re
from Vulnerability import Vulnerability
from UserAgent import userAgent
from Color import color


class Scan:
    """This class fetches payloads and processes it."""
    def __init__(self, path):
        self.path = path

    def __main__(self, payloads, check):
        """ This function processes the payloads."""
        opener = urllib.urlopen(self.path)
        count = 0                   #Stores the count of vulnerabilities found
        for params in self.path.split("?")[1].split("&"):
            for payload in payloads:
                bugs = self.path.replace(params, params + str(payload).strip())
                request = userAgent.open(bugs)
                html = request.readlines()
                for line in html:
                    checker = re.findall(check, line)
                    if len(checker) !=0:
                        print color.red + "  Payload: " ,payload + color.green
                        try:
                            print "  Error Message : ....{}".format(line.strip()[line.strip().index('use'):])
                        except ValueError:
                            print "  Error Message : {}".format(line.strip())

                        print color.blue + "  Injection: " + color.end + bugs
                        print color.green + "  Exploitation Successfull !!" + color.end
                        print color.blue,
                        print "-"*80, color.end
                        count +=1
        if count == 0:
            print color.green+"  Target is not vulnerable!"+color.end
        else:
            print color.blue + "  Congratulations you've found %i bugs" % (count) + color.end

    def _start(self):
        """"It fetches the payloads from the exploits."""
        v = Vulnerability()
        f = dir(v)
        for ff in f:
            if not ff.startswith("_"):
                fu = getattr(v, ff)
                fu()
                print color.green + "Now Scanning For " + v._description + color.blue +"\n  [!] Please Wait..." + color.end
                self.__main__(v._payloads, v._check)
                print "\n\n\n"
