# Projekt pre predmet Informačné Systémy
## Spustenie projektu
### Spustenie databáze aj webovej aplikácie (pomalšie)
```
docker-compose up --build
```
### Spustenie databáze aj webovej aplikácie (rýchlejšie, lepšie na prácu)
Spustíme si container s databázou do pozadia.
```
docker-compose start iis-database
```
Teraz webovú aplikáciu
```
pipenv install
pipenv shell
```
Nám nainštaluje python moduly do virtuálneho prostredia a pustí shell v virtuálnom prostredí.
(install treba pustiť ak sa zmenia balíky v `Pipfile` súbore)
```
python3 app.py
```
Nám pustí webovú aplikáciu. Potom pre reštart aplikácie stačí len `control + d` a pustiť znova tento posledný príkaz.
Z virtuálneho prostredia sa dá odísť `control + d`.

Databáze na pozadí sa potom vypne príkazom
```
docker-compose stop iis-database
```