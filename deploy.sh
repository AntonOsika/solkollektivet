set -ex
unzip -o ~/Downloads/sk.zip -d .
mv -f Sol*.html index.html
git add .
git commit -m 'deploy macro' 
git push
echo check result: https://antonosika.github.io/solkollektivet/
