from decimal import Decimal

from sqlalchemy import ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Skin(Base):

  __tablename__ = "skins"

  id:Mapped[int] = mapped_column(Integer,primary_key=True)

  name:Mapped[str] = mapped_column(String,nullable=False)

  price:Mapped[Decimal] = mapped_column(Numeric(precision=10,scale=2),nullable=False)

  listings:Mapped[list["Listing"]] = relationship(back_populates="skin")

  weapon: Mapped[str] = mapped_column(String(50), nullable=False)

  rarity: Mapped[str] = mapped_column(String(30), nullable=False)

  min_float: Mapped[Decimal] = mapped_column(Numeric(4, 3), nullable=False)

  max_float: Mapped[Decimal] = mapped_column(Numeric(4, 3), nullable=False)






class Listing(Base):
    
    __tablename__ = "listings"

    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    
    skin_id:Mapped[int]= mapped_column(ForeignKey("skins.id"),nullable=False)

    listing_price:Mapped[Decimal] = mapped_column(
       Numeric(10,2),nullable=False
    )

    skin:Mapped["Skin"] = relationship(back_populates="listings")




  

