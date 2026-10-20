# Changelog

Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/) e [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [1.4.1] - 2026-10-20

### Adicionado
- Arquivo `CNAME` com o endereço oficial `mei.esidoro.com.br` para o GitHub Pages, e registro DNS correspondente.

## [1.4.0] - 2026-10-20

### Adicionado
- Campo "Seu nome" logo abaixo da senha do Gov.br, para identificar o cliente (não precisa ser o nome completo). Aparece logo depois da senha no resumo.
- Mini tutorial escondido ("Não sabe como fazer? Clique aqui.") ensinando a desligar a verificação em duas etapas: conta do Gov.br, aba Segurança, desativar.

### Alterado
- A senha do Gov.br passa a ficar visível na tela, para o cliente conferir o que digitou.
- Subtítulo do cabeçalho: "Leva menos de um minuto. Responda com calma."
- Na tela final, o número do escritório deixa de ser mostrado. O botão agora é "Enviar para a Contabilidade", com a explicação de que o WhatsApp abre com as informações prontas e basta apertar enviar.

## [1.3.0] - 2026-10-20

### Adicionado
- Opção "Meu RG termina com uma letra (ex.: X)" com campo de uma letra, para RGs que terminam em letra. O campo principal continua só com números (e teclado numérico no celular).
- Arquivo `LICENSE` (todos os direitos reservados) e publicação do projeto no GitHub.

## [1.2.1] - 2026-10-20

### Corrigido
- Bolinhas (Sim/Não) e caixinha da declaração apareciam vazias mesmo selecionadas.
- Estados fora de ordem alfabética; agora em ordem de sigla e com o nome ao lado (ex.: "MG – Minas Gerais").
- Número da identidade aceitava letras; agora só aceita números (letras digitadas são removidas e o aviso fica vermelho).

### Adicionado
- Aviso na tela quando o formulário é aberto sem JavaScript (pré-visualização do iPhone), orientando a abrir o link no Safari ou no Chrome.

## [1.2.0] - 2026-10-20

### Adicionado
- Número de envio do escritório configurado e exibido na tela de revisão, para o cliente conferir o destino.
- Content-Security-Policy na página (só o script do próprio formulário e só a consulta ao ViaCEP) e o script `atualizar-csp.py` para recalcular o hash depois de edições.

### Alterado
- Órgão emissor virou uma lista (SSP, PC, DETRAN, IFP, PF) com a opção "OUTRO / NENHUM DESSES", que libera um campo para digitar.
- O botão do WhatsApp passou a usar o link direto do aplicativo (`whatsapp://`), para o texto não passar por uma URL web.

## [1.1.0] - 2026-10-20

### Adicionado
- Pergunta "caminhoneiro autônomo?" para definir o Regime de Tributação (Geral ou MEI Caminhoneiro).
- Aviso de golpes na tela de envio: cobranças e ofertas por e-mail ou ligação após a abertura do MEI, lembrando que a única guia do MEI é o DAS e orientando a confirmar com a Esidoros.
- Avisos de que o telefone de contato e o e-mail são públicos no cadastro do MEI.

### Alterado
- E-mail passa a ser obrigatório.
- O campo de celular deu lugar ao "Telefone para contato", que é o campo exigido no portal (o celular do Gov.br o portal preenche sozinho).
- Resumo reordenado para seguir a tela do Portal do Empreendedor: identidade, órgão, UF, telefone, e-mail, capital, regime, ocupação, endereços.

### Removido
- Campo "Nome completo" (o portal puxa pelo CPF).

## [1.0.0] - 2026-10-20

Primeira versão.

### Adicionado
- Formulário único em HTML, pensado para o celular, na ordem do Portal do Empreendedor.
- Bloco de acesso com CPF e senha do Gov.br, com aviso para manter a verificação em duas etapas desligada.
- Campos: nome, RG, órgão e UF emissor, celular, e-mail, capital social, atividade, endereço comercial e residencial.
- Busca de endereço por CEP (ViaCEP) com preenchimento manual caso a busca falhe.
- Validação de CPF e máscaras de CPF, celular, CEP e valor.
- Tela de revisão com envio por WhatsApp, cópia de texto e geração de imagem.
- Aviso de privacidade (LGPD) e declaração de desimpedimento com autorização.
