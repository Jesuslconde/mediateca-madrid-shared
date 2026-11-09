from __future__ import annotations

import pytest
from sqlalchemy import create_engine

from mediateca_shared.db import Base
from mediateca_shared.models import Edicion, HarvestJob, SchemaMeta
from mediateca_shared.version import SCHEMA_VERSION, SchemaVersionError, check_schema_version


def test_modelos_se_crean_en_sqlite() -> None:
    engine = create_engine("sqlite+pysqlite:///:memory:")
    Base.metadata.create_all(engine)
    assert "ediciones" in Base.metadata.tables
    assert "harvest_jobs" in Base.metadata.tables
    assert "schema_meta" in Base.metadata.tables


def test_version_compatible() -> None:
    check_schema_version(SCHEMA_VERSION)


def test_version_incompatible() -> None:
    with pytest.raises(SchemaVersionError):
        check_schema_version("999")


def test_modelos_esperados() -> None:
    assert Edicion.__tablename__ == "ediciones"
    assert HarvestJob.__tablename__ == "harvest_jobs"
    assert SchemaMeta.__tablename__ == "schema_meta"
