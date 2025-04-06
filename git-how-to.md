# Инструкции по работе с SSH и GitHub

## 1. Создание SSH-ключа

```bash
# Генерация нового SSH-ключа (используйте email, привязанный к GitHub)
ssh-keygen -t ed25519 -C "your_email@example.com"

# Или, если система не поддерживает Ed25519:
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

# Запуск ssh-agent в фоновом режиме
eval "$(ssh-agent -s)"

# Добавление SSH-ключа в ssh-agent
ssh-add ~/.ssh/id_ed25519  # или id_rsa, если использовали RSA