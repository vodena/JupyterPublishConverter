import sys
import os

def main():
    print('Jupyter notebook to markdown')
    args = sys.argv[1:]
    if len(args) != 1:
        print('Bad number of passed parameters! No conversion.')
    else:
        ipynbs = os.listdir(args[0])
        converted = []
        for ipynb in ipynbs:
            if ipynb.endswith('.ipynb'):
                converted.append(os.path.splitext(ipynb)[0])
                print('..converting {} to html\n'.format(ipynb))
                ip_path = os.path.join(args[0], ipynb)
                cnvrt = 'jupyter nbconvert --to html ' + ip_path
                os.system(cnvrt)
        for convert in converted:
            convertedhtml = convert + '.html'
            print('..converting {} to md\n'.format(convertedhtml))
            converted_path = os.path.join(args[0], convertedhtml)
            convertedmd = convert + '.md'
            conversion_path = os.path.join(args[0], convertedmd)
            cnvrtmd = 'pandoc ' + converted_path + ' --from html+raw_html --to markdown_strict -o '+ conversion_path
            os.system(cnvrtmd)

if __name__ == '__main__':
    main()