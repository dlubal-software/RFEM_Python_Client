#################################
## DEFINITION:
## This feature allows the user to create an output HTML file with the results.
## The results are in the same form as result tables in RFEM.
## The output file is written in HTML and consists of embedded tabular data.
## It will also include name of the model, 3 drop down menus as in RFEM,
## and data tables will be stuctured into tabs as in RFEM.
#################################
from fileinput import filename
from os import listdir, walk, path
from RFEM.initModel import ExportResultTablesToCsv

columns = 0

def __HTMLheadAndHeader(modelName, category, subCategory, currentCaseOrCombination):
    output = ['<head>',
              '<meta http-equiv="Content-Type" content="text/html; charset=utf-8">',
              '<title>Results</title>',
              '<link rel="icon" sizes="32x32" href="favicon32.png">',
              '</head>',
              '<header>',
              '<link rel="stylesheet" href="styles.css">',
              '<div class="head">',
              '<img alt="Dlubal logo" width="77" height="77" src="favicon32.png" align="right">',
              '<h2>Results report</h2>',
              f'<p>Model: {modelName}</p>',
              '</div>',
              '<div class="head2">',
              '<select class="select" id="category-names">']
    for c in range(len(category)):
        output.append(f'<option value="{c+1}">{list(category)[c]}</option>')
    output += ['</select>',
               '<button class="button" onclick="switchButtonDown(\'category-names\')">&#9664;</button>',
               '<button class="button" onclick="switchButtonUp(\'category-names\')">&#9654;</button>',
               '|',
               '<select class="select" id="subcategory-names">']

    index = 1
    if 'Overview' in subCategory:
        output.append(f'<option value="{index}">Overview</option>')
        index += 1
    if 'Results by Node' in subCategory:
        output.append(f'<option value="{index}">Results by Node</option>')
        index += 1
    if 'Results by Lines' in subCategory:
        output.append(f'<option value="{index}">Results by Lines</option>')
        index += 1
    if 'Results by Surfaces' in subCategory:
        output.append(f'<option value="{index}">Results by Surfaces</option>')
        index += 1
    if 'Results by Members' in subCategory:
        output.append(f'<option value="{index}">Results by Members</option>')
        index += 1
    if 'Results by Solids' in subCategory:
        output.append(f'<option value="{index}">Results by Solids</option>')

    output += ['</select>',
               '<button class="button" onclick="switchButtonDown(\'subcategory-names\')">&#9664;</button>',
               '<button class="button" onclick="switchButtonUp(\'subcategory-names\')">&#9654;</button>',
               '|',
               '<select class="select" id="caseOrCombination-names">']
    for i in range(len(currentCaseOrCombination)):
        output.append(f'<option value="{i+1}">{list(currentCaseOrCombination)[i]}</option>')
    output += ['</select>',
               '<button class="button" onclick="switchButtonDown(\'caseOrCombination-names\')">&#9664;</button>',
               '<button class="button" onclick="switchButtonUp(\'caseOrCombination-names\')">&#9654;</button>',
               '</div>',
               '</header>',
               '',
               '<div class="loader" id="spin"></div>',
               '']
    return output

def __HTMLfooter(sTabs):
    output = ['<div class="buttonContainer">']
    for i in range(len(sTabs)):
        output += f'<button id="tab{i}" onclick="showPanel({i},\'#fff5cc\')">{sTabs[i]}</button>',
    output += ['</div>',
              '</div>',
              '<script src="script.js"></script>']
    return output

def __isEmpty(dividedLine):
    # returns True if all strings are empty
    return not any (dividedLine)

def __numberOfPOsitiveItems(dividedLine):
    # return number of list items which are not empty
    counter = 0
    for i in dividedLine:
        if i:
            counter += 1

    return counter

