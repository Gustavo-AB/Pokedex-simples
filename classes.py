import requests
import json


class BuscarAPI:
    def __init__(self):
        self.url = requests.get(f'https://pokeapi.co/api/v2/pokemon/?limit=10&offset=20')
        self.api = self.url.json()
        self.pokemons_acesso = list()
        self.poke = dict()
        self.list_of_pokemons = list()

        for pokemon in self.api['results']:
            self.poke['name'] = pokemon['name']
            self.poke['url'] = pokemon['url']
            self.pokemons_acesso.append(self.poke.copy())
            self.poke.clear()

        urls_detalhes = list(map(lambda x: x['url'], self.pokemons_acesso))
        for detalhe in urls_detalhes:
            acesso = requests.get(detalhe)
            acesso = acesso.json()
            self.poke['nome'] = acesso['name']
            self.poke['peso'] = float(acesso['weight'])
            self.poke['altura'] = float(acesso['height'])
            self.poke['tipo'] = acesso['types']

            self.list_of_pokemons.append(self.poke.copy())
            self.poke.clear()

    def pokemons_detalhes(self):
        for index in self.list_of_pokemons:
            self.pintar_linhas()
            print()
            print('\033[31m-\033[m'*40)
            print(f"\033[34m{index['nome'].upper():^40}\033[m")  
            print(f"\033[35mNome\033[m: \033[32m{index['nome'].capitalize()}\033[m")  
            print(f"\033[35mPeso\033[m: \033[32m{index['peso']:.2f}Kg\033[m")  
            print(f"\033[35mAltura\033[m: \033[32m{index['altura']}m\033[m") 

            if len(index['tipo']) > 1:
                print(f"\033[35mTipo\033[m: \033[32m{index['tipo'][0]['type']['name'].capitalize()}", end='')  
                print(f", {index['tipo'][0+1]['type']['name'].capitalize()}\033[m")
            else:
                print(f"\033[35mTipo\033[m: \033[32m{index['tipo'][0]['type']['name'].capitalize()}\033[m")  

            print('\033[31m-\033[m'*40)  
            self.pintar_linhas()
            print()
            print(f'\033[33m{"~":^40}\033[m')

    def pintar_linhas(self, char='~'):
        for c in range(1, 21):
            print('\033[35m~\033[m', end='')
            print('\033[34m~\033[m', end='')
            
        