# core/command_parser.py
"""Módulo que converte linguagem natural em 'intent' + 'params'.
Implementação simples: placeholder local + instruções comentadas para usar OpenAI.
"""
import json

def interpret_command(command: str):
    """Retorna tuple (intent, params).
    Exemplo de saída: ("report", {"range": "today"})
    Atualmente usa regras simples; substitua pelo client OpenAI se tiver API key.
    """
    cmd = command.lower()
    # Regras simples de demonstração
    if "relatório" in cmd or "relatorio" in cmd or "report" in cmd:
        if "hoje" in cmd:
            return "report", {"range": "today"}
        return "report", {"range": "all"}
    if "enviar email" in cmd or "enviar e-mail" in cmd or "send email" in cmd:
        # tenta extrair destinatário simples (email dentro do texto)
        tokens = cmd.split()
        to = None
        for t in tokens:
            if "@" in t and "." in t:
                to = t
                break
        return "email", {"to": to or "test@example.com", "subject": "Mensagem via AtlasAI", "body": "Automação executada."}
    if "baixar" in cmd or "download" in cmd:
        return "webscrape", {"target": "default"}
    # fallback
    return "noop", {"raw": command}

# Se quiser usar OpenAI, descomente e adapte:
# import openai
# def interpret_command_with_openai(command: str):
#     prompt = f"Interprete o comando e retorne JSON com 'intent' e 'params': {command}"
#     resp = openai.ChatCompletion.create(
#         model="gpt-4o",
#         messages=[{"role":"user","content":prompt}]
#     )
#     text = resp.choices[0].message.content
#     return json.loads(text)