def __tableHeader(dividedLine_1, dividedLine_2):
    # define htnl of header lines, rowspan and colspan
    # parameters are lists of strings
    global columns
    columns = max(len(dividedLine_1), len(dividedLine_2))
    output = ['<div class="tabPanel">',
              '<table class="responsive-table">',
              '<thead>',
              '<tr>']
    if __isEmpty(dividedLine_1):
        __emptyLine()
    else:
        for i in range(columns):
            if dividedLine_1[i] and not dividedLine_2[i]:
                output.append(f'<th rowspan="2">{dividedLine_1[i]}</th>')
            elif not dividedLine_1[i] and not dividedLine_2[i]:
                output.append(f'<th></th>')
            elif dividedLine_1[i] and dividedLine_2[i]:
                colspan = 1
                for ii in range(i+1, columns):
                    if not dividedLine_1[ii] and ('Comment' not in dividedLine_2[ii]) and dividedLine_2[ii]:
                        colspan += 1
                    else:
                        break
                output.append(f'<th colspan="{colspan}">{dividedLine_1[i]}</th>')
                i += colspan-1
    output += ['</tr>', '<tr>']

    for y in range(columns):
        if not dividedLine_1[y] and not dividedLine_2[y]:
            output.append('<th></th>')
        elif dividedLine_1[y] and not dividedLine_2[y]:
            pass
        else:
            output.append(f'<th>{dividedLine_2[y]}</th>')

    output += ['</tr>', '</thead>']
    return output

def __tableSubHeader(dividedLine):
    # sub header; one liner; in the body of table
    global columns
    return f'<th align="left" colspan="{columns}">{dividedLine}</th>'

def __emptyLine():
    # define html of empty lines
    global columns
    return f'<th colspan="{columns}"></th>'

def __otherLines(dividedLine):
    # define html of other lines
    global columns
    output = []
    for c in range(columns):
        sCheckIfDigit = dividedLine[c].replace('.','',1)
        sCheckIfDigit = sCheckIfDigit.replace(',','',1)
        sCheckIfDigit = sCheckIfDigit.replace('-','',1)
        sCheckIfDigit = sCheckIfDigit.replace('+','',1)
        align = 'left'
        tag = 'td'
        if c == 0:
            align = 'center'
        elif sCheckIfDigit.isdigit():
            align = 'right'
        else:
            if '<sub>' in dividedLine[c] or '[' in dividedLine[c]:
                tag = 'th'
                align = 'center'
        output.append(f'<{tag} align="{align}">{dividedLine[c]}</{tag}>')
    return output

