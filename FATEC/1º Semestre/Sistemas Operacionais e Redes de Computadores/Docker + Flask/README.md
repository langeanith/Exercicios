https://docs.docker.com/engine/install/ubuntu/

# Removendo uma instalação do Docker:
```console
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

Desinstalando o Docker Engine:
```console
sudo apt-get purge docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin docker-ce-rootless-extras
```

Removendo todas imagens, containers e volumes:
```console
 sudo rm -rf /var/lib/docker
 sudo rm -rf /var/lib/container
``` 
Arquivos editados de configuração devem ser removidos manualmente.

# Instalação do pacote Docker (Ubuntu):
Configuração do repositório:
```console
sudo apt-get update
```
```console
sudo apt-get install ca-certificates curl gnupg
```

Adição da chave oficial GPG do Docker:
```console
sudo install -m 0755 -d /etc/apt/keyrings
```
```console
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```
```console
sudo chmod a+r /etc/apt/keyrings/docker.gpg
```

Use o seguinte comando para configurar o repositório:
```console
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

Instalação do Docker Engine:
```console
sudo apt-get update
```

```console
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Teste para confirmar que a instalação foi feita com sucesso:
```console
sudo docker run hello-world
```

# Instalação do Docker Compose (Ubuntu):
```console
sudo apt-get update
sudo apt-get install docker-compose-plugin
```

# Baixando os arquivos e executando o compose:
```console
git clone https://github.com/langeanith/Exercicios.git
```

```console
mv Exercicios/FATEC/1º\ Semestre/Sistemas\ Operacionais\ e\ Redes\ de\ Computadores/Docker\ +\ Flask/ Docker
```

```console
sudo rm Exercicios/ -r
```

```console
cd Docker
sudo docker compose build
```

```console
sudo docker compose up
```

Acessar no IPv4 público na porta 5000
