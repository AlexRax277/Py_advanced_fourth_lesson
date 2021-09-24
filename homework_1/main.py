import json


with open('countries.json', 'r', encoding='utf-8') as f:
    file_countries = json.load(f)


class Iterator:
    def __init__(self, file, start, step):
        self.file = file
        self.start = start
        self.step = step

    def __iter__(self):
        self.start -= self.step
        return self

    def __next__(self):
        self.start = self.start + self.step
        if self.start >= len(self.file):
            raise StopIteration
        return self.start

    def foo(self):
        country = self.file[self.start]['name']['common']
        join_country = country.replace(' ', '')
        url = f'https://ru.wikipedia.org/wiki/{join_country}'
        with open('result.json', 'a', encoding='utf-8') as res:
            res.write(f'{country} - {url}\n')
        return


iter = Iterator(file_countries, 0, 1)
for item in iter:
    iter.foo()



