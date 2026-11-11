# Changelog

Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/) e [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [1.9.2] - 2026-11-11

### Adicionado
- Rodapé com direitos autorais da Esidoros (© 2026, CRCMG 17567), aviso de reprodução proibida (Lei nº 9.610/1998) e o número da versão. Aparece só na página; não vai na mensagem enviada ao escritório.

## [1.9.1] - 2026-11-11

### Alterado
- O aviso de conta Bronze agora usa o texto real do e-CAC (código 88008: "sua conta gov.br deve possuir nível de confiabilidade Prata ou Ouro"), tanto na opção de resultado quanto no painel de ajuda. O painel ganhou uma imagem do aviso destacado em vermelho, para o cliente reconhecer a tela.

## [1.9.0] - 2026-11-11

### Adicionado
- **Teste final de acesso ao e-CAC**, nos dois modos (abrir e alterar), entre a confirmação da verificação em duas etapas e a autorização. O cliente abre o e-CAC (`cav.receita.fazenda.gov.br`) numa aba nova, toca em "Entrar com gov.br", digita CPF e senha e marca o que apareceu. O e-CAC só abre com senha correta, conta Prata ou Ouro e verificação em duas etapas desligada, então o teste confere as três coisas. A senha nunca passa pelo formulário nem por servidor: quem entra é o próprio cliente, no site oficial.
- Tutorial ilustrado com 4 imagens embutidas (funcionam sem internet): seta vermelha enorme no "Entrar com gov.br", CPF e Continuar destacados, tela do e-CAC aberta ("deu certo", dados do titular cobertos) e o aviso "Usuário e/ou senha inválidos".
- Cinco opções de resultado, sem nenhuma marcada de início: abriu (libera o envio); senha inválida, conta Bronze e pediu código (bloqueiam o envio, cada uma com a explicação de como corrigir, com tutorial completo de como subir o nível da conta: app gov.br, "Aumentar nível", Caminho A por reconhecimento facial com a CNH e Caminho B por internet banking, como conferir o selo e o que fazer se o rosto falhar; passos conferidos na página oficial do Gov.br e iguais no Android e no iPhone); e "outra coisa / não consegui testar" (libera, mas avisa o escritório).
- A mensagem para o escritório traz a linha "Teste de acesso ao e-CAC pelo Gov.br" com o resultado informado.

### Observação
- O resultado é informado pelo próprio cliente: o formulário não consegue (nem deve) logar no Gov.br por ele. Se o Gov.br ou o e-CAC mudarem textos, botões ou o aviso de conta Bronze, os textos do tutorial precisam ser revisados.

## [1.8.0] - 2026-11-07

### Adicionado
- Aviso final em destaque (vermelho) pedindo para desligar a verificação em duas etapas do Gov.br, com caixinha obrigatória: "Conferi e confirmo que a verificação em duas etapas do meu Gov.br está DESLIGADA. Estou ciente de que, com ela ligada, o serviço não poderá ser executado." Fica junto da autorização, no fim do formulário, nos dois modos (abrir e alterar). Sem marcar, o formulário não avança.
- A confirmação vai na mensagem para o escritório ("Verificação em duas etapas do Gov.br: Cliente confirmou que está DESLIGADA"), como registro.

### Alterado
- O passo a passo (no aviso final e no "Não sabe como fazer?" do topo) agora é pelo **aplicativo do Gov.br**: Segurança da conta > Verificação em duas etapas > Desabilitar, com a conferência (aparece a opção "Habilitar") e o alerta de não desinstalar o app nem trocar de celular com a verificação ligada. Antes dizia só "entre na sua conta e toque em Segurança".
- O aviso do topo fala em "até terminarmos o serviço" (valia só para abertura) e avisa que a confirmação é no fim.

### Observação
- Caminho no app conferido na página oficial do Governo Digital (gov.br): aplicativo gov.br > Segurança da conta > Verificação em duas etapas > Desabilitar. Os nomes podem mudar se o app for atualizado.

## [1.7.0] - 2026-11-06

### Adicionado
- Conferência da senha do Gov.br (nos dois modos): se a senha digitada não tem 8 ou mais caracteres, letra maiúscula, letra minúscula, número e símbolo, ou se tem espaço (no começo, no fim ou no meio), aparece um aviso amarelo dizendo o que falta e pedindo para a pessoa conferir. Para seguir, ela marca a caixinha "Conferi a senha e ela está certa mesmo assim". É só um aviso: com a caixinha marcada, o envio segue normalmente.
- Quando a senha não bate com o padrão, a mensagem enviada ao escritório traz a linha "Aviso sobre a senha", dizendo que o cliente confirmou e o que foi diferente do padrão (ex.: "tem espaço no fim"), para o escritório digitar exatamente como veio.

### Alterado
- A senha deixa de ser "cortada" (trim): espaços no começo e no fim agora são preservados, porque o espaço também é caractere da senha.

### Observação
- O padrão (8+ caracteres, maiúscula, minúscula, número e símbolo) foi tirado de um tutorial de universidade sobre a conta Gov.br, não da página oficial; por isso é só aviso, nunca bloqueio. Não há limite máximo nem lista de símbolos validada.
- Confirmado pelo Victor: deixar de ser caminhoneiro autônomo pode ser pedido em qualquer época; só **passar a ser** é restrito a janeiro. A regra do formulário já funciona assim.

## [1.6.0] - 2026-11-06

### Adicionado
- Trava de data para **passar a ser caminhoneiro autônomo** no modo alterar: esse pedido só pode ser feito em janeiro. Fora de janeiro (pelo relógio do celular), o formulário mostra um aviso em vermelho, não deixa enviar com essa opção marcada e orienta a marcar "Não quero mudar" para enviar o resto. Abrir um MEI de caminhoneiro continua liberado o ano todo.
- Botão **Criar lembrete no meu celular**: baixa um arquivo de agenda (.ics) com alarme às 9h do primeiro dia útil de janeiro do ano seguinte (a partir do dia 2, pulando fim de semana). No iPhone abre o menu de compartilhar. O aviso também escreve a data por extenso, para o cliente anotar se o lembrete não abrir.
- Avisos em vermelho e em maiúsculas no modo alterar ("PREENCHA SOMENTE O QUE QUER ALTERAR... DEIXE VAZIO E VÁ PARA O PRÓXIMO CAMPO") no topo e no início de cada bloco, e também dentro dos campos opcionais (texto do próprio campo: "NÃO VAI ALTERAR? DEIXE VAZIO").

### Alterado
- No modo alterar, o bloco "Seus dados" começa pelo telefone: RG, órgão emissor e UF emissor não aparecem (o RG de quem já tem MEI está no cadastro e não muda). Mesmo que o cliente tenha preenchido antes no modo abrir, esses dados não vão na mensagem de alteração.

### Observação
- A trava de janeiro vale só para "passar a ser" caminhoneiro (regra confirmada em material do Sebrae). Para "deixar de ser" caminhoneiro não há trava, pois a regra de prazo não foi confirmada.

## [1.5.0] - 2026-11-06

### Adicionado
- Pergunta logo no início: "O que você precisa?" com as opções **Abrir um MEI novo** e **Alterar dados do meu MEI**. O formulário só aparece depois da escolha.
- Modo **alterar dados**: só CPF, senha do Gov.br, nome e a autorização são obrigatórios. Todo o resto é opcional e só o que foi preenchido vai na mensagem, na imagem e no texto copiado. Quem só quer trocar o endereço não precisa informar atividade, RG etc.
- No modo alterar: o formulário exige pelo menos uma alteração; o que for preenchido é conferido (telefone, e-mail, RG, órgão); endereço preenchido pede CEP e número; perguntas próprias para regime ("não quero mudar" / passar a ser / deixar de ser caminhoneiro) e moradia ("não mudou" / mudou, igual ao negócio / mudou, outro endereço); campo opcional de recado para outras alterações.
- Mensagem, imagem e arquivo de imagem com título próprio ("ALTERAÇÃO DE DADOS DO MEI").

### Alterado
- Título da página e do cabeçalho: "MEI: abertura e alteração de dados".
- Aviso de privacidade fala em "atender o seu pedido". O aviso de golpes pós-abertura aparece só no modo abrir.
- O modo **abrir** continua igual: todos os campos obrigatórios seguem obrigatórios.

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
