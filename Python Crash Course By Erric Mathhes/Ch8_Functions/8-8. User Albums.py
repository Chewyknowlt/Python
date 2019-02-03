print('8-8. User Albums')

def make_album(Artist, Song_Title, Track = 0):
    #Using dictionary to store.
    music = {
            'Artist' : Artist.title(),
            'Song Title' : Song_Title.title(),
            }
    # Making track parametre which is optional.
    if Track:
        music['Track'] = Track
    return music
#Making an infinite loop.
while True:
    print('\nFill under all formalities: ')
    
    #Making if condition to quit.
    artist = input('Artist Name: ')
    if artist == 'q':
        break

    song_title = input('Song Title: ')
    if song_title  == 'q':
        break

    track = input('Track no. ')
    if track == 'q':
        break

    gana = make_album(artist, song_title, track)
    print('Information:\n ' + str(gana))
