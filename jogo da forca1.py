 #Inclusão de Bibliotecas Necessárias
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#Constantes que definem as regras do jogo
#define MAX_TENTATIVAS_FACIL 8
#define MAX_TENTATIVAS_MEDIO 6
#define MAX_TENTATIVAS_DIFICIL 4
#define NUM_PALAVRAS_FACIL 10
#define NUM_PALAVRAS_MEDIO 10
#define NUM_PALAVRAS_DIFICIL 10
#define PONTUACAO_POR_PALAVRA_FACIL 5
#define PONTUACAO_POR_PALAVRA_MEDIO 10
#define PONTUACAO_POR_PALAVRA_DIFICIL 15
#define MAX_JOGADORES 5

# Palavras para cada nível de dificuldade
char *palavrasFacil[NUM_PALAVRAS_FACIL] = {"CASA", "GATO", "AMOR", "PASTA", "FICA", "SEIS", "BOLA", "JOIA", "FIAT", "SAPO"};
char *palavrasMedio[NUM_PALAVRAS_MEDIO] = {"RECEIO", "INSENTO", "PAIXÃO", "REINOS", "CASUAL", "ANSEIO", "APREÇO", "RANCOR", "TETO", "ALENTO"};
char *palavrasDificil[NUM_PALAVRAS_DIFICIL] = {"DEMOCRACIA", "COMPUTADOR", "HIPOTETICO", "DESENVOLVIMENTO", "ALGORITMO", "CACHORRO", "ELEFANTE", "MODALIDADE", "CONSTRUCAO", "ENGENHARIA"};

// Estrutura que representa um jogador
typedef struct {
  char nome[6];  // Limitado a 5 caracteres + 1 para o caractere nulo '\0'
  int pontuacao;
} Jogador;

// Função que pausa a execução por um número de segundos
void esperar(unsigned int segundos) {
  unsigned int tempoFim = time(NULL) + segundos;
  while (time(NULL) < tempoFim)
    ;
}

// Inicializa as letras reveladas para a palavra secreta
void inicializarForca(char *palavraSecreta, char *letrasReveladas) {
  for (int i = 0; i < strlen(palavraSecreta); i++) {
    if (palavraSecreta[i] == ' ')
      letrasReveladas[i] = ' ';
    else
      letrasReveladas[i] = '_';
  }
  letrasReveladas[strlen(palavraSecreta)] = '\0';
}

// Exibe o estado atual do jogo (forca)
void exibirForca(char *letrasReveladas, int tentativas, int maxTentativas) {
  printf("\e[46m\e[0;95m+---------------------------------------------------------------------------------+\n");
  printf("| Palavra: %-12s                                                            |\n", letrasReveladas);
  printf("| Tentativas restantes: %-3d/%-3d                                                    |\n",
         maxTentativas - tentativas, maxTentativas);
  printf("+----------------------------------------------------------------------------------+\n");
}

// Verifica se uma letra está na palavra secreta e a revela
int letraEstaNaPalavra(char letra, char *palavraSecreta, char *letrasReveladas) {
  int encontrada = 0;
  for (int i = 0; i < strlen(palavraSecreta); i++) {
    if (palavraSecreta[i] == letra) {
      letrasReveladas[i] = letra;
      encontrada = 1;
    }
  }
  return encontrada;
}

// Exibe o ranking de jogadores
void exibirRanking(Jogador *ranking, int numJogadores) {
  printf("\e[46m\e[0;95m+-----------------------------------------------------------------------------------+\n");
  printf("|                                       RANKING                                      |\n");
  printf("+------------------------------------------------------------------------------------+\n");
  printf("|   Posição   |                    Nome               |           Pontuação          |\n");
  printf("-------------------------------------------------------------------------------------+\n");
  for (int i = 0; i < numJogadores; i++) {
    printf("|      %-4d   |                   %-8s            |             %-17d|\n", i + 1, ranking[i].nome,
           ranking[i].pontuacao);
  }
  printf("+------------------------------------------------------------------------------------+\n");
}

