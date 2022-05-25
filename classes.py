import requests
import json


class BuscarAPI:
    def __init__(self):
        self.url = requests.get(f'https://pokeapi.co/api/v2/pokemon')
        self.api = self.url.json()
        self.pokemons_acesso = list()
        self.poke = dict()
        self.list_of_pokemons = list()

    def agrupar(self): 
        for pokemon in self.api['results']:
            self.poke['name'] = pokemon['name']
            self.poke['url'] = pokemon['url']
            self.pokemons_acesso.append(self.poke.copy())
            self.poke.clear()

    def listar_pokemons(self):
        nomes = list(map(lambda x: x['name'], self.pokemons_acesso))
        return nomes 

    def pokemons_detalhes(self):
        urls_detalhes = list(map(lambda x: x['url'], self.pokemons_acesso))
        for detalhe in urls_detalhes:
            acesso = requests.get(detalhe)
            acesso = acesso.json()
            self.poke['nome'] = acesso['name']
            self.poke['peso'] = acesso['weight']
            self.poke['tipo'] = acesso['types']

            self.list_of_pokemons.append(self.poke.copy())
            self.poke.clear()
        
        for index in self.list_of_pokemons:
            print('='*40)
            print(f"{index['nome'].upper():^40}")  
            print(f"Nome: {index['nome'].capitalize()}")  
            print(f"Peso: {index['peso']}")  
            print(f"Tipo: {index['tipo'][0]['type']['name'].capitalize()}")  
           
        return acesso    
        