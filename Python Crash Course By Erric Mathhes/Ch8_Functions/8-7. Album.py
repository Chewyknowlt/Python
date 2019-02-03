print('8-7. Album')

'''
def make_album(Artist, Song):
    # Using dictionary to store parameters.
    music = {
        'Artist Name'  : Artist.title(),
        'Song Title'   : Song.title()
        }
    return music

gana = make_album('atif aslam', 'lamhe')
print(gana)

gana = make_album('arijit', 'channa mereya')
print(gana)
    
gana = make_album('atif', 'jal main kahin')
print(gana)
'''
def make_album(Artist, Song, Track = 0):
    # Using dictionary to store parameters.
    music = {
        'Artist Name'  : Artist.title(),
        'Song Title'   : Song.title()
        }
    # Making track perametre which is optioanal.
    if Track:
        music['Track'] = Track
    return music

gana = make_album('atif aslam', 'lamhe')
print(gana)

gana = make_album('arijit', 'channa mereya')
print(gana)
    
gana = make_album('atif', 'jal main kahin')
print(gana)

# Optional track with numbers.
gana = make_album('atif', 'be inteha',Track = 8)
print(gana)
