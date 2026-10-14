from app.models.infor_extracted import InforExtractedBase
from app.features.processor.model import Model


class LocalModel(Model):
    def extract(self, text: str) -> InforExtractedBase:
        return InforExtractedBase()

