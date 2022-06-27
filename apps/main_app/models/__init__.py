import imp
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

"""Models"""

from .patient import patient
from .doctor import doctor
from .diseaseinfo import diseaseinfo
from .consultation import consultation
from .rating_review import rating_review
