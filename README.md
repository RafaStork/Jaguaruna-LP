# 321 Modular Jaguaruna — GitHub Pages

Esta pasta contém o site completo: 18 modelos, imagens WebP, plantas, vídeos, fontes, estilos, scripts e bibliotecas já compiladas. Não é necessário instalar Node ou executar npm.

## Publicar

1. Crie um repositório no GitHub. Use `main` como branch principal.
2. Copie **todo o conteúdo desta pasta para a raiz do repositório**, incluindo `.github`, `.nojekyll` e `preparar-pages.py`. O `index.html` deve estar diretamente na raiz. Não envie apenas o ZIP nem coloque tudo dentro de outra pasta.
3. Recomendo usar GitHub Desktop para adicionar e enviar os arquivos, preservando as pastas que começam com ponto.
4. No repositório, abra **Settings > Pages > Build and deployment > Source** e selecione **GitHub Actions**.
5. Abra **Actions > Publicar site no GitHub Pages > Run workflow**. Nas próximas alterações, enviar um commit para `main` publica automaticamente.
6. Quando terminar, abra o endereço informado em **Settings > Pages**.

A publicação configura automaticamente os caminhos para `https://usuario.github.io/repositorio/`, para um site na raiz ou para o domínio personalizado definido no GitHub Pages. Também atualiza canonical, dados estruturados, sitemap e llms.txt, evitando referências ao endereço antigo do site. Não selecione “Deploy from a branch” para este pacote: o workflow precisa preparar os caminhos primeiro.

## Editar conteúdo

Os arquivos HTML já estão prontos. A página inicial é `index.html`; cada modelo está em `chales/<modelo>/index.html`. Imagens e plantas ficam em `assets`, e os vídeos em `videos`. Ao alterar dados de um modelo, mantenha as informações consistentes na página inicial, na página do modelo e nos dados estruturados.

Os preços continuam fictícios. Os contatos continuam direcionados ao Linktree da unidade. Mezaninos contam como quartos. Miniaturas selecionam a foto; o botão “Ampliar fotos” abre o modal.

## Prévia local opcional

Com Python instalado, na pasta execute:

```sh
python preparar-pages.py http://localhost:8000
python -m http.server 8000 --directory _site
```

Abra `http://localhost:8000`. A pasta `_site` deve estar ausente antes de executar novamente o preparo. A prévia exige um servidor HTTP, pois o site usa módulos JavaScript e transições entre páginas.

## Referências

- https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
- https://github.com/actions/starter-workflows/blob/main/pages/static.yml

Pacote exportado em 15/09/2026. O site publicado anteriormente permanece no endereço original; esta pasta é uma cópia independente para sua hospedagem.

## Transições e catálogo

A navegação entre páginas usa um overlay com a marca. Os filtros do catálogo usam Swup Fragment Plugin e substituem apenas os resultados e os controles, preservando a página. As categorias têm endereços próprios em `catalogo/`. Envie também essa pasta e mantenha `preparar-pages.py` atualizado.
