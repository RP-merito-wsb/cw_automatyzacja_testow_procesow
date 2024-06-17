import subprocess
import json


class TestAPI:
    def __init__(self, url, oczekiwany_status, kluczowe_elementy):
        self.url = url
        self.oczekiwany_status = oczekiwany_status
        self.kluczowe_elementy = kluczowe_elementy

    def uruchom_test(self):
        try:
            wynik = subprocess.run(['curl', '-s', '-w', '%{http_code}', self.url],
                                   capture_output=True, text=True, check=True)
            odpowiedz_body = wynik.stdout[:-3]
            status_kod = int(wynik.stdout[-3:])

            if status_kod != self.oczekiwany_status:
                return f"Test {self.url}: NIE POWIODŁO SIĘ (Oczekiwany status {self.oczekiwany_status}, otrzymany {status_kod})"

            odpowiedz_json = json.loads(odpowiedz_body)
            for klucz in self.kluczowe_elementy:
                if klucz not in odpowiedz_json:
                    return f"Test {self.url}: NIE POWIODŁO SIĘ (Klucz '{klucz}' nie znaleziony w odpowiedzi)"

            return f"Test {self.url}: ZDANY"

        except subprocess.CalledProcessError as e:
            return f"Test {self.url}: NIE POWIODŁO SIĘ (błąd subprocess: {e})"
        except json.JSONDecodeError:
            return f"Test {self.url}: NIE POWIODŁO SIĘ (Niepoprawna odpowiedź JSON)"
        except Exception as e:
            return f"Test {self.url}: NIE POWIODŁO SIĘ (Nieoczekiwany błąd: {e})"


def main():
    testy = [
        TestAPI("http://api.open-notify.org/iss-now.json", 200, ["timestamp", "iss_position"]),
        TestAPI("http://api.open-notify.org/astros.json", 200, ["people", "number"]),
    ]

    for test in testy:
        print(test.uruchom_test())


if __name__ == "__main__":
    main()
