"""
Import every model here so `Base.metadata.create_all()` in main.py
picks up all tables. If you add a new model file, add its import here.
"""
from app.models.user import User          # noqa: F401
from app.models.form import Form          # noqa: F401
from app.models.field import FormField    # noqa: F401
from app.models.submission import FormSubmission, SubmissionStatusHistory  # noqa: F401
from app.models.permission import FormPermission  # noqa: F401
