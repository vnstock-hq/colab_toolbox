wget https://github.com/quarto-dev/quarto-cli/releases/download/v1.4.553/quarto-1.4.553-linux-amd64.tar.gz
mkdir -p /content/quarto
tar -xvzf quarto-1.4.553-linux-amd64.tar.gz -C /content/quarto
/content/quarto/quarto-1.4.553/bin/quarto install tinytex