import os
import sys
from re import findall, match
from shutil import copy

PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.ImportExport.exports import ExportResultTablesToCSV

columns = 0

def __HTMLheadAndHeader(modelName, fileNames):
    '''
    Create header of the file.
    '''
    output = ['<head>',
              '<script src="htmlScript.js"></script>',
              '<meta http-equiv="Content-Type" content="text/html; charset=utf-8">',
              '<title>Results</title>',
              '<link rel="icon" sizes="32x32" href="favicon32.png">',
              '</head>',
              '<header>',
              '<link rel="stylesheet" href="htmlStyles.css">',
              '<div class="head">',
              '<img alt="Dlubal logo" width="77" height="77" src="favicon32.png" align="right">',
              '<h2>Result report</h2>',
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
               '<div class="tabContainer">']
    for f in fileNames:
        output.append(f'<iframe src="{f}.html" loading="lazy" frameBorder="0"></iframe>')
    return output

def __HTMLfooter():
    '''
    Create footer.
    '''
    return ['<script>atTheEnd()</script>',
            '</div>']

def __isEmpty(dividedLine):
    '''
    Returns True if all strings are empty.
    '''
    return not any (dividedLine)

def __numberOfPOsitiveItems(dividedLine):
    '''
    Get number of list items which are not empty.
    '''
    counter = 0
    for i in dividedLine:
        if i:
            counter += 1

    return counter

def __isWords(word):
    '''
    Check if 'word' consists of general words.
    '''
    isWords = False
    dividedWords = word.split(' ')

    for oneWord in dividedWords:
        if oneWord and bool(match(r"[A-Z]", oneWord[0])) and oneWord.isalpha():
            isWords = True
        else:
            break

    return isWords

def __tableHeader(dividedLine_1, dividedLine_2):
    '''
    Define html of header lines, rowspan and colspan.
    Parameters are lists of strings.
    '''
    global columns
    columns = max(len(dividedLine_1), len(dividedLine_2))
    output = ['<div class="tabPanel">',
              '<link rel="stylesheet" href="htmlStyles.css">',
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
                    if not dividedLine_1[ii] and dividedLine_2[ii]:
                        colspan += 1
                    else:
                        break
                output.append(f'<th colspan="{colspan}">{dividedLine_1[i]}</th>')
                i += colspan-1
            elif i==columns-1 and not dividedLine_1[i] and dividedLine_2[i]:
                output.append('<th></th>')
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
    '''
    Sub header; one liner; in the body of table
    '''
    return f'<th align="left" colspan="{columns}">{dividedLine}</th>'

def __emptyLine():
    '''
    Define html of empty lines
    '''
    return f'<th colspan="{columns}"></th>'

def __otherLines(dividedLine):
    '''
    Define html of other lines
    '''
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

def __writeToFile(TargetFilePath, output):
    '''
    Write into html file
    '''
    with open(TargetFilePath, "w", encoding="utf-8") as f:
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

def ExportResultTablesToHtml(TargetFolderPath: str):
    '''
    This feature allows the user to create an output HTML file with the results.
    The results are in the same form as result tables in RFEM.
    The output file is written in HTML and consists of embedded tabular data.
    It will also include dropdown menu with all tables/files.
    Result files are language dependent, so parsing based on strings is impossible.

    Args:
        TargetFolderPath (str): Destination path to the directory
    '''
    # Create collection of source files
    ExportResultTablesToCSV(TargetFolderPath)

    modelName = next(os.walk(TargetFolderPath))[1][0]
    dirList = os.listdir(os.path.join(TargetFolderPath, modelName))

    fileNames = []
    dirList.sort()

    for fileName in dirList:
        cats = fileName[:-4].split('_')

        fileNameCapitalized = ''
        for c in cats:
            if findall('[0-9]+', c):
                fileNameCapitalized += c+' '
            else:
                fileNameCapitalized += c.capitalize()+' '
        fileNameCapitalized = fileNameCapitalized[:-1]
        fileNames.append(fileNameCapitalized)

        with open(os.path.join(TargetFolderPath, modelName, fileName), mode='r', encoding='utf-8-sig') as f:
            lines = f.readlines()
            # 1st header always consists of first 2 lines
            line_1 = lines[0].split(';')
            line_1[-1] = line_1[-1].rstrip('\n')
            line_2 = lines[1].split(';')
            line_2[-1] = line_2[-1].rstrip('\n')

            output = __tableHeader(line_1, line_2)
            output.append('<tbody>')

            for line in lines[2:]:
                output.append('<tr>')
                dividedLine = line.split(';')
                dividedLine[-1] = dividedLine[-1].rstrip('\n')

                if __isEmpty(dividedLine):
                    # if empty line
                    output.append(__emptyLine())
                elif __numberOfPOsitiveItems(dividedLine) == 1 and dividedLine[0]:
                    # add empty line, these values doesn't make sence
                    output.append(__emptyLine())
                elif __numberOfPOsitiveItems(dividedLine) == 1 and dividedLine[1]:
                    # if only one string in the list, it is sub header consisting of only 1 line
                    output.append(__tableSubHeader(dividedLine[1]))
                else:
                    output += __otherLines(dividedLine)

            output += ['</tr>', '</tbody>', '</table>', '</div>']

        __writeToFile(os.path.join(TargetFolderPath, fileNameCapitalized+'.html'), output)

    indexOutput = ['<div class="tabContainer">']
    indexOutput += __HTMLfooter()
    indexOutput = __HTMLheadAndHeader(modelName, fileNames) + indexOutput

    # Copy basic files
    dirname = os.path.join(os.getcwd(), os.path.dirname(__file__))
    copy(os.path.join(dirname, 'htmlStyles.css'), TargetFolderPath)
    copy(os.path.join(dirname, 'htmlScript.js'), TargetFolderPath)
    copy(os.path.join(dirname, 'favicon32.png'), TargetFolderPath)

    with open(os.path.join(TargetFolderPath,'index.html'), "w", encoding="utf-8") as f:
        for line in indexOutput:
            f.write(line+'\n')

    # Open result html page
    os.system(f"start {os.path.join(TargetFolderPath, 'index.html')}")