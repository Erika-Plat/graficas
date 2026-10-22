import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Datos
df = pd.DataFrame({
    "mes": ["Ene", "Feb", "Mar", "Abr", "May", "Jun"],
    "ventas": [1200, 1800, 1500, 2400, 2200, 3000],
    "clientes": [40, 55, 48, 70, 65, 90],
})

# Crear la figura con 1 fila y 2 columnas
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# Gráfico 1: Barras para ventas
sns.barplot(data=df, x="mes", y="ventas", ax=axes[0], color="royalblue")
axes[0].set_title("Ventas por mes")
axes[0].set_ylabel("Ventas ($)")
axes[0].set_xlabel("Mes")

# Gráfico 2: Línea para clientes
sns.lineplot(
    data=df,
    x="mes",
    y="clientes",
    marker="o",
    linewidth=3,
    ax=axes[1],
    color="darkorange",
)
axes[1].set_title("Clientes por mes")
axes[1].set_ylabel("Número de clientes")
axes[1].set_xlabel("Mes")

# Título general y ajuste de diseño
plt.suptitle("Dashboard de ventas", fontsize=16)
plt.tight_layout()

# Guardar la imagen en el directorio de trabajo
plt.savefig("dashboard_ventas.png", dpi=300)
print("Dashboard guardado exitosamente como 'dashboard_ventas.png'")