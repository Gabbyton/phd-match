import requests

BASE_URL = "http://api.semanticscholar.org/graph/v1"

def get_paper_info(ids: list[str]):
    endpoint = f"{BASE_URL}/paper/batch"
    params = {'fields': 'title,abstract,year'}
    try:
        response = requests.post(endpoint, params=params, json={"ids": ids})
        response.raise_for_status()
        return response.json()
    except Exception as error:
        print(error)

if __name__ == "__main__":
    paperId = "10.1103/physrevmaterials.8.104405"
    print(get_paper_info([paperId]))