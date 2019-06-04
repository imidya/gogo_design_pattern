import abc


class UN:
    countries = []
    def add_to_un(self, country):
        self.countries.append(country)

    def announce_to_all_countries(self, country, msg):
        for target_country in self.countries:
            if country != target_country:
                print(f'{country.name} talk to {target_country.name}, says {msg}')


# TODO: Abstract class Country

class US(Country):
    pass


class UK(Country):
    def announce(self, msg):
        # TODO

if __name__ == '__main__':
    UN = UN()
    US = US(UN, 'US')
    UK = UK(UN, 'UK')
    UN.add_to_un(US)
    UN.add_to_un(UK)

    UK.announce('Trade War')
