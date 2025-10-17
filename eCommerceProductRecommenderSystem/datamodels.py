# models.py
class Product:
    id: int
    name: str
    category: str

class UserInteraction:
    user_id: int
    product_id: int
    action: str # view, purchase, etc.