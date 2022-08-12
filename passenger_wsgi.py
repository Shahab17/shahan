from whitenoise import WhiteNoise

from shahan.wsgi import application

application = WhiteNoise(application, root='../shahan/home/static')
#application.add_files("/path/to/more/static/files", prefix="more-files/")