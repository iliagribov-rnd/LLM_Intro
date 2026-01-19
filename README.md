# LLM Homework

Домашние задания по Large Language Models.

## Структура

### 1. llm_architecture.ipynb
**Домашнее задание №1: Архитектура LLM**

- Реализация Byte-level BPE токенизатора
- Имплементация Transformer модели
- Обучение модели на датасете с русскими анекдотами
- Публикация токенизатора и модели на HuggingFace

**Стек:** PyTorch, Datasets, HuggingFace

### 2. llm_alignment.ipynb
**Домашнее задание №2: DPO и PPO**

- Имплементация DPO (Direct Preference Optimization) с нуля
- Обучение PPO (Proximal Policy Optimization) с использованием TRL
- Методы алаймента языковых моделей
- Публикация моделей на HuggingFace

**Стек:** PyTorch, TRL, Datasets, HuggingFace

### 3. lora_peft.ipynb
**PEFT: Parameter-Efficient Fine-Tuning**

- LoRA (Low-Rank Adaptation)
- DoRA 
- QLoRA (Quantized LoRA)
- Эффективное дообучение крупных языковых моделей

**Стек:** PyTorch, PEFT, BitsAndBytes, TRL, Datasets

### 4. llm_rag.ipynb
**RAG: Retrieval-Augmented Generation**

- Извлечение информации из внешних источников
- Генерация ответов на основе извлечённой информации
- Text splitting и chunking
- Векторные базы данных (FAISS)
- Embeddings (HuggingFace)

**Стек:** LangChain, FAISS, HuggingFace Embeddings, Groq, BeautifulSoup

## Требования

```bash
pip install torch datasets transformers trl peft bitsandbytes
pip install langchain-text-splitters langchain-community langchain_huggingface langchain_groq
pip install faiss-cpu groq beautifulsoup4 lxml livelossplot
```

## Использование

Ноутбуки выполняются последовательно в Jupyter/Google Colab.

Требуется HuggingFace API токен для публикации моделей.
