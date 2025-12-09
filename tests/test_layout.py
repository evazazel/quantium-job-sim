import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app

def test_header_present():
    layout = app.layout
    headers = [c for c in layout.children if getattr(c, "type", "") == "H1"]
    assert len(headers) == 1
    assert "Sales data" in headers[0].children

def test_graph_present():
    layout = app.layout
    graphs = [c for c in layout.children if c.__class__.__name__ == "Graph"]
    assert len(graphs) == 1

def test_region_picker_present():
    layout = app.layout
    radio = [c for c in layout.children if c.__class__.__name__ == "RadioItems"]
    assert len(radio) == 1
