#!/usr/bin/env python3
"""Recalcula o hash de segurança (CSP) do index.html.

Rode sempre que editar qualquer coisa dentro do <script> (por exemplo, trocar o
número do WhatsApp). Sem isso, o navegador bloqueia o script e o formulário não funciona.

Uso:  python3 atualizar-csp.py [caminho-do-html]
"""
import base64, hashlib, re, sys

caminho = sys.argv[1] if len(sys.argv) > 1 else "index.html"
html = open(caminho, encoding="utf-8").read()

scripts = re.findall(r"<script>(.*?)</script>", html, re.S)
if len(scripts) != 1:
    sys.exit("Esperava exatamente um bloco <script> no arquivo.")

novo = base64.b64encode(hashlib.sha256(scripts[0].encode("utf-8")).digest()).decode()
html2, n = re.subn(r"'sha256-[A-Za-z0-9+/=]+'", f"'sha256-{novo}'", html, count=1)
if n != 1:
    sys.exit("Não achei o hash atual na meta Content-Security-Policy.")

open(caminho, "w", encoding="utf-8").write(html2)
print("Hash atualizado:", novo)
