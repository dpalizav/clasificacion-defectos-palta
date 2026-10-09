"""Ejecuta el EDA completo usando el Python activo, sin entrenar modelos."""
from pathlib import Path
import sys
import nbformat
from nbclient import NotebookClient
from jupyter_client import KernelManager


def main():
    ruta = Path(__file__).resolve().with_name("01_EDA.ipynb")
    notebook = nbformat.read(ruta, as_version=4)
    gestor = KernelManager(kernel_name="python3")
    # Evita utilizar por accidente el Python de otro entorno registrado.
    gestor.kernel_spec.argv = [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"]
    cliente = NotebookClient(notebook, km=gestor, timeout=1200,
                             resources={"metadata": {"path": str(ruta.parent)}})
    try:
        cliente.execute()
        nbformat.validate(notebook)
    finally:
        # Conserva también las salidas útiles si alguna celda falla.
        nbformat.write(notebook, ruta)
        if gestor.has_kernel:
            gestor.shutdown_kernel(now=True)
    print("EDA completado: notebook y reportes guardados.")


if __name__ == "__main__":
    main()
