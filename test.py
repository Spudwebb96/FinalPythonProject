'''
parents = ('ta mere', 'ton geniteur', 'fils de pute')
autres = ('balek', 'de fou')
faiblesse = {
    'parents': parents,
    'autres': autres,
}


joueur_click = "ta mere"
theme_phrase_joueur = (0,0)  # theme_joueur_phrase = (parents, autres)
for key in faiblesse:
    for i in faiblesse[key]:
        if joueur_click == i:
            if key == 'parents':
                theme_phrase_joueur = (theme_phrase_joueur[0] + 1 ,theme_phrase_joueur[1])
                print(theme_phrase_joueur)

'''


class Joueur(faiblesse) :

