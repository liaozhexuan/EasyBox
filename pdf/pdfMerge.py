import os
import PyPDF2


def getFileList(basePath):
    file_list = os.listdir(basePath)
    file_list.sort(key=lambda x: int(os.path.splitext(x)[0]))
    result = []
    for file in file_list:
        suffix = os.path.splitext(file)[1]
        if suffix == ".pdf":
            result.append(os.path.join(basePath, file))
    return result


def merge(basePath, filename):
    file_list = getFileList(basePath)
    file_out = PyPDF2.PdfFileWriter()
    for file in file_list:
        print(str(file) + " will be merged")
        file_reader = PyPDF2.PdfFileReader(file, strict=False)
        for pageNum in range(file_reader.getNumPages()):
            file_out.addPage(file_reader.getPage(pageNum))
        print(str(file) + " is already merged")

    with open('{}.pdf'.format(os.path.join(basePath, filename)), 'wb') as output:
        file_out.write(output)
    return


if __name__ == '__main__':
    # FilePath can be pasted from Windows Explorer directly, and "/" & "\" can be extracted successfully
    InputFilePath = r"C:\Users\xxx"
    OutputFileName = r"result"
    # filepath = filepath.replace("\\", "/")
    merge(InputFilePath, OutputFileName)
