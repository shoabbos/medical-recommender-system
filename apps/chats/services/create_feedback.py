from ..models import Feedback


def create_feedback(user, feedback):
    f = Feedback(sender=user, feedback=feedback)
    f.save()
