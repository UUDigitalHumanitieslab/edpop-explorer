from rdflib import URIRef
from edpop_explorer import Record, SRUReader


class BibliopolisReader(SRUReader):
    sru_url = 'http://jsru.kb.nl/sru/sru'
    sru_version = '1.2'
    HPB_LINK = 'http://hpb.cerl.org/record/{}'
    CATALOG_URIREF = URIRef(
        'https://edpop.hum.uu.nl/readers/bibliopolis'
    )
    IRI_PREFIX = "https://edpop.hum.uu.nl/readers/bibliopolis/"

    def __init__(self):
        super().__init__()
        self.additional_params = {
            'x-collection': 'Bibliopolis'
        }

    def _convert_record(self, sruthirecord: dict) -> Record:
        record = Record(from_reader=self.__class__)
        record.data = sruthirecord
        # TODO: extract fields
        return record

    @classmethod
    def transform_query(cls, query: str) -> str:
        return query
