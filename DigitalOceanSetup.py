#script_for_DigitalOcean
import paramiko


def ssh_command(hostname, commands):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        # Подключение с использованием ключа SSH
        client.connect(hostname)

        for command in commands:
            stdin, stdout, stderr = client.exec_command(command)
            print(f"Output of command '{command}':")
            for line in stdout:
                print(line.strip())
            
            exit_status = stdout.channel.recv_exit_status()
            if exit_status == 0:
                print(f"Command '{command}' executed successfully")
            else:
                print(f"Error executing command '{command}', exit status: {exit_status}")

    finally:
        client.close()




# Вводим имя домена
hostname = input("Enter ip server name: ").split(' ')
domain_name = input("Enter domain name: ").split(' ')
print(f"Just press enter if you want to leave .env")
print(f"ENV files are entered via _")
env_name = input("enter_env:")

# Список команд для выполнения
commands = [
    f"cp /etc/nginx/sites-available/virusfreeprotect.com  /etc/nginx/sites-available/{domain_name}",
    f'sed -i "s/virusfreeprotect.com/{domain_name}/g" /etc/nginx/sites-available/{domain_name}',
    f'sed -i "s/.env_a2/.env{env_name}/g" /etc/nginx/sites-available/{domain_name}',
    f"ln -s /etc/nginx/sites-available/{domain_name} /etc/nginx/sites-enabled/"
]

if len(domain_name) != len(hostname):
    print("Number of domains and hostnames should match.")
else:
    for i in range(len(hostname)):
        ssh_command(hostname, commands)