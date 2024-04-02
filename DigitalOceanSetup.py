#script_for_DigitalOcean
import subprocess

# Вводим имя домена
domain_name = input("Enter domain name: ")
print(f"Don't enter anything if you want to leave .env")
print(f"ENV files are entered via _")
env_name = input("enter_env:")

# Список команд для выполнения
commands = [
    f"rm /etc/nginx/sites-enabled/virusfreeprotect.com",
    f"cp /etc/nginx/sites-available/virusfreeprotect.com  /etc/nginx/sites-available/{domain_name}",
    f'sed -i "s/virusfreeprotect.com/{domain_name}/g" /etc/nginx/sites-available/{domain_name}',
    f'sed -i "s/.env_a2/.env{env_name}/g" /etc/nginx/sites-available/{domain_name}',
    f"ln -s /etc/nginx/sites-available/{domain_name} /etc/nginx/sites-enabled/"
]



# Выполнение командп
for command in commands:
    print(f"Load command: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        print("Succses")
    else:
        print(f"Error {result.stderr}")