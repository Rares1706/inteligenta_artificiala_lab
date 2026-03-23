[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=23238039&assignment_repo_type=AssignmentRepo)
# 🚀 Python Assignment – Control Flow & Functions

> 🎯 *Scop: consolidarea bazelor în Python prin exerciții practice.*

---

## 📌 Ce vei aplica

* structuri de control (`if`, `elif`, `else`)
* bucle (`for`, `while`)
* validarea inputului
* funcții și reutilizarea codului
* expresii lambda
* concepte de programare funcțională
* comprehensions

---

## 🧠 Teorie pe scurt

### 🔹 Structuri condiționale

Permit programului să ia decizii:

```python
if condiție:
    # cod
elif altă_condiție:
    # cod
else:
    # cod
```

---

### 🔹 Bucle

Repetă execuția unui bloc de cod:

```python
for element in colecție:
    # cod

while condiție:
    # cod
```

---

### 🔹 Funcții

Blocuri de cod reutilizabile:

```python
def nume_functie(parametri):
    return rezultat
```

---


### 🔹 *args și **kwargs

Uneori nu știm câte argumente vom primi într-o funcție.

---

#### 🔸 *args (argumente poziționale)

Permite transmiterea unui număr variabil de argumente → sunt stocate într-un **tuple**.

```python
def suma(*args):
    print(args)
```

Apel:

```python
suma(1, 2, 3)
```

Rezultat:

```
(1, 2, 3)
```

👉 Practic: toate valorile sunt grupate într-un tuple.

---

#### 🔸 **kwargs (argumente cheie-valoare)

Permite transmiterea argumentelor sub formă de **dicționar**.

```python
def afisare(**kwargs):
    print(kwargs)
```

Apel:

```python
afisare(nume="Ana", varsta=20)
```

Rezultat:

```
{'nume': 'Ana', 'varsta': 20}
```

👉 Practic: fiecare argument are un nume → devine cheie în dicționar.

---

#### 🔸 Exemplu combinat (foarte util)

```python
def exemplu(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)
```

Apel:

```python
exemplu(1, 2, 3, nume="Ana", oras="Cluj")
```

Rezultat:

```
args: (1, 2, 3)
kwargs: {'nume': 'Ana', 'oras': 'Cluj'}
```

---

💡 *Folosește `*args` când nu știi câte valori primești și `**kwargs` când vrei flexibilitate cu perechi cheie-valoare (ex: produse și prețuri).*


---

### 🔹 Expresii lambda

Funcții anonime, scrise pe o singură linie:

```python
lambda x: x * 2
```

---

### 🔹 Funcții utile

* `map()` → aplică o funcție pe fiecare element
* `filter()` → filtrează elemente după o condiție
* `zip()` → combină mai multe colecții

---

### 🔹 Comprehensions

Mod rapid de a crea colecții:

```python
[x for x in listă if condiție]
```

---

## 🧩 Cerințe

### 🔹 1. Evaluarea unei note

Scrieți un program care:

* citește o notă de la tastatură
* verifică dacă este validă (între 0 și 10)
* afișează calificativul:

  * 9–10 → Excelent
  * 7–8 → Bine
  * 5–6 → Suficient
  * sub 5 → Reexaminare
* dacă valoarea este invalidă, cere reintroducerea

---

### 🔹 2. Analiza unui comentariu

Scrieți un program care:

* citește un comentariu de la utilizator
* verifică dacă acesta conține cuvinte pozitive sau negative

Liste:

* pozitive: `["bine", "frumos", "super", "excelent", "minunat"]`
* negative: `["urât", "prost", "groaznic", "dezamăgitor"]`

Output:

* „Comentariu pozitiv!”
* „Comentariu negativ!”
* „Comentariu neutru.”

---

### 🔹 3. Generare factură

Scrieți o funcție:

* care primește numele clientului
* primește un număr variabil de produse și prețuri folosind `**kwargs`
* afișează produsele și calculează totalul

---

### 🔹 4. Lambda – pătrate

Creați o expresie lambda care:

* primește o listă de numere
* returnează o listă cu elementele ridicate la pătrat

Ex:

```
[1, 2, 3] → [1, 4, 9]
```

---

### 🔹 5. Sortare cu lambda

Sortați lista de tupluri:

```
[(0, 2), (4, 3), (9, 9), (10, -1)]
```

în funcție de al doilea element din fiecare tuplu.

---

### 🔹 6. Filtrare cu lambda

Scrieți un program care:

* primește o listă de numere
* separă numerele pare de cele impare folosind `filter()`

---

### 🔹 7. Prelucrare listă (None)

Aveți o listă de prețuri care conține valori `None`:

* eliminați valorile `None`
* aplicați o reducere de 10% asupra valorilor rămase

---

### 🔹 8. Prelucrare dată

Pentru un string de forma:

```
2023-04-24 09:03:32.744178
```

extrageți:

* anul
* luna
* ziua
* ora

---

### 🔹 9. Sumă liste

Scrieți o funcție care:

* primește două liste de numere
* returnează o listă de tupluri cu suma elementelor corespunzătoare (folosind `zip()`)

---

### 🔹 10. List Comprehension

Realizați:

* o listă cu numere pare între 0 și 100
* o listă cu cuburile primelor 10 numere
* o listă cu elementele comune din două liste

---

### 🔹 11. Set Comprehension

Realizați:

* un set cu primele 10 numere pare
* un set cu literele distincte dintr-un string
* un set cu cuvintele care au cel puțin 5 litere

---

### 🔹 12. Dictionary Comprehension

Realizați:

* un dicționar cu chei 1–10 și valori pătratele lor
* un dicționar cu frecvența literelor dintr-un string
* un dicționar cu numerele 1–10 și lista divizorilor lor

---
