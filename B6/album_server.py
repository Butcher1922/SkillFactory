from bottle import route, run, HTTPError, request
import album

@route("/albums/<artist>")
def albums(artist):
    albums_list = album.find(artist)
    if not albums_list:
        message = "Альбомы артиста {} не найдены".format(artist)
        result = HTTPError(404, message)
    else:
        album_names = [album.album for album in albums_list]
        result = "Найдено {} альбомов артиста {}:<br>".format(len(albums_list),artist)
        for i in range(len(album_names)):
            result += str(i+1) + ") " + album_names[i] + "<br>"
    return result

@route("/albums",method="POST")
def create_album():
    year=request.forms.get("year")
    artist=request.forms.get("artist")
    genre=request.forms.get("genre")
    album_name=request.forms.get("album")

    try:
        year = int(year)
    except ValueError:
        return HTTPError(400, "Неверно указан год альбома")

    try:
        new_album = album.save(year,artist,genre, album_name)
    except AssertionError as err:
        result = HTTPError(400, str(err))
    except album.AlreadyExists as err:
        result = HTTPError(409,str(err))
    else:
        print("New #{} album successfuly saved".format(new_album.id))
        result = "Альбом #{} успешно сохранен".format(new_album.id)
    return result

if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)
