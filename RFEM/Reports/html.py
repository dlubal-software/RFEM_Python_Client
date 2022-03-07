#################################
## DEFINITION:
## This feature allows the user to create an output HTML file with the results.
## The results are in the same form as result tables in RFEM.
## The output file is written in HTML and consists of embedded tabular data.
## It will also include dropdown menu with all tables/files.
## Result files are language dependent, so parsing based on strings is impossible.
#################################
from fileinput import filename
from os import listdir, walk, path
from RFEM.initModel import ExportResultTablesToCsv
from re import findall, match

columns = 0

def __HTMLheadAndHeader(modelName, fileNames):
    output = ['<head>',
              '<script src="script.js"></script>',
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
              '<input type="text" list="filter" id="fl" onfocus="this.value=\'\'" onchange="showPanel()" placeholder="Find result table">',
              '<datalist id="filter">']
    for f in fileNames:
        output.append(f'<option>{f}</option>')
    output += ['</datalist>',
               '<button class="button" onclick="switchButtonDown()">&#9664;</button>',
               '<button class="button" onclick="switchButtonUp()">&#9654;</button>',
               '</div>',
               '</header>',
               '',
               '<progress id="progressBar" value="0" max="100"></progress>',
               '']
    return output

def __HTMLfooter():
    return ['<script>atTheEnd()</script>',
            '</div>']

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

def __isWords(word):
    isWords = False
    dividedWords = word.split(' ')

    for oneWord in dividedWords:
        if oneWord and bool(match(r"[A-Z]", oneWord[0])) and oneWord.isalpha():
            isWords = True
        else:
            break

    return isWords

def __tableHeader(dividedLine_1, dividedLine_2):
    # define htnl of header lines, rowspan and colspan
    # parameters are lists of strings
    global columns
    columns = max(len(dividedLine_1), len(dividedLine_2))
    output = ['<script>updateProgressBar()</script>',
              '<div class="tabPanel">',
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
                output.append('<th></th>')
            elif dividedLine_1[i] and dividedLine_2[i]:
                colspan = 1
                for ii in range(i+1, columns):
                    if ii == columns-1 and not dividedLine_1[ii] and __isWords(dividedLine_2[ii]):
                        break
                    elif not dividedLine_1[ii] and dividedLine_2[ii]:
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
    colspan = 1
    output = []
    for c in range(columns):
        if colspan == 1:
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
            elif bool(match(r"^\D+\.$", dividedLine[c])) or "|" in dividedLine[c]:
                for cc in range(c+1, columns-1):
                    if not dividedLine[cc]:
                        colspan += 1
                    else:
                        break
            else:
                if '<sub>' in dividedLine[c] or '[' in dividedLine[c]:
                    tag = 'th'
                    align = 'center'
            output.append(f'<{tag} colspan="{colspan}"align="{align}">{dividedLine[c]}</{tag}>')
        else:
            colspan -= 1
    return output

def ExportResultTablesToHtml(TargetFolderPath: str):
    # Run ExportResultTablesToCsv() to create collection of source files
    #ExportResultTablesToCsv(TargetFolderPath)

    modelName = next(walk(TargetFolderPath))[1][0]
    dirList = listdir(path.join(TargetFolderPath, modelName))
    # Parse CSV file names into LC and CO, analysis type, types of object (nodes, lines, members, surfaces),
    # and tabs (such as summary, Global Deformations, or Support Forces)

    fileNames = []

    dirlist = dirList.sort()

    output = ['<div class="tabContainer">']
    print('')

    for fileName in dirList:
        print(fileName)
        cats = fileName[:-4].split('_')

        fileNameCapitalized = ''
        for c in cats:
            if findall('[0-9]+', c):
                fileNameCapitalized += c+' '
            else:
                fileNameCapitalized += c.capitalize()+' '
        fileNameCapitalized = fileNameCapitalized[:-1]
        fileNames.append(fileNameCapitalized)

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
                #assert columns-len(dividedLine) == 0

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

    output += __HTMLfooter()
    output = __HTMLheadAndHeader(modelName, fileNames) + output

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
