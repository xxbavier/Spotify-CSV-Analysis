import random

# Read the contents of the songs dataset file and return the data in a dictionary format
def data_to_dict(filename, header):
    # Open file to access data
    data_file = open(filename, "r")

    # If file has a header line read it and save it
    header_line = ""
    if header:  
        header_line = data_file.readline().strip() # Read the header line of the file to extract attributes

    # Initialize an empty dictionary to store the data
    data_dict = {}
    
    # Iterate over each line in the data file
    for line in data_file:

        # Remove leading and trailing whitespaces, and split the line into a list using commas
        line = line.strip().split(",")
        
        # Get the artist name
        artist = line[1]
        # Remove the artist name from the details since it is used as the key
        line.pop(1)
        # If artist in dictionary add line value list
        if artist in data_dict:
            data_dict[artist].append(line)
        else: # New type found
            data_dict[artist] = [line]
      
     # Close the file
    data_file.close()

    # Return the data organinzed in a dictionary
    return data_dict

########################################################
# uncomment the following line to display the data dictionary
data = data_to_dict("SpotifySongs-Dataset.csv", True)
#print(data)
########################################################
# Add your solution here
########################################################

# Output number of artists
print(f"There are {len(data)} artists in the dataset.")

# Create a list for lengths of each artist
artist_song_lengths = {}

# Create variables for the longest song and highest popularity
longest_song = [0, ""]
highest_popularity = [0, ""]

# Initialize variable for the averages for all properties
averages_for_properties = {}

# Find averages across all properties
for artist, songs in data.items():
    keys = ["SongName","Popularity","Danceability","Energy","Key","Loudness","Liveness","Valence","Tempo","Duration_ms"]

    averages = {}

    for key in keys:
        index = keys.index(key)
        list_of_songs = []

        if index != 0:
            for song in songs:
                list_of_songs.append(float(song[index]))
        
            averages[key] = sum(list_of_songs)/len(list_of_songs)

    averages_for_properties[artist] = averages

# Create a list for all of the songs
songs = []

# Iterate through all songs
for artist, artist_songs in data.items():
    for song in artist_songs:
        song.insert(0, artist)
        songs.append(song)

# Find the longest song and highest popularity song
for song in songs:
    length = int(song[-1])
    if length > longest_song[0]:
        longest_song = [length, song]

    popularity = int(song[2])
    if popularity > highest_popularity[0]:
        highest_popularity = [popularity, song]

# Create a variable for shortest song using the longest song
shortest_song = longest_song.copy()

# Find the shortest song
for song in songs:
    length = int(song[-1])
    if length < longest_song[0]:
        longest_song = [length, song]

# Output number of songs
print(f"There are {len(songs)} songs in the dataset.")

# Output the averages data
print(averages_for_properties)

# Output a random song
random_song = random.choice(songs)

# Output the average lengths of each artist
for artist, value in artist_song_lengths.items():
    lengths_sum = 0

    for song in value:
        lengths_sum += int(song)
    
    average_length = lengths_sum/len(value)
    print(f"The average length of a {artist} song is {average_length}.")

# Output the highest popularity song
print("{} by {} is the most popular song.".format(highest_popularity[1][1], highest_popularity[1][0]))

# Output the longest song
print("{} by {} is the shortest song.".format(longest_song[1][1], longest_song[1][0]))

# Output the shortest song
print("{} by {} is the longest song.".format(shortest_song[1][1], shortest_song[1][0]))

# Create dictionary variable for the most common key
keys_dictionary = {}

# Find the song with the most common key
for song in songs:
    try:
        keys_dictionary[song[5]] += 1

    except:
        keys_dictionary[song[5]] = 0

# Output the most common key
most_common_key = [0, ""]

for key, value in keys_dictionary.items():
    if value > most_common_key[0]:
        most_common_key = [value, key]

print("{} was the most common key used in songs.".format(most_common_key[1]))

# Create find_artist_by_property function
def find_artist_by_property(prop, boolean):
    if boolean:
        # Highest average value
        currentRecord = [0, ""]
        for artist, properties in averages_for_properties.items():
            if properties[prop] > currentRecord[0]:
                currentRecord = [properties[prop], artist]
    else:
        # Lowest average value
        currentRecord = [10000000, ""]
        for artist, properties in averages_for_properties.items():
            if properties[prop] < currentRecord[0]:
                currentRecord = [properties[prop], artist]

    return currentRecord

# Display the output of the function
print(find_artist_by_property("Tempo", False))