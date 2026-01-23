import json
import os

def fix_notebook(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Удаляем widgets из metadata
    if 'metadata' in notebook and 'widgets' in notebook['metadata']:
        del notebook['metadata']['widgets']
        print(f"Удалены metadata.widgets из {notebook_path}")
    
    # Сохраняем
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)

# Использование
fix_notebook("llm_rag.ipynb")
fix_notebook("llm_alignment.ipynb")
fix_notebook("llm_peft.ipynb")
fix_notebook("llm_architecture.ipynb")