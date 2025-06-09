import networkx as nx
import pytest

from .util_loader import load_functions

safe_divide, logic_vector = load_functions()


def test_safe_divide_normal():
    assert safe_divide(10, 2) == 5


def test_safe_divide_near_zero():
    assert safe_divide(1, 1e-12) == 0


def test_logic_vector_returns_value():
    G = nx.DiGraph()
    G.add_node("phi_eq_psi", value=0.42)
    assert logic_vector(G, "phi_eq_psi") == pytest.approx(0.42)
