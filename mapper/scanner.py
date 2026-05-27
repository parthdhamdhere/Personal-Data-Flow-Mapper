import ast
import os
from mapper.patterns import PERSONAL_DATA_KEYWORDS, SINK_KEYWORDS


class DataFlowVisitor(ast.NodeVisitor):
    def __init__(self, filename):
        self.filename = filename
        self.findings = []
        self.personal_vars = set()

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                name = target.id.lower()
                if any(kw in name for kw in PERSONAL_DATA_KEYWORDS):
                    self.personal_vars.add(target.id)
                    self.findings.append({
                        "type": "SOURCE",
                        "variable": target.id,
                        "line": node.lineno,
                        "file": self.filename,
                        "risk": "LOW"
                    })
        self.generic_visit(node)

    def visit_Call(self, node):
        call_str = ast.unparse(node)
        for var in self.personal_vars:
            if var in call_str:
                for sink in SINK_KEYWORDS:
                    if sink in call_str:
                        self.findings.append({
                            "type": "SINK",
                            "variable": var,
                            "sink": sink,
                            "line": node.lineno,
                            "file": self.filename,
                            "code": call_str,
                            "risk": "HIGH"
                        })
        self.generic_visit(node)


def scan_file(filepath):
    try:
        with open(filepath) as f:
            source = f.read()
        tree = ast.parse(source)
        visitor = DataFlowVisitor(filepath)
        visitor.visit(tree)
        return visitor.findings
    except SyntaxError as e:
        print(f"[SKIP] Syntax error in {filepath}: {e}")
        return []


def scan_directory(path):
    all_findings = []
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                all_findings += scan_file(os.path.join(root, file))
    return all_findings