// Adiciona um novo jogador ao ranking ou atualiza a pontuação se já existir
void adicionarAoRanking(Jogador *ranking, int *numJogadores, Jogador novoJogador) {
  for (int i = 0; i < *numJogadores; i++) {
    if (strcmp(ranking[i].nome, novoJogador.nome) == 0) {
      ranking[i].pontuacao += novoJogador.pontuacao;
      return;
    }
  }

  if (*numJogadores < MAX_JOGADORES) {
    // Adiciona um novo jogador se houver espaço no ranking
    strncpy(ranking[*numJogadores].nome, novoJogador.nome, 5);
    ranking[*numJogadores].nome[5] = '\0';  // Certifica-se de terminar a string
    ranking[*numJogadores].pontuacao = novoJogador.pontuacao;
    (*numJogadores)++;
  } else {
    // Encontra o jogador com a pior pontuação no ranking
    int piorPontuacao = ranking[0].pontuacao;
    int indicePiorJogador = 0;
    for (int i = 1; i < MAX_JOGADORES; i++) {
      if (ranking[i].pontuacao < piorPontuacao) {
        piorPontuacao = ranking[i].pontuacao;
        indicePiorJogador = i;
      }
    }

    // Substitui o pior jogador se a pontuação do novo jogador for melhor
    if (novoJogador.pontuacao > piorPontuacao) {
      strncpy(ranking[indicePiorJogador].nome, novoJogador.nome, 5);
      ranking[indicePiorJogador].nome[5] = '\0';  // Certifica-se de terminar a string
      ranking[indicePiorJogador].pontuacao = novoJogador.pontuacao;
    }
  }
}

