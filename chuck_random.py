import requests

class Test_new_joke():
    """Create new joke"""
    def __init__(self):
        pass

    def create_new_joke(self):
        """Create random joke"""
        url = 'https://api.chucknorris.io/jokes/random'
        result = requests.request('get', url)
        assert 200 == result.status_code
        if result.status_code == 200:
            print('Success')
        else:
            print('Failed')
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        check_info = check.get("categories")
        print(check_info)
        assert check_info == []
        print('Category - OK')
        check_value = check.get('value')
        print(check_value)
        name = 'Chuck'
        if name in check_value:
            print('Joke about Chuck')
        else:
            print('ERROR!!!!!!')

    def create_new_joke_category(self, category):
        """Create joke for category ["animal","career","celebrity","dev",
        "explicit","fashion","food","history","money","movie","music","political",
        "religion","science","sport","travel"] """
        
        url = f'https://api.chucknorris.io/jokes/random?category={category}'
        result = requests.request('get', url)
        assert 200 == result.status_code
        if result.status_code == 200:
            print('Success')
        else:
            print('Failed')
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        check_cat = check.get("categories")
        if check_cat == [f"{category}"]:
            print('Category sport')
        else:
            print('Error')




random_joke = Test_new_joke()
random_joke.create_new_joke()

sport_joke = Test_new_joke()
sport_joke.create_new_joke_category('sport')