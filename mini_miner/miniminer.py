import requests as req
from constants import challenge_url

def main():
    miniminer = Miniminer(challenge_url)
    try:
        miniminer.run()
    except req.RequestException as e:
        print(e)

class _MiniminerINIT():
    def __init__(self, challengeUrl):
        self.challengeUrl = challengeUrl

class MiniminerAPI(_MiniminerINIT):
    def get(self):
        response = req.get(self.challengeUrl)
        return response

class Miniminer(_MiniminerINIT):
    def run(self):
        api = MiniminerAPI(self.challengeUrl)
        print("sending GET request...")
        response = api.get()
        if response.status_code != 200:
            raise req.RequestException(f"BAD REQUEST! Status Code: {response.status_code}")
        print(f"Received successful response! Status Code: {response.status_code}")

if __name__ == "__main__":
    main()
