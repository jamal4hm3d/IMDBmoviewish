import urllib.request, urllib.parse, urllib.error
import json
import ssl
import sys

api_key = input("Enter the api key here: ")

url = "https://imdb-api.com/en/API/SearchMovie/+api_key+"/"
url2 = "https://imdb-api.com/en/API/Title/+api_key+"/"
det = "/Trailer,Ratings,"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    mv = input("Enter movie name:")
    furl = url + urllib.parse.quote(mv)
    uh = urllib.request.urlopen(furl, context=ctx)
    data = uh.read().decode()
    js = json.loads(data)
    try:
        idm = js["results"][0]["id"]
    except:
        print("Thank you for using")
        break
    furl2 = url2 + idm + det
    uh = urllib.request.urlopen(furl2, context=ctx)
    data = uh.read().decode()
    js1 = json.loads(data)
    fulltitle = js1["fullTitle"]
    imageurl = js1["image"]
    plot = js1["plot"]
    directors = js1["directors"]
    stars = js1["stars"]
    genres = js1["genres"]
    imdbr = js1["ratings"]["imDb"]
    metar = js1["ratings"]["metacritic"]
    tmdbr = js1["ratings"]["theMovieDb"]
    rotten = js1["ratings"]["rottenTomatoes"]
    trailer = js1["trailer"]["link"]
    with open("movie.md", "a+") as m:
        print(
            "#",
            " ",
            fulltitle,
            "\n",
            "![image]",
            "(",
            imageurl,
            ")",
            "\n\n",
            genres,
            "\n\n",
            "[Trailer]",
            "(",
            trailer,
            ")",
            "\n\n",
            "## Plot:",
            "\n\n",
            plot,
            "\n\n",
            "## Directors:",
            "\n\n",
            directors,
            "\n\n",
            "## Cast:",
            "\n\n",
            stars,
            "\n\n",
            "## Ratings:",
            "\n\n",
            "|site  |rating   |",
            "\n",
            "|:-----:|:-----:|",
            "\n",
            "|",
            "IMDB",
            "|",
            imdbr,
            "|",
            "\n",
            "|",
            "Metacritic",
            "|",
            metar,
            "|",
            "\n",
            "|",
            "Rotten Tomatoes",
            "|",
            rotten,
            "|",
            "\n",
            "|",
            "theMovieDb",
            "|",
            tmdbr,
            "|",
            "\n\n",
            "-----------------------------",
            "\n",
            sep="",
            file=m,
        )
    print("Done")

