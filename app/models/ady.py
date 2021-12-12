from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy import func
from ..extensions import Base

class Girl(Base):
    __tablename__ = 'tbl_ady_info'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    avatar = Column(String(100))
    create_time = Column(DateTime(timezone=True), server_default=func.now())
    update_time = Column(DateTime(timezone=True), server_default=func.now(),server_onupdate=func.now())

    def to_dict(self):
        return {  c.name: getattr(self, c.name) for c in self.__table__.columns }