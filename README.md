# Formulário de Abertura de MEI – Esidoros

Formulário simples, feito para o celular, que o cliente preenche sozinho para o escritório abrir o MEI. Ele pede só o que o Portal do Empreendedor exige, **na mesma ordem da tela do portal**, e devolve tudo pronto para enviar pelo WhatsApp (texto ou imagem).

Não tem servidor, banco de dados nem cadastro: tudo acontece no celular do cliente.

Criado por Victor Eduardo ([@victoresidoro](https://github.com/VictorEsidoro)).

## Como colocar para funcionar (passo a passo para não programadores)

**Passo 1 – Confira o número do escritório.**
O número que recebe os dados já vem configurado no arquivo (`WHATSAPP_NUMBER`). Se um dia precisar trocar, edite o número e depois rode `python3 atualizar-csp.py`.

> ⚠️ Sem rodar o `atualizar-csp.py` depois de qualquer edição no script, o navegador bloqueia a página e o formulário não funciona.

**Passo 2 – Coloque o arquivo online.**
O cliente precisa de um link para abrir no navegador do celular. Mandar o arquivo `.html` direto pelo WhatsApp **não funciona no iPhone**: ele abre numa pré-visualização sem JavaScript e o formulário aparece quebrado. A Esidoros publica o `index.html` pelo GitHub Pages (no repositório: Settings → Pages → branch `main`, pasta raiz). O link aparece nessa mesma tela, sempre com `https://`.

> ⚠️ Nada de dados reais de clientes no repositório. O arquivo contém só o formulário vazio.

> ⚠️ Proteja o acesso a quem pode editar o arquivo (senha forte e verificação em duas etapas na conta do GitHub). Quem editar o arquivo pode trocar o número de destino.

**Passo 3 – Mande o link ao cliente.**
Ele preenche, confere, e envia pelo WhatsApp ou salva a imagem.

## Conhecendo o sistema

| Parte | O que é |
|---|---|
| Topo | Logo, título, CPF, senha do Gov.br (visível, para o cliente conferir), nome (só para identificar o cliente) e o aviso para deixar a verificação em duas etapas desligada, com um mini tutorial de como desligar |
| Seus dados | RG (só números; se terminar com letra, o cliente marca uma opção e digita a letra), órgão e UF emissor, telefone para contato, e-mail (obrigatório), capital social (opcional) |
| Seu negócio | Pergunta se é caminhoneiro autônomo (regime Geral ou MEI Caminhoneiro) e um campo livre: "o que você faz ou vende?" (a atividade/CNAE é definida pelo escritório) |
| Endereço | CEP com busca automática (ViaCEP); o cliente só confere e digita o número |
| Envio | O botão verde abre o WhatsApp já com o texto, para o número do escritório (o número não aparece na tela). Também dá para salvar como imagem ou copiar o texto |
| Revisão | Tela de conferência na ordem do portal, com o aviso sobre golpes e os botões de envio |
| Não é pedido | Tudo que o portal preenche sozinho (data de nascimento, sexo, nome da mãe, celular do Gov.br, logradouro, bairro, município) |

## Como usar (do lado do escritório)

1. O cliente envia o texto (ou a imagem) pelo WhatsApp.
2. Cada linha chega na ordem da tela do portal: é só copiar e colar campo a campo.
3. Depois da abertura do MEI, apague a mensagem e os arquivos recebidos (LGPD).

## Problemas comuns

| Problema | O que fazer |
|---|---|
| Endereço não aparece depois do CEP | Sem internet ou CEP não encontrado. O formulário libera campos para o cliente digitar rua, bairro e cidade |
| Botão de imagem só baixa o arquivo | O celular não permite compartilhar direto. A imagem fica na galeria; basta anexar no WhatsApp |
| O botão verde do WhatsApp não abre nada | O celular não tem o aplicativo ou bloqueou o link. Use "Salvar / compartilhar como imagem" ou "Copiar texto" |
| No iPhone o formulário aparece quebrado ou só com títulos | O arquivo foi aberto direto pelo WhatsApp. Envie o link do formulário hospedado e peça para abrir no Safari ou no Chrome |
| CPF "inválido" | O número foi digitado errado (o formulário confere os dígitos verificadores) |

## Configuração

| Item | Onde | Observação |
|---|---|---|
| Número do WhatsApp | `WHATSAPP_NUMBER`, no início do `<script>` | Só dígitos, com 55 + DDD. Depois de trocar, rode `python3 atualizar-csp.py` |

## Para desenvolvedores

- Arquivo único: HTML + CSS + JS puro, sem dependências nem build. A logo está embutida em base64.
- Única chamada externa: `https://viacep.com.br/ws/{cep}/json/`, feita do navegador do cliente. Se falhar, entra o preenchimento manual.
- A imagem é desenhada em `<canvas>` e compartilhada com a Web Share API (com download como alternativa).
- A logo tem texto branco: ela só aparece bem sobre fundo escuro (por isso o cabeçalho escuro).
- Nenhum dado é gravado (sem `localStorage`, sem cookies).
- Todo o formulário depende de JavaScript. Sem ele (pré-visualização do iOS), um aviso `<noscript>` pede para abrir o link no navegador.
- Caixinhas e bolinhas usam `appearance:none` com desenho próprio (`::before`), para aparecerem marcadas de forma igual no Android e no iPhone.
- O botão do WhatsApp usa `whatsapp://send` (link direto do app) em vez de `https://wa.me`, para o texto (que inclui a senha) não trafegar numa URL web.
- Segurança: a página traz uma Content-Security-Policy (meta) que só aceita o próprio script (por hash) e só permite conexão com `viacep.com.br`. Qualquer edição no `<script>` exige `python3 atualizar-csp.py`.
- O GitHub Pages não permite cabeçalhos HTTP personalizados, então a proteção contra o formulário ser colocado dentro de outra página (`frame-ancestors`) não está ativa. Se isso for importante, hospedagens como Cloudflare Pages ou Netlify aceitam esses cabeçalhos.

## Licença

Todos os direitos reservados. Veja o arquivo `LICENSE`. O código é público apenas para visualização; não é permitido copiar ou reutilizar.