def ExportResultTablesToHtml(TargetFolderPath: str):
    # Run ExportResultTablesToCsv() to create collection of source files
    #ExportResultTablesToCsv(TargetFolderPath)

    modelName = next(walk(TargetFolderPath))[1][0]
    dirList = listdir(path.join(TargetFolderPath, modelName))
    # Parse CSV file names into LC and CO, analysis type, types of object (nodes, lines, members, surfaces),
    # and tabs (such as summary, Global Deformations, or Support Forces)

    # Sets of all catebories (not duplicates)
    # Source for 3 drop down menus
    sCurrentCaseOrCombinations = set()
    sCategories = set()
    sSubcategories = set()
    sTabs = []

    dirlist = dirList.sort()

    output = ['<div class="tabContainer">',
	          '<link rel="stylesheet" href="styles.css">']
    print('')
    for fileName in dirList:
        print(fileName)
        cats = fileName[:-4].split('_')
        currentCaseOrCombination = ''
        subcategory = ''
        category = ''
        tab = ''

        if cats[1] == 'design':
            category = str(cats[0]).capitalize()+' '+str(cats[1]).capitalize()
            if cats[2]=='errors' or cats[2]+cats[3]=='notvalid':
                subcategory = 'Overview'
                for i in range(2, len(cats)):
                    tab += str(cats[i]+' ').capitalize()
                tab = tab[:-1]
            elif cats[2]=='design':
                subcategory = str('Design Ratios on'+str(cats[5]).capitalize())
                tab = 'Design Ratios by'
                for i in range(7, len(cats)):
                    tab += str(cats[i]+' ').capitalize()
                tab = tab[:-1]
            elif cats[3]=='reinforcement':
                subcategory = 'Reinforcement on '+str(cats[5]).capitalize
                tab = str(cats[2]).capitalize+' Reinforcement by'
                for i in range(7, len(cats)):
                    tab += str(cats[i]+' ').capitalize()
                tab = tab[:-1]
            elif cats[4]=='reinforcement':
                subcategory = 'Reinforcement on '+str(cats[6]).capitalize
                tab = 'Not Covered Reinforcement by'
                for i in range(8, len(cats)):
                    tab += str(cats[i]+' ').capitalize()
                tab = tab[:-1]
            elif cats[2]=='governing':
                subcategory = 'Governing Results'
            else:
                assert True, filename

        if cats[0] == 'stress' and cats[1] == 'analysis':
            category = 'Stress-Strain Analysis'
            if cats[2]=='errors':
                subcategory = 'Overview'
            elif cats[2]=='':
                subcategory = 'Design Rations on Members'
            elif cats[2]=='':
                subcategory = 'Reinforcement on Members'
            elif cats[2]=='':
                subcategory = 'Design Rations on Surfaces'
            elif cats[2]=='':
                subcategory = 'Reinforcement on Surfaces'
            elif cats[2]=='':
                subcategory = 'Governing Results'
            else:
                assert True, filename

        else:
            currentCaseOrCombination = cats[0]
            category = str(cats[1]).capitalize()+' '+str(cats[2]).capitalize()

            if cats[3]=='summary':
                subcategory = 'Overview'
            elif cats[3]=='nodes':
                subcategory = 'Results by Node'
            elif cats[3]=='lines':
                subcategory = 'Results by Lines'
            elif cats[3]=='surfaces':
                subcategory = 'Results by Surfaces'
            elif cats[3]=='members':
                subcategory = 'Results by Members'
            elif cats[3]=='solids':
                subcategory = 'Results by Solids'
            else:
                assert True, filename
            if not tab:
                if cats[3]=='summary':
                    tab = cats[3].capitalize()
                else:
                    for i in range(4, len(cats)):
                        tab += str(cats[i]+' ').capitalize()
                    tab = tab[:-1]

        sCategories.add(category)
        sCurrentCaseOrCombinations.add(currentCaseOrCombination)
        sSubcategories.add(subcategory)
        sTabs.append(tab)

        with open(path.join(TargetFolderPath, modelName, fileName), mode='r', encoding='utf-8-sig') as f:
            lines = f.readlines()
            # 1st header always consists of first 2 lines
            line_1 = lines[0].split(';')
            line_1[-1] = line_1[-1].rstrip('\n')
            line_2 = lines[1].split(';')
            line_2[-1] = line_2[-1].rstrip('\n')
            subOutput = __tableHeader(line_1, line_2)
            output += subOutput
            output.append('<tbody>')

            for line in lines[2:]:
                output.append('<tr>')
                dividedLine = line.split(';')
                dividedLine[-1] = dividedLine[-1].rstrip('\n')

                # check if number of columns is always same
                assert columns-len(dividedLine) == 0

                if __isEmpty(dividedLine):
                    # if empty line
                    output.append(__emptyLine())
                elif __numberOfPOsitiveItems(dividedLine) == 1 and dividedLine[1]:
                    # if only one string in the list, it is sub header consisting of only 1 line
                    output.append(__tableSubHeader(dividedLine[1]))
                else:
                    subOutput = __otherLines(dividedLine)
                    output += subOutput

            output += ['</tr>', '</tbody>', '</table>', '</div>']

    output += __HTMLfooter(sTabs)
    output = __HTMLheadAndHeader(modelName, sCategories, sSubcategories, sCurrentCaseOrCombinations) + output

    # Write into html file
    # Add lower index
    with open('D:\\Sources\\sub_index.html', "w", encoding="utf-8") as f:
        for line in output:
            while '_' in line:
                beginId = line.find('_')
                endBySpace = line[beginId:].find(' ')
                endByArrow = line.rfind('<')
                if endBySpace == -1:
                    line = line[:beginId]+'<sub>'+line[beginId+1:endByArrow]+'</sub>'+line[endByArrow:]
                else:
                    endId = min(endBySpace + beginId, endByArrow)
                    line = line[:beginId]+'<sub>'+line[beginId+1:endId]+'</sub>'+line[endId:]
            while '^' in line:
                beginId = line.find('^')
                endBySpace = line[beginId:].find(' ')
                endByArrow = line.rfind('<')
                if endBySpace == -1:
                    line = line[:beginId]+'<sup>'+line[beginId+1:endByArrow]+'</sup>'+line[endByArrow:]
                else:
                    endId = min(endBySpace + beginId, endByArrow)
                    line = line[:beginId]+'<sup>'+line[beginId+1:endId]+'</sup>'+line[endId:]
            f.write(line+'\n')