import markdown
import codecs
import pypandoc
import pdflatex


def txt2html(txt_path):
    input_file = codecs.open(txt_path, mode='r', encoding="utf-8")

    text = input_file.read()
    html = markdown.markdown(text)

    html_path = txt_path[:-3] + 'html'
    output_file = codecs.open(html_path, mode='w', encoding="utf-8")
    output_file.write(html)

    return html_path


def html2word(html_path):
    word_path = html_path[:-4] + 'docx'
    pypandoc.convert_file(html_path, 'docx', outputfile=word_path)

    return word_path


def word2pdf(word_path):
    pdf_path = word_path[:-4] + 'pdf'
    pypandoc.convert_file(word_path, 'pdf', outputfile=pdf_path)

    return pdf_path
