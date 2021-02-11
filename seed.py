from models import Playlist, Song, PlaylistSong, db
from app import app

db.drop_all()
db.create_all()

p1 = Playlist(name='Romantic', description='date night songs')
p2 = Playlist(name='Italian', description='cooking music')
p3 = Playlist(name='Coffee shop', description='Study music')

db.session.add_all([p1, p2, p3])
db.session.commit()

s1 = Song(title='Fire For You', artist='Cannons', relation=[
          PlaylistSong(playlist_id=p1.id)])
s2 = Song(title='Lei e noi', artist='I Segreti', relation=[
          PlaylistSong(playlist_id=p2.id)])
s3 = Song(title='A Bridge To Mend', artist='Rizik', relation=[
          PlaylistSong(playlist_id=p3.id)])

db.session.add_all([s1, s2, s3])

db.session.commit()
