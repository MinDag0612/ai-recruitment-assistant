from abc import ABC, abstractmethod

class ParserCV(ABC):
    @abstractmethod
    def parse(self, file) -> str:
        pass


class FakeParserCV(ParserCV):
    def parse(self, file) -> str:
        return "FAKE PARSE !!"