from wq.db import rest
from .models import Category


rest.router.register_model(
    Category,
    fields="__all__",
)
