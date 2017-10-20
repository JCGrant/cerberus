from app import app, door

@app.route('/open')
def open_door():
    door.open()
    return '200'
