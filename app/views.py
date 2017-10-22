from app import app, door

@app.route('/open', methods=['GET', 'POST'])
def open_door():
    door.open()
    return '200'
