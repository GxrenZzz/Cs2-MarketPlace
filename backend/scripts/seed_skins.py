from pathlib import Path
import json
from decimal import Decimal 

from sqlalchemy.dialects.postgresql import insert
from app.modules.skins.models import Skin
from app.database import SessionLocal

base_dir = Path(__file__).resolve().parent.parent

file_path = base_dir / "data" / "sample" / "skins.json"

def decimal_parse(obj):
  decimal_field = {"price","min_float","max_float"}

  for key , value in obj.items():
    if key in decimal_field:
      obj[key] = Decimal(value)

  return obj

data = json.loads(file_path.read_text(encoding="utf-8"),object_hook=decimal_parse)


assert len(data) == 30 

for skin in data:
  assert isinstance(skin["price"], Decimal), "Invalid price type"
  assert isinstance(skin["min_float"], Decimal) ,"Invalid Float Range"
  assert isinstance(skin["max_float"], Decimal) ,"Invalid Float Range"
  assert skin["price"] >= 0 
  assert 0 <= skin["min_float"] <= 1
  assert 0 <= skin["max_float"] <= 1
  assert skin["min_float"] <= skin["max_float"], "Invalid float range"



# bulk insertion 

with SessionLocal() as session:
  stmt = insert(Skin).values(data).on_conflict_do_nothing(index_elements=["name","weapon"])
  session.execute(stmt)
  session.commit()