// Função principal que controla o fluxo do jogo
int main() {
  srand(time(NULL));

  char palavraSecreta[20];
  char letrasReveladas[20];
  char letra;
  int tentativas;
  int escolhaMenu;
  int maxTentativas;
  int pontuacaoTotal = 0;

  Jogador ranking[MAX_JOGADORES];
  int numJogadores = 0;

  do {
    int ok = system("clear");

    // Exibe o menu principal
    printf("\e[46m\e[0;95m+--------------------------------------------------------------------------------+\n");
    printf("|                                  JOGO DA FORCA                                 |\n");
    printf("+--------------------------------------------------------------------------------+\n");
    printf("\e[46m\e[0;95m+--------------------------------------------------------------------------------+\n");
    printf("|                                    MENU                                        |\n");
    printf("+--------------------------------------------------------------------------------+\n");
    printf("|                                  1 - Novo Jogo                                 |\n");
    printf("|                                  2 - Ranking                                   |\n");
    printf("|                                  3 - Sair                                      |\n");
    printf("+-------------------------------------------------------------------------------+\n");
    printf("Escolha uma opção: \e[0m");
    ok = scanf("%d", &escolhaMenu);

    switch (escolhaMenu) {
    case 1:
      ok = system("clear");

      // Exibe o menu de seleção de dificuldade
      printf("\e[46m\e[0;95m+----------------------------------------------------------------------------------+\n");
      printf("|                                NÍVEIS DE DIFICULDADE                             |\n");
      printf("+----------------------------------------------------------------------------------+\n");
      printf("|                                 1 - Fácil                                        |\n");
      printf("|                                 2 - Médio                                        |\n");
      printf("|                                 3 - Difícil                                      |\n");
      printf("+---------------------------------------------------------------------------------+\n");
      printf("Escolha o nível de dificuldade:\e[0m ");
      int nivel;
      ok = scanf("%d", &nivel);

      switch (nivel) {
      case 1:
        maxTentativas = MAX_TENTATIVAS_FACIL;
        strcpy(palavraSecreta, palavrasFacil[rand() % NUM_PALAVRAS_FACIL]);
        pontuacaoTotal += PONTUACAO_POR_PALAVRA_FACIL;
        break;
      case 2:
        maxTentativas = MAX_TENTATIVAS_MEDIO;
        strcpy(palavraSecreta, palavrasMedio[rand() % NUM_PALAVRAS_MEDIO]);
        pontuacaoTotal += PONTUACAO_POR_PALAVRA_MEDIO;
        break;
      case 3:
        maxTentativas = MAX_TENTATIVAS_DIFICIL;
        strcpy(palavraSecreta, palavrasDificil[rand() % NUM_PALAVRAS_DIFICIL]);
        pontuacaoTotal += PONTUACAO_POR_PALAVRA_DIFICIL;
        break;
      default:
        printf("\e[46m\e[0;95mOpção inválida. Voltando ao menu.\n");
        continue;
      }
      tentativas = 0;
      inicializarForca(palavraSecreta, letrasReveladas);

      // Loop principal do jogo
      while (1) {
        ok = system("clear");

        // Exibe o estado atual do jogo
        exibirForca(letrasReveladas, tentativas, maxTentativas);

        printf("\e[46m\e[0;95mDigite uma letra: ");
        ok = scanf(" %c", &letra);
        getchar();
        letra = toupper(letra);

        // Verifica se a entrada é uma letra válida
        if (!isalpha(letra)) {
          printf("\e[46m\e[0;95mPor favor, digite uma letra válida.\n");
          continue;
        }

        // Verifica se a letra está na palavra e atualiza o estado do jogo
        if (!letraEstaNaPalavra(letra, palavraSecreta, letrasReveladas)) {
          tentativas++;
        }

        // Verifica se o jogador venceu
        if (strcmp(palavraSecreta, letrasReveladas) == 0) {
          ok = system("clear");
          exibirForca(letrasReveladas, tentativas, maxTentativas);
          printf("\e[46m\e[0;95mParabéns! Você acertou a palavra: %s\n", palavraSecreta);

          // Solicita o nome do jogador para o ranking
          Jogador novoJogador;
          printf("\e[46m\e[0;95mDigite seu nome para o ranking (limite de 5 caracteres): ");
          ok = scanf("%5s", novoJogador.nome);
          getchar();  // Limpar o buffer
          novoJogador.pontuacao = pontuacaoTotal;

          // Adiciona o jogador ao ranking
          adicionarAoRanking(ranking, &numJogadores, novoJogador);
          esperar(2);
          break;
        }

        // Verifica se o jogador perdeu
        if (tentativas == maxTentativas) {
          ok = system("clear");
          printf("\e[46m\e[0;95mVocê perdeu! A palavra era: %s\n", palavraSecreta);
          printf("\e[46m\e[0;95mSua pontuação: %d\n", pontuacaoTotal);
          esperar(2);
          break;
        }
      }
      break;
    case 2:
      // Exibe o ranking
      do {
        ok = system("clear");

        // Exibe o ranking de jogadores
        exibirRanking(ranking, numJogadores);

        printf("\e[46m\e[0;95m+------------------------------------------------------------------------------------+\n");
        printf("\e[46m\e[0;95m+------------------------------------------------------------------------------------+\n");
        printf("|                             4 - Voltar ao Menu                                     |\n");
        printf("|                             5 - Sair do Jogo                                       |\n");
        printf("+-----------------------------------------------------------------------------------+\n");
        printf("\e[46m\e[0;95mEscolha uma opção: ");
        ok = scanf("%d", &escolhaMenu);

        if (escolhaMenu == 4) {
          break; // Voltar ao Menu
        } else if (escolhaMenu == 5) {
          printf("\e[46m\e[0;95mSaindo do jogo.\n");
          return 0;
        } else {
          printf("\e[46m\e[0;95mOpção inválida. Tente novamente.\n");
        }
      } while (1);
      break;
    case 3:
      printf("\e[46m\e[0;95mSaindo do jogo.\n");
      break;
    default:
      printf("\e[46m\e[0;95mOpção inválida. Tente novamente.\n");
      break;
    }

  } while (escolhaMenu != 3);

  return 0;
}