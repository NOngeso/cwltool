# Stubs for rdflib.namespace (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional, Text

from rdflib.term import URIRef

class Namespace(str):
    __doc__: Any = ...
    def __new__(cls, value: Any): ...
    @property
    def title(self) -> URIRef: ...
    def term(self, name: Any) -> URIRef: ...
    def __getitem__(self, key: Any, default: Optional[Any] = ...) -> URIRef: ...
    def __getattr__(self, name: Any) -> URIRef: ...

class URIPattern(str):
    __doc__: Any = ...
    def __new__(cls, value: Any): ...
    def __mod__(self, *args: Any, **kwargs: Any): ...
    def format(self, *args: Any, **kwargs: Any): ...

class ClosedNamespace:
    uri: Any = ...
    def __init__(self, uri: Any, terms: Any) -> None: ...
    def term(self, name: Any) -> URIRef: ...
    def __getitem__(self, key: Any, default: Optional[Any] = ...) -> URIRef: ...
    def __getattr__(self, name: Any) -> URIRef: ...

class _RDFNamespace(ClosedNamespace):
    def __init__(self) -> None: ...
    def term(self, name: Any) -> URIRef: ...

RDF = ClosedNamespace("", [])
RDFS = ClosedNamespace("", [])
OWL = Namespace("")
XSD: Namespace
SKOS: Namespace
DOAP: Namespace
FOAF: Namespace
DC: Namespace
DCTERMS: Namespace
VOID: Namespace

class NamespaceManager:
    graph: Any = ...
    def __init__(self, graph: Any) -> None: ...
    def reset(self) -> None: ...
    store: Any = ...
    def qname(self, uri: Any): ...
    def normalizeUri(self, rdfTerm: Any): ...
    def compute_qname(self, uri: Any, generate: bool = ...): ...
    def bind(self, prefix: Any, namespace: Any, override: bool = ..., replace: bool = ...) -> None: ...
    def namespaces(self) -> None: ...
    def absolutize(self, uri: Any, defrag: int = ...): ...

def is_ncname(name: Any): ...

XMLNS: str

def split_uri(uri: Any): ...
