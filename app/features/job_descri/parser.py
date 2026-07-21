from abc import ABC, abstractmethod

class ParserJD(ABC):
    @abstractmethod
    def parse(self, file) -> str:
        pass


class FakeParserJD(ParserJD):
    def parse(self, file) -> str:
        return "FAKE PARSE !!"