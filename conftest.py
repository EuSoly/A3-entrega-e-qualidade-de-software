# conftest.py
# Configuração compartilhada por todos os testes (o pytest carrega este arquivo sozinho).
# - Fixture `driver`: abre o Chrome antes de cada teste e fecha ao final,
#   mesmo quando o teste falha (item 7 do enunciado).
# - Hook de evidência: ao fim de cada teste tira um print e salva em
#   evidencias/CT-XXX_APROVADO.png ou evidencias/CT-XXX_REPROVADO.png (item 8).
