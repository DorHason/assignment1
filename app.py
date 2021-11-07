import datetime
import json

from flask import request

from helpers import validate_payload
from create_app import create_app
from database import get_modified_messages, get_random_messages
from models import Message, db

app = create_app()


# removes whatever is currently in the DB, and stores 5000 duplicates of the provided data entry example
@app.route('/initialize', methods=['GET'])
def initialize():
    # restart table
    db.session.query(Message).delete()
    db.session.commit()
    # create 5000 entries and save to DB
    messages = [Message(status=i, data="data example", timestamp=int(datetime.datetime.utcnow().timestamp()))
                for i in range(5000)]
    db.session.add_all(messages)
    db.session.commit()
    return json.dumps("Initialized"), 200


# randomly selects a number of entries (according to what was sent in data.entries),
# and for each entry modifies the value of the boolean field 'is_modified' from false to true
@app.route('/modify', methods=['POST'])
def modify():
    json_data = request.get_json()
    # validate payload
    if not validate_payload(json_data):
        return json.dumps("Payload is not valid"), 404
    # modify rows randomly and save to DB
    entries = json_data['entries']
    messages = get_random_messages(entries)
    for message in messages:
        message.is_modified = True
    db.session.commit()
    return json.dumps('modified'), 200


# goes over the database and finds the entries that were modified
# returns a human-readable report that specifies how many entries were modified, and which one (their ID's)
@app.route('/validate', methods=['GET'])
def validate():
    # get modified rows
    modified_messages = get_modified_messages()
    # construct string accordingly
    report_string = f'{len(modified_messages)} messages were modified.'
    if modified_messages:
        modified_ids = [str(item[0]) for item in modified_messages]
        report_string += f' The following ids were modified: {", ".join(modified_ids)}'
    return json.dumps(report_string), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
