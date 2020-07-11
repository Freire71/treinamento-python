# Vamos modelar uma playlist no spotify
# Para isso faremos o uso intenso de listas e dicionários
# Muitas aspectos de uma playlist podem ser mapeados
# Título, descrição, autor, foto, número de seguidores, total de músicas, total de horas de música
# Se a mesma foi favoritada ou se o usuário fez o download da mesma
# Em uma música temos o título, o artista, o album e a duração da mesma
# Sua tarefa é extrair todos esses dados da foto mostrada no slide
# O dado do tempo total de uma playlist deve ser extraído iterando por todas as músicas e somando o tempo de cada uma
# Para a foto da playlist, utilize uma url de uma foto da sua preferência

from datetime import datetime, timedelta

playlist = {
    "titulo": "São João",
    "descricao": "Seleção da sua festa incluindo músicas escolhidas por Elba Ramalho!",
    "criado_por": "Spotify",
    "favoritado": True,
    "seguidores": 42735,
    "disponivel_offline": False,
    "musicas": [
        {
            "titulo": "Medley para Dançar o São João",
            "artista": "Elba Ramalho",
            "album": "Medley para Dançar",
            "duracao": "00:12:24",
        },
        {
            "titulo": "Medley para Dançar o São João",
            "artista": "Elba Ramalho",
            "album": "Medley para Dançar", 
            "duracao": "00:04:04",
        }
    ]
}
total_musicas = len(playlist["musicas"])

print(f"Total de músicas: {total_musicas}")

tempo_total = 0
for musica in playlist["musicas"]:
  date_time = datetime.strptime(musica["duracao"], "%H:%M:%S")
  delta = date_time - datetime(1900, 1, 1)
  tempo_em_segundos = delta.total_seconds()
  tempo_total += tempo_em_segundos

print(f"Tempo total  de playlist: {timedelta(seconds=tempo_total)}")