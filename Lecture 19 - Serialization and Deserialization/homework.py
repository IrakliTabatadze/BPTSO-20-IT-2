import json

processed_movies = []


def open_json_file(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
        print(type(data))
        return data


def write_json_file(filename):
    with open(filename, 'w') as json_file:
        json.dump(processed_movies, json_file, indent=4)


def filter_data(json_data):
    for page_json in json_data:
        process_movies(page_json)


def process_movies(movie_json):
    for movie in movie_json['results']:
        release_date = int(movie['release_date'][:4])
        genres = movie['genres']

        if release_date > 2000 and 'Crime' in genres:
            movie['genres'].remove('Crime')
            movie['genres'].append('New_Crime')
        if release_date < 2000 and 'Drama' in genres:
            movie['genres'].remove('Drama')
            movie['genres'].append('Old_Drama')
        if release_date == 2000:
            movie['genres'].append('New_Century')

        processed_movies.append(movie)


def main():
    filename = 'movies.json'

    data = open_json_file(filename)
    filter_data(data)

    write_json_file(filename)


if __name__ == '__main__':
    main()
