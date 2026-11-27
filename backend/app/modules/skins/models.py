from decimal import Decimal

from sqlalchemy import ForeignKey, Integer, Numeric, String , CheckConstraint , UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

# ck - check constraints
# uq - unique constraint
# pk - primary key 



class Skin(Base):

  __tablename__ = "skins"

  __table_args__ = (
     UniqueConstraint("name","weapon" , name= "uq_skin_name_weapon"),
     CheckConstraint("price >= 0 ",name="ck_skin_price"),
     CheckConstraint("min_float BETWEEN 0 AND 1",name="ck_skin_min_float"),
     CheckConstraint("max_float BETWEEN 0 AND 1",name="ck_skin_max_float"),
     CheckConstraint("min_float <= max_float",name="ck_skin_float_range")
  )

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

    __table_args__ = (
       CheckConstraint("listing_price >=0",name="ck_listing_price"),
    )

    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    
    skin_id:Mapped[int]= mapped_column(ForeignKey("skins.id"),nullable=False)

    listing_price:Mapped[Decimal] = mapped_column(
       Numeric(10,2),nullable=False
    )

    skin:Mapped["Skin"] = relationship(back_populates="listings")




  

