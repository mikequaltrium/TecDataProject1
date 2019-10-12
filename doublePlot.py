# Genera una gráfica con eje secundario:
#
# Parámetros
# title: Título de la gráfica
# xlabel: Etiqueta del eje X
# ylabel1: Etiqueta del eje principal Y
# ylabel2: Etiqueta del eje secundario Y
# xSet: Nombre de los ticks X
# ySet1: Set de datos principal Y
# ySet2: Set de datos secundarios Y
#
#
# Returns
# Devuelve la impresión de pantalla de la gráfica
# Guarda un archivo con la gráfica, el nombre es el mismo del título de la gráfica, 
# lo guarda en el mismo folder del archivo que la llama


def doblePlot(title, xlabel, ylabel1, ylabel2, xSet, ySet1, ySet2): 
    
    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel1, color=color)
    ax1.plot(xSet, ySet1, color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    plt.xticks(rotation=45)
    plt.title(title)
    
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel(ylabel2, color=color)  # we already handled the x-label with ax1
    ax2.plot(xSet, ySet2, color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    plt.show()
    fig.savefig(title)