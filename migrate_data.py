import json

# Carregar dados recuperados
with open('/home/ubuntu/Downloads/sistema-mamae-default-rtdb-export.json', 'r') as f:
    data = json.load(f)

# Extrair lançamentos e converter para lista
lancamentos_dict = data.get('lancamentos', {})
lancamentos_list = []
for key, val in lancamentos_dict.items():
    val['id'] = key
    lancamentos_list.append(val)

# Extrair sócios
socios = data.get('config', {}).get('socios', ["Sócio 1", "Sócio 2", "Sócio 3", "Sócio 4"])

# Ler o HTML atual
with open('/home/ubuntu/sistema_permanente/index.html', 'r') as f:
    html = f.read()

# Injetar os dados no script de inicialização
# Procurar por let lancamentos = []; e substituir
data_js = f"let lancamentos = {json.dumps(lancamentos_list)};\n    let socios = {json.dumps(socios)};"
html = html.replace("let lancamentos = [];", data_js)

# Salvar o novo HTML
with open('/home/ubuntu/sistema_permanente/index.html', 'w') as f:
    f.write(html)

print("Dados migrados com sucesso!")
