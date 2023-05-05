def list_to_html_ul(string_list):
    ul_start = "<ul>"
    ul_end = "</ul>"
    li_elements = ""

    for string in string_list:
        li_elements += f"<li>{string}</li>"

    html_ul = ul_start + li_elements + ul_end
    return html_ul


def red_text(text:str):
    return f'''<font color = "red">{text}</font>'''


def code(text:str):
    return f'''<code>{text}</code>'''


def inline_math(text:str):
    return f'''\n\n${text}$'''

def block_math(text:str):
    return f'''\n\n$$\n\n{text}\n\n$$'''


def tables(tables:list[str]):
    ret = '''\n<div class="tables-wrapper">\n'''
    for i in tables:
        ret += i
        ret += '\n'
    ret += '</div>'
    return ret


def two_columns(width1:float,width2:float, column1:str, column2:str):
    width1 = width1 * 100
    width2 = width2 * 100
    ret = f'''
<style>
  .two-columns {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    text-align: left;
  }}
  .column1 {{
    width: {width1}%;
  }}
  
  .column2 {{
    width: {width2}%;
  }}
</style>

<div class="two-columns">
  <div class="column1">
    {column1}
  </div>
  <div class="column2">
    {column2}
  </div>
</div>
    
    '''
    return ret
    