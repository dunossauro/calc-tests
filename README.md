# Quanto valem seus testes?

Repositório exclusivo da palestra.


Tópicos abordados:
- O cliente e sua [estória](./estorias)
- Desenvolvimento:
    - [TDD](./code)
- Testes:
    - [Unitários](./code/unit_test.py)
    - Mutação
    - [Funcionais](./BDD/test.feature)


### Execução dos testes
Como executar a mutação de testes (MutPy):

    $ cd code
    $ mut.py --target functions --unit-test unit_test -m -c

Testes com BDD (Behave):

    behave BDD/features

#### Referências:
https://bitbucket.org/khalas/mutpy
