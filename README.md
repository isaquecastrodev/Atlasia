# AtlasAI - Starter Project
AtlasAI é um starter para um sistema de automação + interpretação por linguagem natural.
Esse scaffold cria uma estrutura modular (core, modules, web) e exemplos de módulos.

## O que tem aqui
- Motor principal (core/engine.py)
- Parser simples (core/command_parser.py) — placeholder para integrar com OpenAI
- Loader dinâmico de módulos (core/module_loader.py)
- Módulos de exemplo: email, report, webscrape, noop
- API mínima em Flask (web/app.py)
- Config em config/settings.json

## Rodando localmente (requisitos)
- Python 3.10+
- criar e ativar um venv:
  ```bash
  python -m venv .venv
  source .venv/bin/activate  # macOS / Linux
  .venv\Scripts\activate    # Windows
  pip install -r requirements.txt
  ```

## Executando
- Rodar REPL:
  ```bash
  python main.py
  ```
- Rodar API Flask:
  ```bash
  python web/app.py
  ```
- Exemplo de request:
  ```bash
  curl -X POST http://localhost:8000/api/execute -H "Content-Type: application/json" -d '{"command":"Enviar email para teste@example.com"}'
  ```

## Próximos passos para deixar "foda pra caralho"
- Integrar `core/command_parser.py` com OpenAI (descomentar e configurar chave)
- Implementar módulos reais (integração SMTP, Google Sheets, PDF generation)
- Adicionar autenticação na API, UI em React com websockets, Dockerfile e CI
- Adicionar exemplos em README e GIFs mostrando execução

## Licença
MIT
