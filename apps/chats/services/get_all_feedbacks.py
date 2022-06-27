from ..models import Feedback

def get_all_feedbacks():
    _objects = Feedback.objects.all()
    return _objects
