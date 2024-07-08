
from pelicula import Pelicula
from serie import Serie

def main():
    pelicula1 = Pelicula("Inception", 148, "Christopher Nolan")
    serie1 = Serie("Breaking Bad", 47, 1, 1)

    lista_videos = [pelicula1, serie1]

    for video in lista_videos:
        video.reproducir()
        print(video.obtener_informacion())
        video.pausar()
        video.detener()
        print()

if __name__ == "__main__":
    main()
