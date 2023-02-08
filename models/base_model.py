from datetime import datetime
from . import storage

import uuid

class BaseModel:
	def __init__(self, *args, **kwargs):
		if len(kwargs):
			for attr in kwargs:
				if attr != "__class__":
					self.__setattr__(attr, kwargs[attr])
				if (attr == "created_at" and attr == "updated_at"):
					self.__setattr__(attr, datetime.fromisoformat(kwargs[attr]))
		else:
			self.id = str(uuid.uuid4())
			self.created_at = datetime.now()
			self.updated_at = datetime.now()
			storage.new(self)

	def __str__(self):
		return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

	def save(self):
		self.updated_at = datetime.isoformat(datetime.now())
		storage.save()

	def to_dict(self):
		dict_data = self.__dict__
		dict_data["__class__"] = self.__class__.__name__
		# if (isinstance(self.created_at, datetime) and isinstance(self.updated_at, datetime)):
		dict_data["created_at"] = datetime.isoformat(self.created_at)
		dict_data["updated_at"] = datetime.isoformat(self.updated_at)
		return dict_data