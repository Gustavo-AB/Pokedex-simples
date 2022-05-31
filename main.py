from classes import *


if __name__ == '__main__':
    pokeApi = BuscarAPI()

    pokeApi.pintar_linhas()
    print(f"\n{'POKEDEX':^40}")
    pokeApi.pokemons_detalhes()
    print(len(pokeApi.list_of_pokemons))
