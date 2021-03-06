from flask import Blueprint, jsonify, request
from backend.models.user import User, db, Review
from flask_login import current_user, login_required, login_user
from sqlalchemy.orm import joinedload

user_routes = Blueprint('users', __name__)

@user_routes.route('/', methods=["POST"])
def createUser():
    email, password, firstName, lastName = request.json.values()
    user = User(email=email, password=password,
                first_name=firstName, last_name=lastName)
    db.session.add(user)
    db.session.commit()
    login_user(user)
    return {"current_user_id": current_user.id}


@user_routes.route('/test', methods=["GET"])
def test():
    info = db.session.query(User).first()
    tester = info.safe_user()
    t2 = db.session.query(Review).first()
    print(t2.review_tags)
    return {'t1':tester, 't2':2}
