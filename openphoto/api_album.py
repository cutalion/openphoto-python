from errors import *
from objects import Album

class ApiAlbums:
    def __init__(self, client):
        self._client = client

    def list(self, **kwds):
        """ Return a list of Album objects """
        results = self._client.get("/albums/list.json", **kwds)["result"]
        return [Album(self._client, album) for album in results]

class ApiAlbum:
    def __init__(self, client):
        self._client = client

    def create(self, name, **kwds):
        """ Create a new album and return it"""
        result = self._client.post("/album/create.json", name=name, **kwds)["result"]
        return Album(self._client, result)

    def delete(self, album, **kwds):
        """ Delete an album """
        if not isinstance(album, Album):
            album = Album(self._client, {"id": album})
        album.delete(**kwds)
        
    def form(self, album, **kwds):
        raise NotImplementedError()

    def add_photos(self, album, photos, **kwds):
        raise NotImplementedError()

    def remove_photos(self, album, photos, **kwds):
        raise NotImplementedError()

    def update(self, album, **kwds):
        """ Update an album """
        if not isinstance(album, Album):
            album = Album(self._client, {"id": album})
        album.update(**kwds)

        # Don't return the album, since the API currently doesn't give us the modified album
        # TODO: Uncomment the following once frontend issue #937 is resolved
#        return album

    def view(self, album, **kwds):
        """ 
        View an album's contents.
        Returns the requested album object.
        """
        if not isinstance(album, Album):
            album = Album(self._client, {"id": album})
        album.view(**kwds)
        return album