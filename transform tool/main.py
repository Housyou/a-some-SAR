import sys
import re
import base64


def replace_tex(inline_tag, directory):
    filename = 'a0/天线中的口径面积-波束范围(Aperture-beam-area)的关系式.md'

    def dashrepl(matchobj, tag):
        formular = matchobj.group(1)
        return tag.format(formular, formular)
    inline_pattern = "\$\n*(.*?)\n*\$"
    interline_pattern = '\$%s\$' % inline_pattern
    interline_tag = '\n%s\n' % inline_tag

    with open('../origin ver/'+filename, 'r', encoding='UTF-8') as f:
        content = f.read()
        content = re.sub(interline_pattern, lambda mo: dashrepl(
            mo, interline_tag), content)
        content = re.sub(inline_pattern, lambda mo: dashrepl(
            mo, inline_tag), content)
        with open(directory+'/'+filename.split('/')[-1], 'w', encoding='UTF-8') as f:
            f.write(content)


def md2zhihu():
    inline_tag = '<img src="https://www.zhihu.com/equation?tex={}" alt="{}" class="ee_img tr_noresize" eeimg="1">'
    replace_tex(inline_tag, '../zhihu ver')


def md2github():
    inline_tag = '<img src="https://render.githubusercontent.com/render/math?math={}" />'
    replace_tex(inline_tag, '..')


def img2base64():
    filename = '3.png'
    with open(filename, 'rb') as f:
        res = 'data:image/png;base64,' + \
            str(base64.b64encode(f.read()), encoding='utf-8')
        print(res)


def img_url(name):
    res = 'https://raw.githubusercontent.com/Housyou/a-some-SAR/master/origin%20ver/a0/imgs/' + '%s.png' % name
    print(res)


if __name__ == '__main__':
    # img_url('1')
    md2zhihu()
    md2github()