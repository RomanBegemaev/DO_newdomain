#script_for_DigitalOcean
import subprocess

# Вводим имя домена
domain_name = input("Enter domain name: ")

# Список команд для выполнения
commands = [
    f"rm /etc/nginx/site-enabled/virusfreeprotect.com ",
    f"cp /etc/nginx/sites-available/virusfreeprotect.com  /etc/nginx/sites-available/{domain_name}",
    f'sed -i "s/virusfreeprotect.com /{domain_name}/g" /etc/nginx/sites-available/{domain_name}',
    f"ln -s /etc/nginx/sites-available/{domain_name} /etc/nginx/sites-enabled/"
]

# Выполнение команд
for command in commands:
    print(f"Выполняется команда: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        print("Команда успешно выполнена.")
    else:
        print(f"Ошибка при выполнении команды: {result.stderr}")