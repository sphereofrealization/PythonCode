import ast
import types
import pathlib


def load_functions():
    path = pathlib.Path(__file__).resolve().parents[1] / 'hexagon_tessellation_games_of_quasi_quanta_topology.py'
    source = path.read_text()
    tree = ast.parse(source, filename=str(path))
    selected = []
    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            selected.append(node)
        elif isinstance(node, ast.FunctionDef) and node.name in {'safe_divide', 'logic_vector'}:
            selected.append(node)
    module = types.ModuleType('extracted')
    code = compile(ast.Module(body=selected, type_ignores=[]), filename=str(path), mode='exec')
    exec(code, module.__dict__)
    return module.safe_divide, module.logic_vector

