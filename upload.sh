make clean
make html
git co gh-pages
cp -pr _build/html/* ./
git add .
git commit -m 'update gh-pages'
git push origin gh-pages
git co master

