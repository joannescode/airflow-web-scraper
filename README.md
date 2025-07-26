# 🌀 Airflow Web Scraper - Quotes to Scrape

Este projeto é um exemplo prático criado com o objetivo de aprender e aplicar os conceitos fundamentais do **Apache Airflow** no contexto de **orquestração de tarefas de scraping**.

## 🔍 Sobre o projeto

O projeto automatiza o processo de extração de dados do site [Quotes to Scrape](https://quotes.toscrape.com), uma página criada especificamente para testes de scraping.

### O que o pipeline faz:
1. Descobre dinamicamente todas as páginas disponíveis.
2. Realiza requisições HTTP para cada página.
3. Armazena temporariamente o HTML.
4. Faz o parsing e extração de:
   - Citações
   - Autores
   - Tags associadas
5. Loga os dados extraídos.

Tudo isso é feito utilizando **tarefas pequenas, isoladas e idempotentes**, seguindo as boas práticas de uso do Airflow.

---

## 📚 Objetivo

O foco deste repositório é **estudo prático e domínio do Airflow**:
- Aprender sobre DAGs, tarefas (`@task`), agendamentos (`schedule`), e mapeamento dinâmico de tarefas (`expand()`).
- Entender como organizar um projeto Airflow em um formato limpo e modular.
- Praticar boas práticas como separação de responsabilidades, controle de side-effects e uso adequado do XCom.

---

## 🛠️ Tecnologias utilizadas

- [Apache Airflow](https://airflow.apache.org/)
- Python 3.12+
- requests
- BeautifulSoup4
- Astro CLI (para ambiente local)

---

## 🚀 Como rodar localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/joannescode/airflow-quotes-scraper.git
   cd airflow-quotes-scraper```

2. Suba o ambiente com Astro CLI:
```astro dev start```

3. Acesse o Airflow em http://localhost:8080

