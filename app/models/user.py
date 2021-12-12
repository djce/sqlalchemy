from sqlalchemy import Column, String, Integer, Boolean, DateTime
from sqlalchemy import func
from ..extensions import Base

class User(Base):
    __bind_key__ = 'default'
    __tablename__ = 'user'
    id = Column(Integer, autoincrement=True, primary_key=True, comment='用户id')
    username = Column(String(20), unique=True, comment='用户名')
    password_hash = Column(String(128), comment='密码')
    is_active = Column(Boolean, default=True, comment='是否可用')
    last_login = Column(DateTime(timezone=True), nullable=True, comment='最后一次登录时间')
    create_time = Column(DateTime(timezone=True), server_default=func.now(), comment='创建时间')
    update_time = Column(DateTime(timezone=True), server_default=func.now(),
                        onupdate=func.now(),
                        comment='更新时间')

    def to_dict(self):
        return {  c.name: getattr(self, c.name) for c in self.__table__.columns }