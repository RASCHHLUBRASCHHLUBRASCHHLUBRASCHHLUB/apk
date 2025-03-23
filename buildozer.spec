[app]

# Nome do aplicativo
title = MeuApp

# Nome do pacote (deve ser único)
package.name = meuapp

# Nome do domínio (invertido, por convenção)
package.domain = org.meuapp

# Versão do aplicativo (formato: major.minor.revision)
version = 0.1

# Código da versão (deve ser um número inteiro)
version.code = 1

# Diretório onde está o código-fonte
source.dir = ./

# Extensões de arquivos a serem incluídos no APK
source.include_exts = py,png,jpg,kv,atlas

# Diretórios ou padrões de arquivos a serem incluídos
source.include_patterns = assets/*,images/*,fonts/*

# Requisitos do Python (bibliotecas necessárias)
requirements = python3,kivy

# Permissões do Android (se necessário)
android.permissions = INTERNET

# Versão do Android SDK
android.sdk = 24

# Versão do Android NDK
android.ndk = 25b

# Versão das ferramentas de compilação
android.build_tools_version = 34.0.0

# Orientação da tela (portrait ou landscape)
orientation = portrait

# Ícone do aplicativo (caminho para o arquivo .png)
# (Se você não tem um ícone, comente ou remova esta linha)
# icon.filename = %(source.dir)s/data/icon.png

# Tela de carregamento (splash screen)
# (Se você não tem uma tela de carregamento, comente ou remova esta linha)
# presplash.filename = %(source.dir)s/data/presplash.png

# Logotipo do aplicativo
# (Se você não tem um logotipo, comente ou remova esta linha)
# logo.filename = %(source.dir)s/data/logo.png

# Ativar ou desativar o console (útil para depuração)
fullscreen = 0

# Configurações de depuração
log_level = 2

# Configurações de release (assinar o APK)
# (comente essas linhas se não quiser assinar o APK)
# android.release_artifact = .apk
# android.keystore = mykey.keystore
# android.keystore_password = senha_da_chave
# android.keyalias = mykeyalias
# android.keyalias_password = senha_do_alias
