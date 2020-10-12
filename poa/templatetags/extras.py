from django import template

register = template.Library()

@register.filter(name='porcentaje')
def calculaperct(value, arg):
    try:
        resultado = (float(value) / float(arg) * 100)
        return resultado
    except:
        return 0