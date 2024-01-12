from datetime import datetime
import uuid
from models import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        # if len(kwargs) != 0 and kwargs is not None:
        #     kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
        #                                              "%Y-%m-%dT%H:%M:%S.%f")
        #     kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
        #                                              "%Y-%m-%dT%H:%M:%S.%f")
        # else:
        #     self.id = str(uuid.uuid4())
        #     self.created_at = datetime.now()
        #     self.updated_at = datetime.now()
        #     storage.new(self)
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        # return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
        #                             self.__dict__)
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
