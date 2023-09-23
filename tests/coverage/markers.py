import pytest
from _pytest.mark import MarkDecorator

unit: MarkDecorator = pytest.mark.unit
smoke: MarkDecorator = pytest.mark.smoke
sanity: MarkDecorator = pytest.mark.sanity
regression : MarkDecorator = pytest.mark.regression
