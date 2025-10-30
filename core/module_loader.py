# core/module_loader.py
"""Carrega dinamicamente módulos da pasta modules e executa a função run(params)."""
import importlib
import core.logger as logger_mod

logger = logger_mod.get_logger(__name__)

def execute_module(intent, params):
    try:
        module = importlib.import_module(f"modules.{intent}_module")
        if hasattr(module, 'run'):
            return module.run(params)
        return {"status": "error", "message": "module has no run()"}
    except ModuleNotFoundError:
        logger.error(f"Módulo não encontrado para intent: {intent}")
        return {"status": "error", "message": "module not found"}
    except Exception as e:
        logger.exception("Erro ao executar módulo")
        return {"status": "error", "message": str(e)}
