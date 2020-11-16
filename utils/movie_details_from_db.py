def movie_details(movie_det):
    '''
    This function purpose is to access a record of the model Movie and return a dictionary with its values.

    Parameters
        movie_det <- Must be a record of the Movie model.

    '''
    tagline_big = False
    if len(movie_det.tagline) > 100:
        tagline_big = True
    else:
        pass
    content_movie = {
        'movie_id': movie_det.movie_id,
        'imbd_id': movie_det.imbd_id,
        'movie_title': movie_det.movie_title,
        'genero': movie_det.genero,
        'original_language': movie_det.original_language,
        'overview': movie_det.overview,
        'poster_path': 'https://image.tmdb.org/t/p/original' + movie_det.poster_path,
        'release_date': movie_det.release_date,
        'budget': (f'{int(movie_det.budget):,}').replace(',', '.'),
        'revenue': (f'{int(movie_det.revenue):,}').replace(',', '.'),
        'runtime': movie_det.runtime,
        'vote_average': movie_det.vote_average,
        'tagline': movie_det.tagline,
        'tagline_big': tagline_big,
    }

    return content_movie
