#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    longueur = (len(string))
    #print(len(string))
    reste = longueur%2
    paire_impaire = (reste == 0)
    return paire_impaire
    pass


def remove_third_char(string: str) -> str:
    longueur = (len(string))
    #print('hello world' [2:3])
    nouveau_mot = (string[:2]+ string[3:])
    return nouveau_mot
    pass


def replace_char(string: str, old_char: str, new_char: str) -> str:
    caractere = list(string)
    #print(caractere)
    caractere[6] = 'z'
    new_char = "".join(caractere)
    #print(type(new_char))
    return new_char
    pass


def get_number_of_char(string: str, char: str) -> int:
    #longueur = len(string)
    a = 0
    nombre_occurence = 0

    while a < len(string):
        if string[a] == 'l':
            nombre_occurence += 1
        a +=1

    nombre_occurence-=1

    return nombre_occurence
    pass #ne pas utiliser la fonction count


def get_number_of_words(sentence: str, word: str) -> int:
    liste_mots = sentence.split()
 

    a = 0
    nombre_occurence = 0

    while a < len(liste_mots):
        if liste_mots[a] == 'doo':
            nombre_occurence += 1
        a += 1

    return nombre_occurence
    pass


def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
