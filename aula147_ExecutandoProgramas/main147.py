import subprocess

"windows -  ping ip da propria maquina 127.0.0.1"
"linux - ping"

# run vai executar
proc = subprocess.run(
    ['ping', '127.0.0.1'],
    capture_output=True,
    text=True,
)



#saida em si
saida = proc.stdout
print(saida)


