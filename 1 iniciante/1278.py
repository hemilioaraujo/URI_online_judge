texto = '''3
     ROMEO      AND
      JULIET WERE  
        IN LOVE    
4
WHO
ELSE
LOVES
STAIRS
3
A TEXT CAN BE JUSTIFIED
ON   BOTH   SIDES    OR
JUST   TO   THE   RIGHT
0'''


linhas = []

ultimo = 0

for i, letra in enumerate(texto):

    if letra == "\n":
        linhas.append(texto[ultimo:i])
        ultimo = i + 1

print(linhas)

