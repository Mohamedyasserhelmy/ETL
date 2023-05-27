class Config(object):
    Testing = False


class Development_config(object):
    UPLOAD_FOLDER = './uploads'
    ALLOWED_EXTENSIONS = {'csv','xml','json'}
    DATABASE_URI = "LOCAL DATABASE FOR DEVELOPMENT"
    SECRET_KEY = 'e2f88ed4ffb867c83357effd0b903bfb7749b3fef06b47f37612cd89bb573ea6'

class Production_config(object):
    DATABASE_URI = "ONLINE MONGO ATLAS DB FOR PRODUCTION"
    
