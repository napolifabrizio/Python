from Modelos.Filme import Filme
from Modelos.Serie import Serie
from Modelos.Playlist import Playlist

vingadores = Filme("vingadores - guerra infinita", 2018, 160)
tmep = Filme("todo mundo em pânico", 1999, 100)
suits = Serie("Suits", 2009, 9)
loki = Serie("Loki", 2022, 2)

vingadores.dar_likes(1000)
suits.dar_likes(250)
loki.dar_likes(200)
tmep.dar_likes(100)

filmes_e_series = [vingadores, suits, loki, tmep]
playlist_fim_de_semana = Playlist("fim de semana", filmes_e_series)

print(f"Tamanho da playlist: {len(playlist_fim_de_semana)}")

for programa in playlist_fim_de_semana:
    print(programa)


