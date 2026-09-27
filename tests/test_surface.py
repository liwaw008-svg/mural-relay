from pathlib import Path
s=(Path(__file__).parents[1]/'contracts'/'contract.py').read_text()
def test_methods():
 for n in ['permit_mural','paint_next','get_mural','get_critiques_page','get_murals_page','get_summary']:assert f'def {n}' in s
def test_guards():
 for n in ['actor in painters','len(painted)>=int(m.panels)','int(m.fractures)>=3','run_nondet_unsafe']:assert n in s
