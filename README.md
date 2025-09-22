# Sistema de Estoque (Python + Flet)

Aplicativo de controle de estoque com foco em arquitetura simples, i18n e UX fluida. A navegação usa um “shell” principal (Main View) com Sidebar; o conteúdo central é trocado dinamicamente sem mudar de rota para a maior parte das ações.

## Recursos
- Shell principal com Sidebar (NavigationRail) e conteúdo dinâmico
- Internacionalização (pt/en) via `lib/utils/label_keys.py` e `lib/utils/labels.py`
- Temas (ThemeManager) e troca de logo por tema
- Rotas centralizadas (`lib/src/core/routes.py`) e `PageManager` com `event.route`
- Páginas de exemplo: Welcome, Products e Clients
- Clients: grade responsiva (Nx3) via `ResponsiveRow` e cartões com avatar
- Otimizações de performance em UI: cache de imagens (arquivo/base64), reuso de controles e resize sem reconstrução

## Estrutura
```
config.ini
main.py
lib/
  app.py
  src/
    app/
      styles/
      views/
        pages/            # welcome.py, products.py, etc.
        widgets/          # side_bar.py, text_field.py, etc.
    core/
      page_manager.py
      routes.py
    config/
      app_config.py
  utils/
    label_keys.py
    labels.py
assets/
  images/
storage/
  data/
  temp/
docs/
  DOCUMENTACAO_PROJETO.md
  Projeto-Sistema-de-Estoque.pdf
tools/
  md_to_pdf.py
```

## Executando
- Via CLI do Flet:
```powershell
flet run
```
- Via Python:
```powershell
python .\main.py
```

## Documentação
- Markdown: `docs/DOCUMENTACAO_PROJETO.md`
- PDF: `docs/Projeto-Sistema-de-Estoque.pdf`
- Regenerar PDF:
```powershell
python .\tools\md_to_pdf.py
```

## Notas de UI (Flet)
- Para ocupar todo o espaço: use `Row(vertical_alignment=STRETCH)`, `Column(expand=True, horizontal_alignment=STRETCH)` e `Expanded`/`expand=True` em containers internos
- Para tabelas: envolva `DataTable` em `ListView(expand=True)` para preencher e permitir scroll
- Para grades de cartões: use `ResponsiveRow` com `columns=12` e defina `col` em cada card (ex.: `{xs:12, md:6, lg:4}`), evitando reconstruções no `on_resized`
- Evite recriar `content` durante resize/hover; altere apenas propriedades animáveis (ex.: `scale`) e chame `update()` no próprio controle
- Em imagens, prefira cache local (arquivo) ou `src_base64` calculado uma única vez por card

## Próximos passos
- Controladores por domínio (ex.: Produtos/Clientes)
- CRUD real com backend/armazenamento
- Linter/formatador (ruff/black) e testes automatizados
- Telemetria simples de performance (tempo de render/carga e memória durante animações)
