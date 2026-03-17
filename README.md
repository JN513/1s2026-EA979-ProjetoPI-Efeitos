# Projeto de PI - Parte 1 - Fotos e Efeitos

Neste parte do projeto, você irá explorar uma outra aplicação comum para processamento de imagem: edição de imagens. Você deverá utilizar fotos que você tirará pela FEEC, e propor operações/filtros para editá-las.

## Formato de entrega

1. Clone este repositório e crie uma nova branch com seu RA.
2. Realize um pull request quando terminar as tarefas especificadas a seguir.


## Executando o código

Neste repositório você irá encontrar o pacote `unicamp_effects`, onde deverá implementar efeitos para editar fotos. O pacote também possui o entry-point `run_effect` para executar os efeitos que implementar.

1. Instale o pacote na pasta raiz do repositório: `python -m pip install -e .`
   - Observe que o comando instala o pacote no modo editável (opção `-e`), isto significa que qualquer modificação que você fizer nele é diretamente refletida ao utilizar.
2. Execute os efeitos usando o comando na pasta raiz do repositório:
   - `python -m unicamp_effects.run_effect photo\NOME_DA_FOTO.xxx 123456_NOME_DO_EFEITO` (123456 = seu RA)
   - Os resultados são colocados na pasta `photo_result`

Obs: utilize `python` ou `python3` de acordo com seu sistema.


## Tarefas

1. Ande pela FEEC e tire ao menos 15 fotos de locais/cenas/eventos/objetos que julgar interessante.
   - As fotos devem ser colocadas na pasta `photo`
2. Destas fotos, selecione 3 para trabalhar neste momento.
3. Pesquise e pense sobre as operações que você pode realizar nestas fotos. Uma mesma foto pode utilizar uma ou mais operações. Seja criativo. Incluindo algumas que você já estudou e outras, você pode realizar coisas como (você deve implementar ao menos 2 entre as em negrito):
   - **Detecção de borda**
   - **Aberração Cromática**
   - **Operações não lineares (pixelização, distorção radial, twirl)**
   - Quantização
   - Dithering
   - Blur
   - Depth of Field
   - Mapeamento de cores
   - Vinheta
   - Halftoning
4. Responda o formulário disponibilizado no Google Classroom sobre quais efeitos decidiu realizar. 
5. Implemente as operações seguindo as restrições:
   - Você não pode utilizar softwares externos para editar as fotos originais
   - Além da leitura e escrita das imagens, todas as outras operações precisam ser implementadas por você
   - Você deve implementar os efeitos em um arquivo `RA.py` na pasta `src\unicamp_effects\effects`.
     - Utilize como base o arquivo `my_ra`.
     - Cada efeito deve ser implementada por uma função com o nome deste efeito, com a assinatura `EFFECT_NAME(img: np.ndarray) -> np.ndarray:`
     - Todos os efeitos precisam ser registrados com a função `register`, passando como parâmetro o seu RA.
   - As funções devem operar em imagens de 3 canais RGB com dtype `uint8`, e devem retornar imagens com o mesmo shape e dtype. Caso retorne uma imagem monocromática, replique a mesma imagem para os 3 canais.

Dica: pode ser útil implementar o efeito em um notebook antes de transferi-lo para o pacote. 

## Testes

Ao realizar o pull request, serão executados um testes automáticos para verificar se a tarefa foi realiza corretamente:

- Efeitos retornam imagem como `np.ndarray` e não alteram dtype e shape do array.
- Foram registrados 3 efeitos com prefixo contendo um RA válido
- Foram adicionadas 15 fotos na pasta `photo`, todas contendo como prefixo o mesmo RA válido
- Foram adicionadas 3 fotos na pasta `photo_result`, todas contendo como prefixo o mesmo RA válido

Após o prazo de entrega, também verificaremos manualmente se os efeitos de fato foram implementados corretamente e os resultados obtidos.