from flask import Blueprint, render_template
from flask import jsonify,request
from ..models.user import User
from ..extensions import session
from ..forms.user import RegisterForm

user_bp = Blueprint('user', __name__)

@user_bp.route('/')
def index():
    return render_template('index.html')


# @user_bp.route('/register', methods=['GET','POST'])
# def register():

#     form = RegisterForm()

#     if request.method == 'GET':
#         return render_template('admin/register.html', form=form)

#     elif request.method == 'POST':
        
#         payload = request.form

#         if form.validate_on_submit():

#             session.add(User(**{'name': form.name.data}))
#             session.commit()

#         return jsonify({'code':200})


#     return jsonify({'code':200})
