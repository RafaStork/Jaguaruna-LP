# Como aparecer no Google

Domínio oficial: https://jaguaruna.321modular.com.br/

## 1. Publicar estes arquivos

Envie o conteúdo atualizado desta pasta ao repositório, incluindo `.github`, `CNAME`, `preparar-pages.py`, as páginas HTML e os arquivos de SEO. Aguarde o workflow concluir. Em Settings > Pages, mantenha o domínio personalizado `jaguaruna.321modular.com.br` e HTTPS habilitado. O workflow usa este domínio como URL oficial.

Foram atualizados canonical (endereço preferido de cada página), Open Graph, dados estruturados de empresa e modelos, sitemap, robots.txt e llms.txt. O sitemap contém a página inicial e os 18 modelos. As páginas de categoria possuem títulos, descrições e endereços canônicos próprios e fazem parte do sitemap. A página 404 tem noindex.

## 2. Verificar no Google Search Console

Abra https://search.google.com/search-console/ e adicione uma propriedade do tipo **Prefixo do URL** com `https://jaguaruna.321modular.com.br/`.

Selecione **Arquivo HTML**, baixe o arquivo de verificação fornecido pelo Google e coloque-o na raiz do repositório, ao lado do index.html, sem alterar nome ou conteúdo. O script de publicação foi ajustado para incluir arquivos `google...html`. Publique novamente, confirme que o arquivo abre no endereço informado pelo Google e clique em Verificar. Mantenha o arquivo no repositório nas próximas atualizações.

Se você já tem acesso ao DNS, outra opção é uma propriedade de domínio e a verificação pelo registro TXT fornecido pelo Search Console. Use exatamente os dados que o Google indicar; não substitua registros existentes.

## 3. Enviar o sitemap

Abra **Sitemaps** no Search Console e envie `sitemap.xml`.
URL completa: https://jaguaruna.321modular.com.br/sitemap.xml

Após publicar, esse arquivo deve abrir sem login, bloqueio ou erro. O robots.txt deve apontar para esse mesmo sitemap.

## 4. Solicitar indexação

Em **Inspeção de URL**, informe a página inicial. Use **Testar URL publicada** e, se ela estiver acessível e indexável, clique em **Solicitar indexação**. Faça o mesmo com algumas páginas principais dos modelos; o sitemap ajuda o Google a descobrir as demais.

Acompanhe **Indexação > Páginas** e **Desempenho** nos dias seguintes. Não é necessário repetir a solicitação diariamente. O Google informa que o rastreamento pode levar de dias a semanas; solicitar não garante indexação nem uma posição específica.

## 5. Fortalecer a presença local

No Perfil da Empresa no Google de 321 Modular Jaguaruna, use o domínio oficial como site. Mantenha endereço, categoria, contatos e horários reais atualizados. Publique fotos reais da unidade e das montagens, e peça avaliações honestas a clientes, sem oferecer recompensa. Responda às avaliações.

Inclua o endereço do site no Instagram, Linktree e, se a franqueadora permitir, na página oficial de unidades da rede. Amplie o conteúdo com informações reais sobre montagem, entrega, materiais, projetos executados e dúvidas dos compradores. Não crie páginas repetidas para cidades sem conteúdo útil específico. Substitua os preços fictícios antes de tratá-los como ofertas.

## Limite desta verificação

As verificações locais dos arquivos passaram. A consulta externa automatizada realizada neste ambiente recebeu HTTP 403 para o domínio, robots.txt e sitemap. Isso pode ser uma restrição ao ambiente de consulta; não comprova bloqueio ao Googlebot. O teste de URL publicada do Search Console é a verificação indicada. Caso ele também receba 403, corrija as regras de acesso na hospedagem/CDN antes de solicitar indexação.

O arquivo llms.txt é complementar e não substitui o sitemap nem garante presença em respostas de IA. Não há pagamento ao Google para melhorar a posição orgânica.

## Fontes oficiais

- Verificação: https://support.google.com/webmasters/answer/9008080?hl=pt-BR
- Sitemap: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
- Solicitar indexação: https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl
- Pesquisa local: https://support.google.com/business/answer/7091?hl=pt-BR
