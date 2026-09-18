from time import sleep
def main():
    playlist = [" Boston","Dracula","I Knew It, I Knew You"," hate that i made you love me","Risk It All"]
    playlist.append("Be By You")
    print(playlist)
    playlist.insert(0, "Bohemian Rhapsody")
    print(playlist)
    playlist.pop(4)
    print(playlist)
    print(playlist.index("Risk It All"))
    print("Number of songs in the playlist:", len(playlist))
    playlist.reverse() #this method transforms the current list, it doesn´t creates a new one
    print(playlist)
    playlist.sort()
    print(playlist)

    repeat = len(playlist)
    while repeat > 0:
        print(playlist)
        song_played = playlist[0]
        playlist.pop(0)
        playlist.append(song_played)
        sleep(3)
        repeat -= 1



if __name__ == "__main__":
    main()
