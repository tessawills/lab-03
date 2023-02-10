from typing import Dict, List, Optional
from flask import Flask, request, jsonify
import pathlib
import uuid
import json


app = Flask(__name__)
thisdir = pathlib.Path(__file__).parent.absolute() # path to directory of this file

# Function to load and save the mail to/from the json file

def load_mail() -> List[Dict[str, str]]:
    """
    Loads the mail from the json file

    Returns:
        list: A list of dictionaries representing the mail entries
    """
    try:
        return json.loads(thisdir.joinpath('mail_db.json').read_text())
    except FileNotFoundError:
        return []

def save_mail(mail: List[Dict[str, str]]) -> None:
    """TODO: fill out this docstring (using the load_mail docstring as a guide)
    
    Summary: write to/adds the mail (message) into the dictionary
    
    Args: (mail: List[Dict[str, str]]):  the mail dictonary

    Returns:
        none
    
    """
    thisdir.joinpath('mail_db.json').write_text(json.dumps(mail, indent=4))

def add_mail(mail_entry: Dict[str, str]) -> str:
    """TODO: fill out this docstring (using the load_mail docstring as a guide)
    
    Summary: generates and gives ID numbers to each mail entry that was previously written to the dictionary
    
    Args: (mail_entry: Dict[str, str]):  the mail entry in the mail dictonary

    Returns:
        the entry's ID number
   
    """
    mail = load_mail()
    mail.append(mail_entry)
    mail_entry['id'] = str(uuid.uuid4()) # generate a unique id for the mail entry
    save_mail(mail)
    return mail_entry['id']

def delete_mail(mail_id: str) -> bool:
    """TODO: fill out this docstring (using the load_mail docstring as a guide)
    
    Summary: finds the ID number that a user enters, and if it is in the dictionary, deletes it. 
    
    Args: (mail_id: str):  mail id of mail wanted to be deleted.

    Returns:
        True if mail was deleted, False if not deleted (because the ID num didn't exist).
     
    """
    mail = load_mail()
    for i, entry in enumerate(mail):
        if entry['id'] == mail_id:
            mail.pop(i)
            save_mail(mail)
            return True

    return False

def get_mail(mail_id: str) -> Optional[Dict[str, str]]:
    """TODO: fill out this docstring (using the load_mail docstring as a guide)
    
    Summary: user enters an ID number, if it matches a number in the dict, it will return the 
    	     corresponding mail entry for the ID 
    
    Args: (mail_id: str):  mail id of mail wanted to be read.

    Returns:
        the mail entry if the ID exists. returns None if the ID does not have a mail entry
    
  
    """
    mail = load_mail()
    for entry in mail:
        if entry['id'] == mail_id:
            return entry

    return None

def get_inbox(recipient: str) -> List[Dict[str, str]]:
    """TODO: fill out this docstring (using the load_mail docstring as a guide)
    
    Summary: looks at each mail entry and checks if the recipient of that entry matches, if it does, it will
    	add its own list of all the corresponding mail entries that that recipient has received.
    
    Args: (recipient: str):  the name/keyword of the recipient being searched for

    Returns:
        a list containing all mail entries that the given recipient has received.
    
    """
    mail = load_mail()
    inbox = []
    for entry in mail:
        if entry['recipient'] == recipient:
            inbox.append(entry)

    return inbox

def get_sent(sender: str) -> List[Dict[str, str]]:
    """TODO: fill out this docstring (using the load_mail docstring as a guide)
    
    Summary: looks at each mail entry and checks if the sender of that entry matches, if it does, it will
    	add its own list of all the corresponding mail entries that that sender has sent.
    
    Args: (sender: str):  the name/keyword of the sender being searched for

    Returns:
        a list containing all mail entries that the given sender has sent.
        
    """
    mail = load_mail()
    sent = []
    for entry in mail:
        if entry['sender'] == sender:
            sent.append(entry)

    return sent

# API routes - these are the endpoints that the client can use to interact with the server
@app.route('/mail', methods=['POST'])
def add_mail_route():
    """
    Summary: Adds a new mail entry to the json file

    Returns:
        str: The id of the new mail entry
    """
    mail_entry = request.get_json()
    mail_id = add_mail(mail_entry)
    res = jsonify({'id': mail_id})
    res.status_code = 201 # Status code for "created"
    return res

@app.route('/mail/<mail_id>', methods=['DELETE'])
def delete_mail_route(mail_id: str):
    """
    Summary: Deletes a mail entry from the json file

    Args:
        mail_id (str): The id of the mail entry to delete

    Returns:
        bool: True if the mail was deleted, False otherwise
    """
    # TODO: implement this function
    #call delete mail function, with mail_id as the argument 
    res = jsonify(delete_mail(mail_id))
    #return 200 if it worked
    res.status_code = 200 # Status code for "OK"
    return res
    #pass # remove this line

@app.route('/mail/<mail_id>', methods=['GET'])
def get_mail_route(mail_id: str):
    """
    Summary: Gets a mail entry from the json file

    Args:
        mail_id (str): The id of the mail entry to get

    Returns:
        dict: A dictionary representing the mail entry if it exists, None otherwise
    """
    res = jsonify(get_mail(mail_id))
    res.status_code = 200 # Status code for "ok"
    return res

@app.route('/mail/inbox/<recipient>', methods=['GET'])
def get_inbox_route(recipient: str):
    """
    Summary: Gets all mail entries for a recipient from the json file

    Args:
        recipient (str): The recipient of the mail

    Returns:
        list: A list of dictionaries representing the mail entries
    """
    res = jsonify(get_inbox(recipient))
    res.status_code = 200
    return res

# TODO: implement a route to get all mail entries for a sender
# HINT: start with something like this:
#   @app.route('/mail/sent/<sender>', ...)

@app.route('/mail/sent/<sender>', methods=['GET'])
def get_sent_route(sender: str):
    """
    Summary: Gets all mail entries for a sender from the json file

    Args:
        sender (str): The sender of the mail

    Returns:
        list: A list of dictionaries representing the mail entries
    """
    #call get_sent function
    res = jsonify(get_sent(sender))
    res.status_code = 200
    return res



if __name__ == '__main__':
    app.run(port=5000, debug=True)
