import os
import requests
from collections import defaultdict

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

rootURL = "https://github.com/OIEC/Banco-de-Pruebas/tree/main"

apiURL = (
    "https://api.github.com/repos/OIEC/Banco-de-Pruebas/git/trees/main?recursive=true"
)

before_table = """{{ define "main" }}
  <main class="items-center flex-1 mx-4 mt-4 md:mx-12 lg:mx-24 sm:mt-16">
    <article
      class="mb-16 prose text-gray-700 sm:mx-auto lg:prose-lg prose-blue"
    >
      <h1>{{ .Title }}</h1>
        <table>
"""

after_table = """</table>
    </article>
  </main>
{{ end }}
"""


def main():
    directories = get_directories_from_API(apiURL)

    ONI_HTML = oni_table(directories)

    selectivos_HTML = selectivos_table(directories)

    with open(
        os.path.join(BASE_DIR, "layouts/banco-de-pruebas", "section.html"), "w"
    ) as page:
        page.write(selectivos_HTML)


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


if __name__ == "__main__":
    main()
