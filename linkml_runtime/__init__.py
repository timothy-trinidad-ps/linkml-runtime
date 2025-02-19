from pathlib import Path
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.schemaview import SchemaView
from rdflib import RDF, RDFS, SKOS, XSD, OWL

# use importlib.metadata to read the version provided
# by the package during installation. Do not hardcode
# the version in the code
import importlib.metadata as importlib_metadata

LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
TCCM = CurieNamespace('tccm', 'https://ontologies.r.us/tccm/')
OWL = CurieNamespace('owl', OWL)
RDF = CurieNamespace('rdf', RDF)
RDFS = CurieNamespace('rdfs', RDFS)
SKOS = CurieNamespace('skos', SKOS)
XSD = CurieNamespace('xsd', XSD)

__version__ = importlib_metadata.version(__name__)


THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH / "linkml_model" / "model" / "schema"

MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "meta.yaml"


class MappingError(ValueError):
    """
    An error when mapping elements of a LinkML model to runtime objects
    """
    pass

class DataNotFoundError(ValueError):
    """
    An error in which data cannot be found
    """
    pass
