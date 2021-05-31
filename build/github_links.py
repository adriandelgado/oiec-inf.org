import os
import requests
from collections import defaultdict
import fileinput

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

rootURL = "https://github.com/OIEC/Banco-de-Pruebas/tree/main"

apiURL = (
    "https://api.github.com/repos/OIEC/Banco-de-Pruebas/git/trees/main?recursive=true"
)

before_table = """{{< rawhtml >}}\n\n<table>"""
after_table = """</table>\n\n{{< /rawhtml >}}"""


def main():
    directories = get_directories_from_API(apiURL)

    ONI_HTML = oni_table(directories)
    ONI_dir = os.path.join(BASE_DIR, "content/banco-de-pruebas/oni", "index.md")
    insert_into_markdown(ONI_dir, ONI_HTML)

    selectivos_HTML = selectivos_table(directories)
    selectivos_dir = os.path.join(
        BASE_DIR, "content/banco-de-pruebas/selectivos", "index.md"
    )
    insert_into_markdown(selectivos_dir, selectivos_HTML)


def get_directories_from_API(url):
    response = requests.get(url).json()

    directories = defaultdict(lambda: defaultdict(lambda: defaultdict(set)))

    for leaf in response["tree"]:
        if (
            leaf["type"] == "tree"
            and leaf["path"].count("/") == 4
            and not leaf["path"].startswith("Entrenamientos")
        ):
            olimpiada, year, fase, problema, _ = leaf["path"].split("/")
            directories[olimpiada][year][fase].add(problema)
    return directories


def oni_table(directories):
    heading = "<thead><tr><th>Olimpiada</th><th>Fase</th><th>Problema</th><th>Casos</th><th>Soluciones</th></tr></thead>\n<tbody>\n"
    titulo = "ONI"
    return create_table(directories, heading, titulo)


def selectivos_table(directories):
    heading = "<thead><tr><th>Año</th><th>Olimpiada</th><th>Problema</th><th>Casos</th><th>Soluciones</th></tr></thead>\n<tbody>\n"
    titulo = "Selectivos"
    return create_table(directories, heading, titulo)


def create_table(directories, heading, titulo):
    html = ""
    for year, fases in directories[titulo].items():
        num_problemas = 0
        yearHTML = heading
        for fase, problemas in fases.items():
            num_problemas += len(problemas)
            once = False
            for problema in sorted(problemas):
                link = f"{rootURL}/{titulo}/{year}/{fase}/{problema}"
                if once:
                    yearHTML += f'<tr><td>{problema}</td><td><a href="{link}/cases">Github</a></td><td><a href="{link}/soluciones">Github</a></td></tr>\n'
                else:
                    yearHTML += f'<tr><td rowspan="{len(problemas)}">{fase}</td><td>{problema}</td><td><a href="{link}/cases">Github</a></td><td><a href="{link}/soluciones">Github</a></td></tr>\n'
                    once = True
        corte = len(heading) + 4
        html += (
            yearHTML[:corte]
            + f'<td rowspan="{num_problemas}">{year}</td>'
            + yearHTML[corte:]
            + "</tbody>\n"
        )

    return before_table + html + after_table


def insert_into_markdown(directory, raw_html):
    with fileinput.input(directory, inplace=True) as md:
        for line in md:
            if line == "{{< rawhtml >}}\n":
                print(raw_html)
                break
            print(line, end="")


if __name__ == "__main__":
    main()
