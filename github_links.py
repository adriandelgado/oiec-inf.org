import os
from collections import defaultdict
from github import Github

access_token = os.getenv("ACCESS_TOKEN")
repo_name = "OIEC/Banco-de-Pruebas"
repo_dir = ""
path_to_yaml = "github_links.yaml"


def dicOfLinks(repo):
    contents = repo.get_contents(repo_dir)
    dic = defaultdict(
        lambda: defaultdict(
            lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(str)))
        )
    )

    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            dir_split = file_content.path.split("/")
            if dir_split[-1] == "cases" or dir_split[-1] == "soluciones":
                year = dir_split[-4]
                activity = dir_split[-5]
                olympiad = dir_split[-3]
                problem = dir_split[-2]
                typ = dir_split[-1]
                link = file_content.html_url
                dic[year][activity][olympiad][problem][typ] = link
            else:
                contents.extend(repo.get_contents(file_content.path))
    return dic


def writeDic(f, dic, space):
    for key in sorted(dic.keys()):
        writeDir(f, key, space)
        if type(dic[key]) == defaultdict:
            writeDic(f, dic[key], space + 1)
        else:
            f.write("  " * (space + 1) + dic[key] + "\n")


def writeDir(f, directory, space):
    f.write("  " * space + directory + ":\n")


def dicToYaml(dic, path_to_yaml):
    f = open(path_to_yaml, "w")
    writeDic(f, dic, 0)
    f.close()


def createYamlFile(repo, path_to_yaml):
    dic = dicOfLinks(repo)
    dicToYaml(dic, path_to_yaml)


def main():
    g = Github(access_token)
    repo = g.get_repo(repo_name)
    createYamlFile(repo, path_to_yaml)


if __name__ == "__main__":
    main()
