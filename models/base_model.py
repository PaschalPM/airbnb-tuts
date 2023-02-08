from datetime import datetime
import uuid

class BaseModel:
	def __init__(self):
		self.id = str(uuid.uuid4())
		self.created_at = datetime.now()
		self.updated_at = datetime.now()

	def __str__(self):
		return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

	def save(self):
		self.updated_at = datetime.now()

	def to_dict(self):
		dict_data = self.__dict__
		dict_data["__class__"] = self.__class__.__name__
		dict_data["created_at"] = datetime.isoformat(self.created_at)
		dict_data["updated_at"] = datetime.isoformat(self.updated_at)
		return dict_data