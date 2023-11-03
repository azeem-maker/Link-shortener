import pyshorteners


def link_shortener(l):
    shortener = pyshorteners.Shortener()
    short_link = shortener.tinyurl.short(l)

    print("real link: " + l)
    print("short link: " + short_link)


if __name__ == '__main__':
    print("hwllo! Welcome to link shortener")
    link = input("enter your link: \n")

    link_shortener(link)
