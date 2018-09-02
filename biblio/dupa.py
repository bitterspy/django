# pip install pytest - instaluje moduł test
# sprawdzenie istnienia klasy
def sprawdz_klase():
    klasa = Klasa()
    assert klasa


# sprawdzenie działania metody w klasie
def sprawdz_metode():
    klasa = Klasa()
    klasa.metoda('argument')
    assert klasa.zmienna_zmieniana_przez_metode == wynik_jaki_powinien_byc

# sprawdzenie czy klasa wywołuje zamierzony błąd (sprawdza czy wystąpi błąd jak teks będzie za długi):
def test_tweet_long_message():
    twitter - Twitter()
    with pytest.raises(Exception)
        twitter.tweet('test' * 42)
    assert twitter.tweets == []


# sprawdzenie czy funkcja działa prawidłowo (wynik zawiera słowo "#first")
# FUNKCJA:
def find_hashtag(self, message):
    return re.findall("#(\w+)", message)


# TEST:
def test_find_hashtag():
    twitter = Twitter()
    message = "Test #first message"
    assert hastag in twitter.find_hashtag(message)


# parametryzacja testów: (dekorator podaje parametry do funkcji, dzięki temu mozęmy przetestować trzy warianty)
@pytest.mark.parametrize("message,hashtag", (
        ("Test #first message", "first"),
        ("#first Test messge", "first"),
        ("Test #FIRST message", "FIRST")
))
def test_tweet_with_hashtag(message, hashtag):
    twitter = Twitter()
    assert hashtag in twitter.find_hashtag(message)


# fixture - reużywalne fragmenty kodu (generowanie atryutu funkcj poprzez inną funkcję???) zamiast pisać wszczędzie twitter=Twitter() przekazujemy to w argumencie funkcji
@pytest.fixture
def twitter():
    twitter = Twitter()
    return twitter


def test_twitter_initialization(twitter):
    assert twitter


# fixture może przyjmować różne argumenty:
# scope="function" - fixture żyje tylko od początku do końca funkcji
# scope="module" - fixture żyje w pliku testowym
# scope="session" - żyje w sesji

# generatory:
# jeżeli chcemy aby w finkcji fixture po wykonaniu jej uruchomić coś jeszcze możeny to dodać w ten sposób (yield jest generatorem i wywoła raz twitter = Twitter() a potem funkcję twitter.delete()
@pytest.fixture
def twitter():
    twitter = Twitter()
    yield twitter
    twitter.delete()


# fixture może też mieć parametry: (wywołujemy klasę Twitter z pustym backend lub z wartością, oprócz tego zmieniliśmy nazwę funkcji po pokrywałą się ze zmienną.
# Żeby jednak funkcje widziały parametr pod nazwą "twitter", trzeba dodać parametr "name='twitter'"
@pytest.fixture(params=[None, 'test.txt'], name='twitter')
def fixture_twitter(request):
    twitter = Twitter(backend=request.param)


# request: po dodaniu request dowiemy się kto wywołał test a finalizer jest inną metodą do powyższego przykładu z generatorem
@pytest.fixture(request)
def twitter():
    twitter = Twitter()

    def fin()
        twitter.delete()

    request.addfinalizer(fin)
    return twitter
