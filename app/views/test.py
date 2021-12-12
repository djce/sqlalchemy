from flask import Blueprint
from flask import jsonify
from datetime import datetime

from ..models.user import User
from ..extensions import session

current_time = datetime.now().__format__('%Y-%m-%d %H:%M:%S')

test_bp = Blueprint('test', __name__)

@test_bp.route('/user', methods=['GET'])
def test():
    users = session.query(User).all()
    data = [ user.to_dict() for user in users if user is not None ]
    return jsonify({'code': 200,'msg': 'success', 'data':data})