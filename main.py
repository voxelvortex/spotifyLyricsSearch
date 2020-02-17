import json
import loader, spotify;

def main():
    auth = json.load(open('auth.json'))
    CID = auth["client_id"]
    CSEC = auth["client_secret"]
    spotify.test(CID, CSEC)



if __name__ == '__main__':
    main()