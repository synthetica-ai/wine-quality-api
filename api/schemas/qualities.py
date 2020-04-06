from ma import ma
from models.qualities import Qualities

class QualitiesSchema(ma.ModelSchema):
    class Meta:
        model=Qualities
        dump_only=("id",)
        ordered=True
