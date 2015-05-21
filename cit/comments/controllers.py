from flask import Blueprint, session, jsonify, g

from .models import Comment
from ..auth.models import User
from ..db import db
from sqlalchemy import or_

comments_bp = Blueprint('comments', __name__)


@comments_bp.route('/comments/<int:comment_id>/', methods=['DELETE'])
def delete_comment(comment_id):
    comment_query = db.session.query(Comment)
    comment_filtered = comment_query.filter(Comment.id == comment_id)
    has_permission = comment_query.join(User).filter(Comment.author_id == User.id).\
        filter(or_(Comment.author_id == g.user.id, g.user.is_superuser is True))
    if has_permission:
        result = comment_filtered.delete()
        if result:
            db.session.commit()
            return jsonify({'status': 0})
        else:
            db.session.rollback()
            return jsonify({'msg': 'comment not found', 'status': 1})
    else:
        return jsonify({'status': 2}), 405

