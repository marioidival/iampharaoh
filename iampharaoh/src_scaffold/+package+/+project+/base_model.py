import re
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import Column, Integer

from zope.sqlalchemy import ZopeTransactionExtension


DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))


class PharaohBase(object):
    """
    Gives PK and table name for future classes
    """

    @declared_attr
    def pk(self):
        return Column(Integer, primary_key=True)

    @declared_attr
    def __tablename__(cls):
        name = cls.__name__.replace('Mixin', '')

        return (
            name[0].lower() +
            re.sub(r'([A-Z])', lambda m: "_" + m.group(0).lower(), name[1:])
        )

Base = declarative_base(cls=PharaohBase)
