from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

# creates a blueprint object of all the routes on the website
routes = Blueprint('routes', __name__)


# ('/') defines the root route after the url
@routes.route('/', methods=['GET', "POST"])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        
        if len(note) < 1:
            flash('Note is too short.', 'error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added.', 'success')
            
    return render_template("home.html", user=current_user)


@routes.route('/delete-notes', methods=['POST'])
def delete_notes():
    # takes json data form the request.data (note to be deleted)
    note = json.load(request.data)
    noteId = note['noteId']  # noteId is the id of the note to be deleted
    note = Note.query.get(noteId)  # check if note exists
    
    # if note exisits and made by the user who created the note, delete it
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            flash('Note deleted.', 'success')
    
    return jsonify({})  # return empty json object