from apps.randomovie.models import Movie


def obj_movie_mod_create():
    '''
    When testing a empty database is created, this code below creates two objects in that database to perform tests.
    '''

    Movie.objects.create(movie_id=102899, imbd_id='tt0478970', movie_title='Ant-Man', genero='Adventure', original_language='en', overview='''
        Armed with the astonishing ability to shri
        nk in scale but increase in strength, master thief Scott Lang must embrace his i
        nner-hero and help his mentor, Doctor Hank Pym, protect the secret behind his sp
        ectacular Ant-Man suit from a new generation of towering threats. Against seemin
        gly insurmountable obstacles, Pym and Lang must plan and pull off a heist that w
        ill save the world.')
        ''',
                         poster_path='/fddtVEUozxvLmehR5yGZjem44pD.jpg', release_date='2015-07-14', budget='130000000', revenue='519311965',
                         runtime='117', vote_average=7.1
                         )

    Movie.objects.create(movie_id=99999, imbd_id='tt3783958', movie_title='La La Land', genero='Drama', original_language='en', overview='''
        Mia, an aspiring actress, serves lattes to movie stars in between auditions and Sebastian, a jazz musician, scrapes by playing cocktail party gigs in dingy bars, but as success mounts they are faced with decisions that begin to fray the fragile fabric of their love affair, and the dreams they worked so hard to maintain in each other threaten to rip them apart.')
        ''',
                         poster_path='//q0dsNZOuSKzAdZod9ohPXJ4GQUs.jpg', release_date='2016-11-29', budget='30000000', revenue='446486225',
                         runtime='129', vote_average=7.9
                         )
