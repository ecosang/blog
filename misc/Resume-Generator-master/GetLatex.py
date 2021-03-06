import json

'''
Function to get project resume tex.
args:
    namelist: a list contains all Project name
'''
def getProLatex(namelist,full=True):
    rs = ""
    d = {}
    for filename in ["ProjectJson/Project.json"]:
        with open(filename, 'r') as f:
            obj = json.load(f)
        for i in obj:
            name = i["name"]
            date = i['date']
            place = i['place']
            title = i['title']
            tech = i['tech']
            bull = ""
            if name not in namelist:
                continue
            for s in i["bullet"]:
                bull += "\\item{{{0}}}\n".format(s)
            for t in tech:
                if t in bull:
                    bull = bull.replace(t, "\\textbf{{{0}}}".format(t))
            if full==False:
                template = "\\datedsubsection{{\\textbf{{{0}}}}}{{{1}}} \n\\begin{{itemize}}\n{2}\\end{{itemize}}\n".format(name, date,bull)
            else:
                template = "\\datedsubsection{{\\textbf{{{0}}}}}{{{1}}} \n\\role{{{2}}} {{\\hfill {3}}}\n\\begin{{itemize}}{4}\\end{{itemize}}\n".format(name, place,title,date,bull)
            d[name]=template
    for i in namelist:
        rs+=d[i]
    return rs

def getAwardLatex(namelist,full=True):
    rs = ""
    d = {}
    for filename in ["ProjectJson/Award.json"]:
        with open(filename, 'r') as f:
            obj = json.load(f)
        for i in obj:
            name = i["name"]
            date = i['date']
            place = i['place']
            title = i['title']
            tech = i['tech']
            bull = ""
            if name not in namelist:
                continue
            for s in i["bullet"]:
                bull += "\\item{{{0}}}\n".format(s)
            for t in tech:
                if t in bull:
                    bull = bull.replace(t, "\\textbf{{{0}}}".format(t))
            if full==False:
                template = "\\datedsubsection{{\\textbf{{{0}}}}}{{{1}}} \n\\begin{{itemize}}\n{2}\\end{{itemize}}\n".format(name, date,bull)
            else:
                template = "\\datedsubsection{{\\textbf{{{0}}}}}{{{1}}} \n\\role{{{2}}} {{\\hfill {3}}}\n\\begin{{itemize}}{4}\\end{{itemize}}\n".format(name, place,title,date,bull)
            d[name]=template
    for i in namelist:
        rs+=d[i]
    return rs
'''
Function to get skill resume tex.
args:
    name: your skill id
'''

def getSkillLatex(name):
    with open("ProjectJson/SkillSet.json", 'r') as f:
        obj = json.load(f)
    rs = "\\begin{itemize}\n"
    for i in obj:
        if i["id"]==name:
            for k in i:
                if k=="id":
                    continue
                s2 = ", ".join(i[k])
                rs += "\\item \\textbf{{{0}}}: {{{1}}}\n".format(k,s2)
    rs+="\\end{itemize}\n"
    return rs
    

def getPublicationLatex(namelist,full=True):
    rs = ""
    d = {}
    for filename in ["ProjectJson/Publication.json"]:
        with open(filename, 'r') as f:
            obj = json.load(f)
        for i in obj:
            name = i["name"]
            date = i['date']
            place = i['place']
            title = i['title']
            tech = i['tech']
            bull = ""
            if name not in namelist:
                continue
            for s in i["bullet"]:
                bull += "\\item{{{0}}}\n".format(s)
            for t in tech:
                if t in bull:
                    bull = bull.replace(t, "\\textbf{{{0}}}".format(t))
            if full==False:
                template = "\\datedsubsection{{\\textbf{{{0}}}}}{{{1}}} \n\\begin{{itemize}}\\setlength\\itemsep{{0.5em}}\\setlength\\itemindent{{-.1in}}\n{2}\\end{{itemize}}\n".format(name, date,bull)
            else:
                template = "\\datedsubsection{{\\textbf{{{0}}}}}{{{1}}} \n\\role{{{2}}} {{\\hfill {3}}}\n\\begin{{itemize}}{4}\\setlength\\itemsep{{0.5em}}\\setlength\\itemindent{{-.1in}}\\end{{itemize}}\n".format(name, place,title,date,bull)
            d[name]=template
    for i in namelist:
        rs+=d[i]
    return rs


'''
Function to get Education resume tex.
args:
    education: your education id
'''
def getEductionLatex(education):
    rs = ""
    for filename in ["ProjectJson/Education.json"]:
        with open(filename, 'r') as f:
            obj = json.load(f)
        for i in obj:
            name = i["name"]
            date = i['date']
            place = i['place']
            title = i['title']
            tech = i['tech']
            bull = ""
            if i["id"]!= education:
                continue
            for s in i["bullet"]:
                bull += "\\item{{{0}}}\n".format(s)
            for t in tech:
                if t in bull:
                    bull = bull.replace(t, "\\textbf{{{0}}}".format(t))
            template = "\\datedsubsection{{\\textbf{{{0}}}}}{{{1}}} \n\\role{{{2}}} {{\\hfill {3}}}\n\\begin{{itemize}}\n{4}\\end{{itemize}}\n".format(name, place,title,date,bull)
            rs+= template
    return rs

'''
Function to get Experience resume tex.
args:
    experience: your Experience id
'''
def getExperience(experience):
    rs = ""
    for filename in ["ProjectJson/Experience.json"]:
        with open(filename, 'r') as f:
            obj = json.load(f)
        for i in obj:
            name = i["name"]
            date = i['date']
            place = i['place']
            title = i['title']
            tech = i['tech']
            bull = ""
            if i["id"]!= experience:
                continue
            for s in i["bullet"]:
                bull += "\\item{{{0}}}\n".format(s)
            for t in tech:
                if t in bull:
                    bull = bull.replace(t, "\\textbf{{{0}}}".format(t))
            template = "\\datedsubsection{{\\textbf{{{0}}}}}{{{1}}} \n\\role{{{2}}} {{\\hfill   {3}}}\n\\begin{{itemize}}\n{4}\\end{{itemize}}\n".format(name, place,title,date,bull)
            rs+= template
    return rs


def getResearchExperience(experience):
    rs = ""
    for filename in ["ProjectJson/ResearchExperience.json"]:
        with open(filename, 'r') as f:
            obj = json.load(f)
        for i in obj:
            name = i["name"]
            date = i['date']
            place = i['place']
            title = i['title']
            tech = i['tech']
            bull = ""
            if i["id"]!= experience:
                continue
            for s in i["bullet"]:
                bull += "\\item{{{0}}}\n".format(s)
            for t in tech:
                if t in bull:
                    bull = bull.replace(t, "\\textbf{{{0}}}".format(t))
            template = "\\datedsubsection{{\\textbf{{{0}}}}}{{{1}}} \n\\role{{{2}}} {{\\hfill   {3}}}\n\\begin{{itemize}}\n{4}\\end{{itemize}}\n".format(name, place,title,date,bull)
            rs+= template
    return rs
    