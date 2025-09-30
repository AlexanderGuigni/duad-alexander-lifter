def open_file_get_Song_List(path):
    try:
        with open(path) as song_file:
            return song_file.readlines()
    except Exception as ex:
        print(f"Error Reading: {ex}")
    
def create_new_file_with_sorted_songs(song_list, path):
    try:
        with open(path, "a") as sorted_songs_file:
            for song in song_list:
                sorted_songs_file.write(song)
    except Exception as ex:
        print(f"Error Writing: {ex}")

def main():
    try:
        path = "SongsList.txt"
        list_of_songs = open_file_get_Song_List(path)
        list_of_songs.sort()
        create_new_file_with_sorted_songs(list_of_songs, "SortedSongList.txt")
    except Exception as ex:
        print(f"Error: {ex}")

main()