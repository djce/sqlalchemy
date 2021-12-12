# from flask import Blueprint
# from flask.templating import render_template
# from flask.views import MethodView
# from flask import jsonify
# from flask import request
# from flask import flash
# from flask import redirect
# from flask import url_for
# from app.models.person import Person
# from ..models import Tag
# from ..models import db
# from ..forms.person import TagForm, PersonForm

# person_bp = Blueprint('person_bp', __name__)

# @person_bp.route('/tag/', methods=['GET','POST'])
# def add_tag():
#     form = TagForm()
#     if form.validate_on_submit():
#         tag = Tag(title=form.title.data)
#         db.session.add(tag)
#         db.session.commit()
#         flash('Your tag has been created!','success')
#         return redirect(url_for('home_bp.index'))
#     return render_template('doki/tag.html',form=form, legend='New Tag')


# def add_

# class TagView(MethodView):

#     def get(self):
#         objs = db.session.query(Tag).order_by('id').all()
#         # session.close()
#         tags = [{
#             'id': obj.id,
#             'title': obj.title,
#             'create_time': obj.create_time,
#             'update_time': obj.update_time
#         } for obj in objs]
#         return jsonify({'code': 200, 'msg': '', 'data': tags})

#     def post(self):
#         tag = Tag(**request.json)
#         db.session.add(tag)
#         db.session.commit()
#         db.session.close()
#         return jsonify({'code': 200, 'msg': 'success'})

# person_bp.add_url_rule('/tag', view_func=TagView.as_view('tag'))
