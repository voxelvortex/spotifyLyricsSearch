import json
import loader, spotify
from sys import argv


def main(playlist_id, args):
    auth = json.load(open('auth.json'))
    CID = auth["client_id"]
    CSEC = auth["client_secret"]
    data = spotify.get_data(CID, CSEC, playlist_id)
    track = spotify.get_name_and_artist(data)
    print(loader.search_for_keywords( (["test testy thing"],["ha har him"]), ["ha"]))



if __name__ == '__main__':
   # loader.check_input(argv)
    uri = argv[0]
    del argv[0]
    main(uri, argv)
